import struct

class CarStatusData:

    format = '<5B3f2H2BH3Bb3fB3fB'

    def __init__(self,
                 m_tractionControl,
                 m_antiLockBrakes,
                 m_fuelMix,
                 m_frontBrakeBias,
                 m_pitLimiterStatus,
                 m_fuelInTank,
                 m_fuelCapacity,
                 m_fuelRemainingLaps,
                 m_maxRPM,
                 m_idleRPM,
                 m_maxGears,
                 m_drsAllowed,
                 m_drsActivationDistance,
                 m_actualTyreCompound,
                 m_visualTyreCompound,
                 m_tyresAgeLaps,
                 m_vehicleFiaFlags,
                 m_enginePowerICE,
                 m_enginePowerMGUK,
                 m_ersStoreEnergy,
                 m_ersDeployMode,
                 m_ersHarvestedThisLapMGUK,
                 m_ersHarvestedThisLapMGUH,
                 m_ersDeployedThisLap,
                 m_networkPaused):
        self.m_tractionControl = m_tractionControl
        self.m_antiLockBrakes = m_antiLockBrakes
        self.m_fuelMix = m_fuelMix
        self.m_frontBrakeBias = m_frontBrakeBias
        self.m_pitLimiterStatus = m_pitLimiterStatus
        self.m_fuelInTank = m_fuelInTank
        self.m_fuelCapacity = m_fuelCapacity
        self.m_fuelRemainingLaps = m_fuelRemainingLaps
        self.m_maxRPM = m_maxRPM
        self.m_idleRPM = m_idleRPM
        self.m_maxGears = m_maxGears
        self.m_drsAllowed = m_drsAllowed
        self.m_drsActivationDistance = m_drsActivationDistance
        self.m_actualTyreCompound = m_actualTyreCompound
        self.m_visualTyreCompound = m_visualTyreCompound
        self.m_tyresAgeLaps = m_tyresAgeLaps
        self.m_vehicleFiaFlags = m_vehicleFiaFlags
        self.m_enginePowerICE = m_enginePowerICE
        self.m_enginePowerMGUK = m_enginePowerMGUK
        self.m_ersStoreEnergy = m_ersStoreEnergy
        self.m_ersDeployMode = m_ersDeployMode
        self.m_ersHarvestedThisLapMGUK = m_ersHarvestedThisLapMGUK
        self.m_ersHarvestedThisLapMGUH = m_ersHarvestedThisLapMGUH
        self.m_ersDeployedThisLap = m_ersDeployedThisLap
        self.m_networkPaused = m_networkPaused

    def pack(self):
        return struct.pack(
            self.format,
            self.m_tractionControl,
            self.antiLockBrakes,
            self.fuelMix,
            self.frontBrakeBias,
            self.pitLimiterStatus,
            self.fuelInTank,
            self.fuelCapacity,
            self.fuelRemainingLaps,
            self.maxRPM,
            self.idleRPM,
            self.maxGears,
            self.drsAllowed,
            self.drsActivationDistance,
            self.actualTyreCompound,
            self.visualTyreCompound,
            self.tyresAgeLaps,
            self.vehicleFiaFlags,
            self.enginePowerICE,
            self.enginePowerMGUK,
            self.ersStoreEnergy,
            self.ersDeployMode,
            self.ersHarvestedThisLapMGUK,
            self.ersHarvestedThisLapMGUH,
            self.ersDeployedThisLap,
            self.networkPaused
        )
    
    @classmethod
    def unpack(cls, data):
        unpackped_data = struct.unpack(cls.format, data)
        return cls(*unpackped_data)
    
    def to_json(self):
        return self.__dict__