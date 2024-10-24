import struct
import json
from packet.packet_header import PacketHeader
from data.car_telemetry_data import CarTelemetryData

class PacketCarTelemetryData:
    additional_fields_format = "2Bb"

    format = "<" + PacketHeader.format + (CarTelemetryData * 22) + additional_fields_format

    def __init__(self, m_header, m_carTelemetryData, m_mfdPanelIndex, m_mfdPanelIndexSecondaryPlayer, m_suggestedGear):
        self.m_header = m_header
        self.m_carTelemetryData = m_carTelemetryData
        self.m_mfdPanelIndex = m_mfdPanelIndex
        self.m_mfdPanelIndexSecondaryPlayer = m_mfdPanelIndexSecondaryPlayer
        self.m_suggestedGear = m_suggestedGear

    def pack(self):
        packed_header = self.m_header.pack()
        packed_cat_telemetry_data = b''.join([telem.pack() for telem in self.m_carTelemetryData])
        packed_data = packed_header + packed_cat_telemetry_data + struct.pack(self.additional_fields_format, self.m_mfdPanelIndex, self.m_mfdPanelIndexSecondaryPlayer, self.m_suggestedGear)
        return packed_data
    
    @classmethod
    def unpack(self, cls, data):
        num_cars = 22
        header_size = struct.calcsize(PacketHeader.format)
        car_telemetry_data_size = struct.calcsize(CarTelemetryData.format)
        m_header = PacketHeader.unpack(data[:header_size])
        m_carTelemetryData = [
            CarTelemetryData.unpack(data[header_size + i * car_telemetry_data_size: header_size + (i + 1) * car_telemetry_data_size])
            for i in range(num_cars)
        ]
        m_mfdPanelIndex, m_mfdPanelIndexSecondaryPlayer, m_suggestedGear = struct.unpack_from(self.additional_fields_format , data, header_size + num_cars * car_telemetry_data_size)
        return cls(m_header, m_carTelemetryData, m_mfdPanelIndex, m_mfdPanelIndexSecondaryPlayer, m_suggestedGear)
    
    def to_json(self):
        json.dumps({
            'm_header': self.m_header.to_json(),
            'm_carTelemetryData': [car_telem.to_json() for car_telem in self.m_carTelemetryData],
            'm_mfdPanelIndex': self.m_mfdPanelIndex,
            'm_mfdPanelIndexSecondaryPlayer': self.m_mfdPanelIndexSecondaryPlayer,
            'm_suggestedGear': self.m_suggestedGear
        })
    
