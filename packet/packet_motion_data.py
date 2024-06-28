import struct
from packet.packet_header import PacketHeader
from data.motion_data import CarMotionData


class PacketMotionData:
    def __init__(self, m_header, m_carMotionData):
        self.m_header = m_header
        self.m_carMotionData = m_carMotionData

    def pack(self):
        packed_header = self.m_header.pack()
        packed_car_motion_data = b''.join([car_data.pack() for car_data in self.m_carMotionData])
        return packed_header + packed_car_motion_data

    @classmethod
    def unpack(cls, data):
        header_size = struct.calcsize('<HBBBBBQfII2B')
        car_motion_data_size = struct.calcsize('<3f3f6h3f3f')
        num_cars = 22
        
        m_header = PacketHeader.unpack(data[:header_size])
        m_carMotionData = [
            CarMotionData.unpack(data[header_size + i * car_motion_data_size: header_size + (i + 1) * car_motion_data_size])
            for i in range(num_cars)
        ]
        
        return cls(m_header, m_carMotionData)