import json

class PacketSend:

    def __init__(self, packet):
        self.id = packet.m_header.m_packetId
        self.data = packet

    def to_json(self):
        return json.dumps({
            'id': self.id,
            'data': self.data.to_json()
        })