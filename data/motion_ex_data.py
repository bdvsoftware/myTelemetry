import struct

class CarMotionExData:
    
    format = '<4f4f4f4f4f4f4f4f11f4f'

    def __init__(self, 
                 m_suspensionPosition, 
                 m_suspensionVelocity, 
                 m_suspensionAcceleration,
                 m_wheelSpeed, 
                 m_wheelSlipRatio, 
                 m_wheelSlipAngle,
                 m_wheelLatForce, 
                 m_wheelLongForce, 
                 m_heightOfCOGAboveGround,
                 m_localVelocityX, 
                 m_localVelocityY, 
                 m_localVelocityZ,
                 m_angularVelocityX, 
                 m_angularVelocityY, 
                 m_angularVelocityZ,
                 m_angularAccelerationX, 
                 m_angularAccelerationY, 
                 m_angularAccelerationZ, 
                 m_frontWheelsAngle,
                 m_wheelVertForce):
        self.m_suspensionPosition = m_suspensionPosition
        self.m_suspensionVelocity = m_suspensionVelocity
        self.m_suspensionAcceleration = m_suspensionAcceleration
        self.m_wheelSpeed = m_wheelSpeed
        self.m_wheelSlipRatio = m_wheelSlipRatio
        self.m_wheelSlipAngle = m_wheelSlipAngle
        self.m_wheelLatForce = m_wheelLatForce
        self.m_wheelLongForce = m_wheelLongForce
        self.m_heightOfCOGAboveGround = m_heightOfCOGAboveGround
        self.m_localVelocityX = m_localVelocityX
        self.m_localVelocityY = m_localVelocityY
        self.m_localVelocityZ = m_localVelocityZ
        self.m_angularVelocityX = m_angularVelocityX
        self.m_angularVelocityY = m_angularVelocityY
        self.m_angularVelocityZ = m_angularVelocityZ
        self.m_angularAccelerationX = m_angularAccelerationX
        self.m_angularAccelerationY = m_angularAccelerationY
        self.m_angularAccelerationZ = m_angularAccelerationZ
        self.m_frontWheelsAngle = m_frontWheelsAngle
        self.m_wheelVertForce = m_wheelVertForce

    def pack(self):
        return struct.pack(
            format,
            self.m_suspensionPosition, 
            self.m_suspensionVelocity, 
            self.m_suspensionAcceleration,
            self.m_wheelSpeed, 
            self.m_wheelSlipRatio, 
            self.m_wheelSlipAngle,
            self.m_wheelLatForce, 
            self.m_wheelLongForce, 
            self.m_heightOfCOGAboveGround,
            self.m_localVelocityX, 
            self.m_localVelocityY, 
            self.m_localVelocityZ,
            self.m_angularVelocityX, 
            self.m_angularVelocityY, 
            self.m_angularVelocityZ,
            self.m_angularAccelerationX, 
            self.m_angularAccelerationY, 
            self.m_angularAccelerationZ, 
            self.m_frontWheelsAngle,
            self.m_wheelVertForce
        )
    
    @classmethod
    def unpack(cls, data):
        unpacked_data = struct.unpack(cls.format, data)
        return cls(*unpacked_data)