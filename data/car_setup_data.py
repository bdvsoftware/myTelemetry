import struct

class CarSetupData:
    
    format = '<4B4f8B4fBf'
    def __init__(self,
                 m_frontWing,
                 m_rearWing,
                 m_onThrottle,
                 m_offThrottle,
                 m_frontCamber,
                 m_rearCamber,
                 m_frontToe,
                 m_rearToe,
                 m_frontSuspension,
                 m_rearSuspension,
                 m_frontAntiRollBar,
                 m_rearAntiRollBar,
                 m_frontSuspensionHeight,
                 m_rearSuspensionHeight,
                 m_brakePressure,
                 m_brakeBias,
                 m_rearLeftTyrePressure,
                 m_rearRightTyrePressure,
                 m_frontLeftTyrePressure,
                 m_frontRightTyrePressure,
                 m_ballast,
                 m_fuelLoad):
        self.m_frontWing = m_frontWing
        self.m_rearWing = m_rearWing
        self.m_onThrottle = m_onThrottle
        self.m_offThrottle = m_offThrottle
        self.m_frontCamber = m_frontCamber
        self.m_rearCamber = m_rearCamber
        self.m_frontToe = m_frontToe
        self.m_rearToe = m_rearToe
        self.m_frontSuspension = m_frontSuspension
        self.m_rearSuspension = m_rearSuspension
        self.m_frontAntiRollBar = m_frontAntiRollBar
        self.m_rearAntiRollBar = m_rearAntiRollBar
        self.m_frontSuspensionHeight = m_frontSuspensionHeight
        self.m_rearSuspensionHeight = m_rearSuspensionHeight
        self.m_brakePressure = m_brakePressure
        self.m_brakeBias = m_brakeBias
        self.m_rearLeftTyrePressure = m_rearLeftTyrePressure
        self.m_rearRightTyrePressure = m_rearRightTyrePressure
        self.m_frontLeftTyrePressure = m_frontLeftTyrePressure
        self.m_frontRightTyrePressure = m_frontRightTyrePressure
        self.m_ballast = m_ballast
        self.m_fuelLoad = m_fuelLoad

    def pack(self):
        return struct.pack(
            self.format,
            self.m_frontWing,
            self.m_rearWing,
            self.m_onThrottle,
            self.m_offThrottle,
            self.m_frontCamber,
            self.m_rearCamber,
            self.m_frontToe,
            self.m_rearToe,
            self.m_frontSuspension,
            self.m_rearSuspension,
            self.m_frontAntiRollBar,
            self.m_rearAntiRollBar,
            self.m_frontSuspensionHeight,
            self.m_rearSuspensionHeight,
            self.m_brakePressure,
            self.m_brakeBias,
            self.m_rearLeftTyrePressure,
            self.m_rearRightTyrePressure,
            self.m_frontLeftTyrePressure,
            self.m_frontRightTyrePressure,
            self.m_ballast,
            self.m_fuelLoad)
    
    @classmethod
    def unpack(cls, data):
        unpackped_data = struct.unpack(cls.format, data)
        return cls(*unpackped_data)
    
    def to_json(self):
        return self.__dict__