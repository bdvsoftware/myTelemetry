import struct
from scapy.all import sniff, UDP

from packet.packet_header import PacketHeader
from packet.packet_motion_data import PacketMotionData
from packet.packet_lap_data import PacketLapData

from kafka.packet_lapdata_event_producer import PacketLapDataEventProducer


def capturePacketMontion(udp_payload):
    try:
        motion_packet = PacketMotionData.unpack(udp_payload)
        print(motion_packet.__dict__)
    except struct.error as e:
        print(f"Error unpacking MOTION packet: {e}")

def capturePacketLapData(udp_payload):
    try:
        lap_data_packet = PacketLapData.unpack(udp_payload)
        producer = PacketLapDataEventProducer()
        producer.produce(lap_data_packet.to_json())
    except struct.error as e:
        print(f"Error unpacking LAP DATA packet: {e}")
    finally:
        producer.close()

switch_funct = {
    0: capturePacketMontion,
    2: capturePacketLapData
}

accepted_packet_ids = [2]

# Función callback para manejar los paquetes capturados
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

# Sniff en localhost y llama a packet_callback para cada paquete capturado
sniff(filter="udp port 20777", prn=packet_callback, store=0, iface="Ethernet")
