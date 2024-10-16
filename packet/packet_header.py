import struct
import json

class PacketHeader:

    format = '<HBBBBBQfII2B'

    def __init__(self, m_packetFormat, m_gameYear, m_gameMajorVersion, m_gameMinorVersion, 
                 m_packetVersion, m_packetId, m_sessionUID, m_sessionTime, 
                 m_frameIdentifier, m_overallFrameIdentifier, m_playerCarIndex, 
                 m_secondaryPlayerCarIndex):
        self.m_packetFormat = m_packetFormat
        self.m_gameYear = m_gameYear
        self.m_gameMajorVersion = m_gameMajorVersion
        self.m_gameMinorVersion = m_gameMinorVersion
        self.m_packetVersion = m_packetVersion
        self.m_packetId = m_packetId
        self.m_sessionUID = m_sessionUID
        self.m_sessionTime = m_sessionTime
        self.m_frameIdentifier = m_frameIdentifier
        self.m_overallFrameIdentifier = m_overallFrameIdentifier
        self.m_playerCarIndex = m_playerCarIndex
        self.m_secondaryPlayerCarIndex = m_secondaryPlayerCarIndex

    def pack(self):
        return struct.pack(self.format, 
                           self.m_packetFormat,
                           self.m_gameYear,
                           self.m_gameMajorVersion,
                           self.m_gameMinorVersion,
                           self.m_packetVersion,
                           self.m_packetId,
                           self.m_sessionUID,
                           self.m_sessionTime,
                           self.m_frameIdentifier,
                           self.m_overallFrameIdentifier,
                           self.m_playerCarIndex,
                           self.m_secondaryPlayerCarIndex)

    @classmethod
    def unpack(cls, data):
        unpacked_data = struct.unpack(cls.format, data)
        return cls(*unpacked_data)
    
    def to_json(self):
        return {
        'm_packetFormat': self.m_packetFormat,
        'm_gameYear': self.m_gameYear,
        'm_gameMajorVersion': self.m_gameMajorVersion,
        'm_gameMinorVersion': self.m_gameMinorVersion,
        'm_packetVersion': self.m_packetVersion,
        'm_packetId': self.m_packetId,
        'm_sessionUID': self.m_sessionUID,
        'm_sessionTime': self.m_sessionTime,
        'm_frameIdentifier': self.m_frameIdentifier,
        'm_overallFrameIdentifier': self.m_overallFrameIdentifier,
        'm_playerCarIndex': self.m_playerCarIndex,
        'm_secondaryPlayerCarIndex': self.m_secondaryPlayerCarIndex
    }

