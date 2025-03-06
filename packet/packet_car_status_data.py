import struct
from packet.packet_header import PacketHeader
from data.car_status_data import CarStatusData

class PacketCarStatusData:

    def __init__(self, m_header, m_carStatusData):
        self.m_header = m_header
        self.m_carStatusData = m_carStatusData

    def pack(self):
        packed_header = self.m_header.pack()
        packed_car_status_data = b''.join([car_status_data.pack() for car_status_data in self.m_carStatusData])
        return packed_header + packed_car_status_data
    
    @classmethod
    def unpack(cls, data):
        header_size = struct.calcsize(PacketHeader.format)
        car_status_data_size = struct.calcsize(CarStatusData.format)
        num_cars = 22
        
        m_header = PacketHeader.unpack(data[:header_size])
        m_carStatusData = [
            CarStatusData.unpack(data[header_size + i * car_status_data_size: header_size + (i + 1) * car_status_data_size])
            for i in range(num_cars)
        ]
        
        return cls(m_header, m_carStatusData)
    
    def to_json(self):
        return {
            'm_header': self.m_header.to_json(),
            'm_carStatusData': [car_status.to_json() for car_status in self.m_carStatusData]
        }