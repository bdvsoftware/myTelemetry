import struct
import json
from packet.packet_header import PacketHeader
from data.lap_data import LapData

class PacketLapData:
    format = "<" + PacketHeader.format + (LapData.format * 22) + "BB"

    def __init__(self, m_header, m_lapData, m_timeTrialPBCarIdx, m_timeTrialRivalCarIdx):
        self.m_header = m_header
        self.m_lapData = m_lapData
        self.m_timeTrialPBCarIdx = m_timeTrialPBCarIdx
        self.m_timeTrialRivalCarIdx = m_timeTrialRivalCarIdx

    def pack(self):
        packed_header = self.m_header.pack()
        packed_lap_data = b''.join([lap_data.pack() for lap_data in self.m_lapData])
        packed_data = packed_header + packed_lap_data + struct.pack("<BB", self.m_timeTrialPBCarIdx, self.m_timeTrialRivalCarIdx)
        return packed_data

    @classmethod
    def unpack(cls, data):
        header_size = struct.calcsize(PacketHeader.format)
        lap_data_size = struct.calcsize(LapData.format)
        num_cars = 22

        m_header = PacketHeader.unpack(data[:header_size])
        m_lapData = [
            LapData.unpack(data[header_size + i * lap_data_size: header_size + (i + 1) * lap_data_size])
            for i in range(num_cars)
        ]
        m_timeTrialPBCarIdx, m_timeTrialRivalCarIdx = struct.unpack_from("<BB", data, header_size + num_cars * lap_data_size)

        return cls(m_header, m_lapData, m_timeTrialPBCarIdx, m_timeTrialRivalCarIdx)
    
    def to_json(self):
        return json.dumps({
            'm_header': self.m_header.to_json(),  # Suponiendo que PacketHeader tiene un método to_json()
            'm_lapData': [lap_data.to_json() for lap_data in self.m_lapData],  # Suponiendo que LapData tiene un método to_json()
            'm_timeTrialPBCarIdx': self.m_timeTrialPBCarIdx,
            'm_timeTrialRivalCarIdx': self.m_timeTrialRivalCarIdx
        })
