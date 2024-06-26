from scapy.all import sniff, UDP

def packet_callback(packet):
    if UDP in packet and packet[UDP].dport == 20777:
        print(packet.show())

# Sniff en localhost y llama a packet_callback para cada paquete capturado
sniff(filter="udp port 20777", prn=packet_callback, store=0, iface="Ethernet")
