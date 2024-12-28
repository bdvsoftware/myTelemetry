import struct
from scapy.all import sniff, UDP

from packet.packet_header import PacketHeader
from packet.packet_motion_data import PacketMotionData
from packet.packet_lap_data import PacketLapData
from packet.packet_motion_ex_data import PacketMotionExData
from packet.packet_car_telemetry_data import PacketCarTelemetryData

from kafka.packet_created_event_producer import PacketCreatedEventProducer


def capturePacketMotion(udp_payload):
    try:
        motion_packet = PacketMotionData.unpack(udp_payload)
        producer = PacketCreatedEventProducer()
        producer.produce(motion_packet, stint_name)
    except struct.error as e:
        print(f"Error unpacking MOTION packet: {e}")
    finally:
        producer.close()

def capturePacketMotionEx(udp_payload):
    try:
        producer = PacketCreatedEventProducer()
        motion_packet_ex = PacketMotionExData.unpack(udp_payload)
        producer.produce(motion_packet_ex, stint_name)
    except struct.error as e:
        print(f"Error unpacking MOTION-EX packet: {e}")
    finally:
        producer.close()

def capturePacketLapData(udp_payload):
    try:
        producer = PacketCreatedEventProducer()
        lap_data_packet = PacketLapData.unpack(udp_payload)
        producer.produce(lap_data_packet, stint_name)
    except struct.error as e:
        print(f"Error unpacking LAP DATA packet: {e}")
    finally:
        producer.close()

def capturePacketCarTelemetryData(udp_payload):
    try:
        producer = PacketCreatedEventProducer()
        packet_car_telemetry_data = PacketCarTelemetryData.unpack(PacketCarTelemetryData, udp_payload)
        producer.produce(packet_car_telemetry_data, stint_name)
    except struct.error as e:
        print(f"Error unpacking CAR TELEMETRY packet: {e}")
    finally:
        producer.close()

switch_funct = {
    0: capturePacketMotion,
    2: capturePacketLapData,
    6: capturePacketCarTelemetryData,
    13: capturePacketMotionEx
}

accepted_packet_ids = [0, 2, 6, 13]

# Packet managing
def packet_callback(packet):
    if UDP in packet and packet[UDP].dport == 20777:
        udp_payload = bytes(packet[UDP].payload)
        try:
            packet_header = PacketHeader.unpack(udp_payload[:struct.calcsize(PacketHeader.format)])
            analyzePacketType(packet_header.m_packetId, udp_payload)
        except struct.error as e:
            print(f"Error unpacking packet: {e}")

def analyzePacketType(packet_header_id: int, udp_payload):
    if(packet_header_id in accepted_packet_ids):
        switch_funct.get(packet_header_id)(udp_payload)

# Request stint name from the user
global stint_name
stint_name = input("Please enter the stint name: ")
print(f"Stint name set to: {stint_name}")
# Sniffing
sniff(filter="udp port 20777", prn=packet_callback, store=0, iface="Ethernet")
