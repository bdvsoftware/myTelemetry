import struct
import json
import math

class LapData:
    format = '<2I2H2B2H3f9B4H2B'

    def __init__(self, m_lastLapTimeInMS, m_currentLapTimeInMS, m_sector1TimeInMS,
                 m_sector1TimeMinutes, m_sector2TimeInMS, m_sector2TimeMinutes,
                 m_deltaToCarInFrontInMS, m_deltaToRaceLeaderInMS, m_lapDistance,
                 m_totalDistance, m_safetyCarDelta, m_carPosition, m_currentLapNum,
                 m_pitStatus, m_numPitStops, m_sector, m_currentLapInvalid, m_penalties,
                 m_totalWarnings, m_cornerCuttingWarnings, m_numUnservedDriveThroughPens,
                 m_numUnservedStopGoPens, m_gridPosition, m_driverStatus, m_resultStatus,
                 m_pitLaneTimerActive):  
        self.m_lastLapTimeInMS = m_lastLapTimeInMS
        self.m_currentLapTimeInMS = m_currentLapTimeInMS
        self.m_sector1TimeInMS = m_sector1TimeInMS
        self.m_sector1TimeMinutes = m_sector1TimeMinutes
        self.m_sector2TimeInMS = m_sector2TimeInMS
        self.m_sector2TimeMinutes = m_sector2TimeMinutes
        self.m_deltaToCarInFrontInMS = m_deltaToCarInFrontInMS
        self.m_deltaToRaceLeaderInMS = m_deltaToRaceLeaderInMS
        self.m_lapDistance = m_lapDistance
        self.m_totalDistance = m_totalDistance
        self.m_safetyCarDelta = m_safetyCarDelta
        self.m_carPosition = m_carPosition
        self.m_currentLapNum = m_currentLapNum
        self.m_pitStatus = m_pitStatus
        self.m_numPitStops = m_numPitStops
        self.m_sector = m_sector
        self.m_currentLapInvalid = m_currentLapInvalid
        self.m_penalties = m_penalties
        self.m_totalWarnings = m_totalWarnings
        self.m_cornerCuttingWarnings = m_cornerCuttingWarnings
        self.m_numUnservedDriveThroughPens = m_numUnservedDriveThroughPens
        self.m_numUnservedStopGoPens = m_numUnservedStopGoPens
        self.m_gridPosition = m_gridPosition
        self.m_driverStatus = m_driverStatus
        self.m_resultStatus = m_resultStatus
        self.m_pitLaneTimerActive = m_pitLaneTimerActive

    def pack(self):
        return struct.pack(self.format,
                           self.m_lastLapTimeInMS,
                           self.m_currentLapTimeInMS,
                           self.m_sector1TimeInMS,
                           self.m_sector1TimeMinutes,
                           self.m_sector2TimeInMS,
                           self.m_sector2TimeMinutes,
                           self.m_deltaToCarInFrontInMS,
                           self.m_deltaToRaceLeaderInMS,
                           self.m_lapDistance,
                           self.m_totalDistance,
                           self.m_safetyCarDelta,
                           self.m_carPosition,
                           self.m_currentLapNum,
                           self.m_pitStatus,
                           self.m_numPitStops,
                           self.m_sector,
                           self.m_currentLapInvalid,
                           self.m_penalties,
                           self.m_totalWarnings,
                           self.m_cornerCuttingWarnings,
                           self.m_numUnservedDriveThroughPens,
                           self.m_numUnservedStopGoPens,
                           self.m_gridPosition,
                           self.m_driverStatus,
                           self.m_resultStatus,
                           self.m_pitLaneTimerActive,
                           None,
                           None,
                           None)

    @classmethod
    def unpack(cls, data):
        unpacked_data = struct.unpack(cls.format, data)
        return cls(*unpacked_data)
    
    def to_json(self):
        return {
            'm_lastLapTimeInMS': self.m_lastLapTimeInMS,
            'm_currentLapTimeInMS': self.m_currentLapTimeInMS,
            'm_sector1TimeInMS': self.m_sector1TimeInMS,
            'm_sector1TimeMinutes': self.m_sector1TimeMinutes,
            'm_sector2TimeInMS': self.m_sector2TimeInMS,
            'm_sector2TimeMinutes': self.m_sector2TimeMinutes,
            'm_deltaToCarInFrontInMS': self.m_deltaToCarInFrontInMS,
            'm_deltaToRaceLeaderInMS': self.m_deltaToRaceLeaderInMS,
            'm_lapDistance': None if isinstance(self.m_lapDistance, float) and math.isnan(self.m_lapDistance) else self.m_lapDistance,
            'm_totalDistance': None if isinstance(self.m_totalDistance, float) and math.isnan(self.m_totalDistance) else self.m_totalDistance,
            'm_safetyCarDelta': None if isinstance(self.m_safetyCarDelta, float) and math.isnan(self.m_safetyCarDelta) else self.m_safetyCarDelta,
            'm_carPosition': self.m_carPosition,
            'm_currentLapNum': self.m_currentLapNum,
            'm_pitStatus': self.m_pitStatus,
            'm_numPitStops': self.m_numPitStops,
            'm_sector': self.m_sector,
            'm_currentLapInvalid': self.m_currentLapInvalid,
            'm_penalties': self.m_penalties,
            'm_totalWarnings': self.m_totalWarnings,
            'm_cornerCuttingWarnings': self.m_cornerCuttingWarnings,
            'm_numUnservedDriveThroughPens': self.m_numUnservedDriveThroughPens,
            'm_numUnservedStopGoPens': self.m_numUnservedStopGoPens,
            'm_gridPosition': self.m_gridPosition,
            'm_driverStatus': self.m_driverStatus,
            'm_resultStatus': self.m_resultStatus,
            'm_pitLaneTimerActive': self.m_pitLaneTimerActive
        }
