import struct

class CarMotionData:

    format = '<3f3f6h3f3f'

    def __init__(self, m_worldPositionX, m_worldPositionY, m_worldPositionZ, 
                 m_worldVelocityX, m_worldVelocityY, m_worldVelocityZ,
                 m_worldForwardDirX, m_worldForwardDirY, m_worldForwardDirZ,
                 m_worldRightDirX, m_worldRightDirY, m_worldRightDirZ,
                 m_gForceLateral, m_gForceLongitudinal, m_gForceVertical,
                 m_yaw, m_pitch, m_roll):
        self.m_worldPositionX = m_worldPositionX
        self.m_worldPositionY = m_worldPositionY
        self.m_worldPositionZ = m_worldPositionZ
        self.m_worldVelocityX = m_worldVelocityX
        self.m_worldVelocityY = m_worldVelocityY
        self.m_worldVelocityZ = m_worldVelocityZ
        self.m_worldForwardDirX = m_worldForwardDirX
        self.m_worldForwardDirY = m_worldForwardDirY
        self.m_worldForwardDirZ = m_worldForwardDirZ
        self.m_worldRightDirX = m_worldRightDirX
        self.m_worldRightDirY = m_worldRightDirY
        self.m_worldRightDirZ = m_worldRightDirZ
        self.m_gForceLateral = m_gForceLateral
        self.m_gForceLongitudinal = m_gForceLongitudinal
        self.m_gForceVertical = m_gForceVertical
        self.m_yaw = m_yaw
        self.m_pitch = m_pitch
        self.m_roll = m_roll

    def pack(self):
        return struct.pack(self.format, 
                           self.m_worldPositionX,
                           self.m_worldPositionY,
                           self.m_worldPositionZ,
                           self.m_worldVelocityX,
                           self.m_worldVelocityY,
                           self.m_worldVelocityZ,
                           self.m_worldForwardDirX,
                           self.m_worldForwardDirY,
                           self.m_worldForwardDirZ,
                           self.m_worldRightDirX,
                           self.m_worldRightDirY,
                           self.m_worldRightDirZ,
                           self.m_gForceLateral,
                           self.m_gForceLongitudinal,
                           self.m_gForceVertical,
                           self.m_yaw,
                           self.m_pitch,
                           self.m_roll)

    @classmethod
    def unpack(cls, data):
        unpacked_data = struct.unpack(cls.format, data)
        return cls(*unpacked_data)