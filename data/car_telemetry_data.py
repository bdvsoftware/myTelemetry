import struct
import json

class CarTelemetryData:
    format = '<H3fBbH2BH4H4B4BH4f4B'

    def __init__(self, m_speed, m_throttle, m_steer, m_brake, m_clutch, m_gear, m_engineRPM,
                 m_drs, m_revLightsPercent, m_revLightsBitValue, m_brakesTemperature,
                 m_tyresSurfaceTemperature, m_tyresInnerTemperature, m_engineTemperature,
                 m_tyresPressure, m_surfaceType):
        self.m_speed = m_speed
        self.m_throttle = m_throttle
        self.m_steer = m_steer
        self.m_brake = m_brake
        self.m_clutch = m_clutch
        self.m_gear = m_gear
        self.m_engineRPM = m_engineRPM
        self.m_drs = m_drs
        self.m_revLightsPercent = m_revLightsPercent
        self.m_revLightsBitValue = m_revLightsBitValue
        self.m_brakesTemperature = m_brakesTemperature
        self.m_tyresSurfaceTemperature = m_tyresSurfaceTemperature
        self.m_tyresInnerTemperature = m_tyresInnerTemperature
        self.m_engineTemperature = m_engineTemperature
        self.m_tyresPressure = m_tyresPressure
        self.m_surfaceType = m_surfaceType

    def pack(self):
        return struct.pack(self.format,
                           self.m_speed,
                           self.m_throttle,
                           self.m_steer,
                           self.m_brake,
                           self.m_clutch,
                           self.m_gear,
                           self.m_engineRPM,
                           self.m_drs,
                           self.m_revLightsPercent,
                           self.m_revLightsBitValue,
                           *self.m_brakesTemperature,
                           *self.m_tyresSurfaceTemperature,
                           *self.m_tyresInnerTemperature,
                           self.m_engineTemperature,
                           *self.m_tyresPressure,
                           *self.m_surfaceType)

    @classmethod
    def unpack(cls, data):
        # Desempaquetar los datos desde binario
        unpacked_data = struct.unpack(cls.format, data)
        return cls(
            unpacked_data[0],  # m_speed
            unpacked_data[1],  # m_throttle
            unpacked_data[2],  # m_steer
            unpacked_data[3],  # m_brake
            unpacked_data[4],  # m_clutch
            unpacked_data[5],  # m_gear
            unpacked_data[6],  # m_engineRPM
            unpacked_data[7],  # m_drs
            unpacked_data[8],  # m_revLightsPercent
            unpacked_data[9],  # m_revLightsBitValue
            unpacked_data[10:14],  # m_brakesTemperature
            unpacked_data[14:18],  # m_tyresSurfaceTemperature
            unpacked_data[18:22],  # m_tyresInnerTemperature
            unpacked_data[22],  # m_engineTemperature
            unpacked_data[23:27],  # m_tyresPressure
            unpacked_data[27:31]  # m_surfaceType
        )

    def to_json(self):
        return {
            'm_speed': self.m_speed,
            'm_throttle': self.m_throttle,
            'm_steer': self.m_steer,
            'm_brake': self.m_brake,
            'm_clutch': self.m_clutch,
            'm_gear': self.m_gear,
            'm_engineRPM': self.m_engineRPM,
            'm_drs': self.m_drs,
            'm_revLightsPercent': self.m_revLightsPercent,
            'm_revLightsBitValue': self.m_revLightsBitValue,
            'm_brakesTemperature': list(self.m_brakesTemperature),
            'm_tyresSurfaceTemperature': list(self.m_tyresSurfaceTemperature),
            'm_tyresInnerTemperature': list(self.m_tyresInnerTemperature),
            'm_engineTemperature': self.m_engineTemperature,
            'm_tyresPressure': list(self.m_tyresPressure),
            'm_surfaceType': list(self.m_surfaceType)
        }
