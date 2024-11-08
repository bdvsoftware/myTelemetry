import json

class PacketSend:

    types = {0: "motionPacketData",
                   2: "lapDataPacketData",
                   6: "carTelemetryPacketData",
                   13: "motionExPacketData"}

    def __init__(self, packet):
        self.id = packet.m_header.m_packetId
        self.packet_type = self.types.get(self.id)
        self.data = packet

    def to_json(self):
        return json.dumps({
            'id': self.id,
            'packetType': self.packet_type,
            'data': self.data.to_json()
        })