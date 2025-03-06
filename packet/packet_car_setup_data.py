import struct
from packet.packet_header import PacketHeader
from data.car_setup_data import CarSetupData

class PacketCarSetupData:
    
    def __init__(self, m_header, m_carSetups):
        self.m_header = m_header
        self.m_carSetups = m_carSetups

    def pack(self):
        packed_header = self.m_header.pack()
        packed_car_setup_data = b''.join([car_setup_data.pack() for car_setup_data in self.m_carSetups])
        return packed_header + packed_car_setup_data
    
    @classmethod
    def unpack(cls, data):
        header_size = struct.calcsize(PacketHeader.format)
        car_setup_data_size = struct.calcsize(CarSetupData.format)
        num_cars = 22
        
        m_header = PacketHeader.unpack(data[:header_size])
        m_carSetups = [
            CarSetupData.unpack(data[header_size + i * car_setup_data_size: header_size + (i + 1) * car_setup_data_size])
            for i in range(num_cars)
        ]
        
        return cls(m_header, m_carSetups)
    
    def to_json(self):
        return {
            'm_header': self.m_header.to_json(),
            'm_carSetups': [car_setup.to_json() for car_setup in self.m_carSetups]
        }