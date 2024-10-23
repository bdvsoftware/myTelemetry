import struct
from packet.packet_header import PacketHeader

class PacketMotionExData:

    format = '<4f4f4f4f4f4f4f4f11f4f'

    def __init__(self, 
                 m_header,
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
        self.m_header = m_header
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

    def pack (self):
        packed_header = self.m_header.pack()

        motion_ex_data = struct.pack(
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
        return packed_header+motion_ex_data
    
    @classmethod
    def unpack(cls, data):
        header_size = struct.calcsize(PacketHeader.format)
        header = PacketHeader.unpack(data[:header_size])
        motion_ex_data = struct.unpack_from('4f'  # m_suspensionPosition[4]
            '4f'  # m_suspensionVelocity[4]
            '4f'  # m_suspensionAcceleration[4]
            '4f'  # m_wheelSpeed[4]
            '4f'  # m_wheelSlipRatio[4]
            '4f'  # m_wheelSlipAngle[4]
            '4f'  # m_wheelLatForce[4]
            '4f'  # m_wheelLongForce[4]
            'f'   # m_heightOfCOGAboveGround
            'f'   # m_localVelocityX
            'f'   # m_localVelocityY
            'f'   # m_localVelocityZ
            'f'   # m_angularVelocityX
            'f'   # m_angularVelocityY
            'f'   # m_angularVelocityZ
            'f'   # m_angularAccelerationX
            'f'   # m_angularAccelerationY
            'f'   # m_angularAccelerationZ
            'f'   # m_frontWheelsAngle
            '4f'  # m_wheelVertForce[4]
            , data, header_size)
        return cls(
            header,
            motion_ex_data[:4],    # m_suspensionPosition[4]
            motion_ex_data[4:8],   # m_suspensionVelocity[4]
            motion_ex_data[8:12],  # m_suspensionAcceleration[4]
            motion_ex_data[12:16], # m_wheelSpeed[4]
            motion_ex_data[16:20], # m_wheelSlipRatio[4]
            motion_ex_data[20:24], # m_wheelSlipAngle[4]
            motion_ex_data[24:28], # m_wheelLatForce[4]
            motion_ex_data[28:32], # m_wheelLongForce[4]
            motion_ex_data[32],    # m_heightOfCOGAboveGround
            motion_ex_data[33],    # m_localVelocityX
            motion_ex_data[34],    # m_localVelocityY
            motion_ex_data[35],    # m_localVelocityZ
            motion_ex_data[36],    # m_angularVelocityX
            motion_ex_data[37],    # m_angularVelocityY
            motion_ex_data[38],    # m_angularVelocityZ
            motion_ex_data[39],    # m_angularAccelerationX
            motion_ex_data[40],    # m_angularAccelerationY
            motion_ex_data[41],    # m_angularAccelerationZ
            motion_ex_data[42],    # m_frontWheelsAngle
            motion_ex_data[43:47]
        )




