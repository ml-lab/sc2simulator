
"""
This hard-coded list would need to be maintained differently if/when the
available units, available upgrades or their in-game IDs change.
"""

codeMap = {
    "protoss"   : {
        "ground" : {
                    4  , # Colossus
                    73 , # Zealot
                    74 , # Stalker
                    75 , # HighTemplar
                    76 , # DarkTemplar
                    77 , # Sentry
                    83 , # Immortal
                    84 , # Probe
                    694, # Disruptor
                    311, # Adept
        },
        "air" : {
                    78 , # Phoenix
                    79 , # Carrier
                    80 , # VoidRay
                    81 , # WarpPrism
                    495, # Oracle
                    496, # Tempest
        },
        "defense" : {
                    66 , # PhotonCannon
                    1910,# ShieldBattery
        },
        "detection" : {
                    82 , # Observer
        },
        "upgrades" : {
                    4  , # CarrierLaunchSpeedUpgrade
                    42 , # ProtossGroundWeaponsLevel1
                    43 , # ProtossGroundWeaponsLevel2
                    44 , # ProtossGroundWeaponsLevel3
                    45 , # ProtossGroundArmorsLevel1
                    46 , # ProtossGroundArmorsLevel2
                    47 , # ProtossGroundArmorsLevel3
                    48 , # ProtossShieldsLevel1
                    49 , # ProtossShieldsLevel2
                    50 , # ProtossShieldsLevel3
                    51 , # ObserverGraviticBooster
                    52 , # GraviticDrive
                    53 , # ExtendedThermalLance
                    55 , # PsiStormTech
                    87 , # WarpGateResearch
                    90 , # BlinkTech
                    89 , # Charge
                    81 , # ProtossAirWeaponsLevel1
                    82 , # ProtossAirWeaponsLevel2
                    83 , # ProtossAirWeaponsLevel3
                    84 , # ProtossAirArmorsLevel1
                    85 , # ProtossAirArmorsLevel2
                    86 , # ProtossAirArmorsLevel3
                    148, # PhoneixRangeUpgrade
                    181, # AdeptPiercingAttack
                    198, # DarkTemplarBlinkUpgrade
        },
    },
    "terran"    : {
        "ground" : {
                    33 , # SiegeTank
                    45 , # SCV
                    48 , # Marine
                    49 , # Reaper
                    50 , # Ghost
                    51 , # Marauder
                    52 , # Thor
                    53 , # Hellion
                    498, # WidowMine
                    692, # Cyclone
        },
        "air" : {
                    35 , # VikingFighter
                    54 , # Medivac
                    55 , # Banshee
                    57 , # Battlecruiser
                    689, # Liberator
        },
        "defense" : {
                    23 , # MissileTurret
                    24 , # Bunker
                    25 , # SensorTower
        },
        "detection": {
                    56 , # Raven
        },
        "upgrades" : {
                    8  , # HiSecAutoTracking
                    9  , # TerranBuildingArmor
                    10 , # TerranInfantryWeaponsLevel1
                    11 , # TerranInfantryWeaponsLevel2
                    12 , # TerranInfantryWeaponsLevel3
                    13 , # NeosteelFrame
                    14 , # TerranInfantryArmorsLevel1
                    15 , # TerranInfantryArmorsLevel2
                    16 , # TerranInfantryArmorsLevel3
                    18 , # Stimpack
                    19 , # CombatShields
                    20 , # PunisherGrenades
                    22 , # HighCapacityBarrels
                    23 , # BansheeCloak
                    25 , # RavenCorvidReactor
                    28 , # PersonalCloaking
                    33 , # TerranVehicleWeaponsLevel1
                    34 , # TerranVehicleWeaponsLevel2
                    35 , # TerranVehicleWeaponsLevel3
                    39 , # TerranShipWeaponsLevel1
                    40 , # TerranShipWeaponsLevel2
                    41 , # TerranShipWeaponsLevel3
                    79 , # BattlecruiserEnableSpecializations
                    162, # TerranVehicleAndShipArmorsLevel1
                    163, # TerranVehicleAndShipArmorsLevel2
                    164, # TerranVehicleAndShipArmorsLevel3
                    168, # DrillClaws
                    187, # SmartServos
                    189, # CycloneRapidFireLaunchers
                    192, # BansheeSpeed
                    195, # MedivacIncreaseSpeedBoost
                    196, # LiberatorAGRangeUpgrade
        },
    },
    "zerg"      : {
        "ground" : {
                    9  , # Baneling
                    104, # Drone
                    105, # Zergling
                    107, # Hydralisk
                    109, # Ultralisk
                    110, # Roach
                    111, # Infestor
                    126, # Queen
                    494, # SwarmHostMP
                    502, # LurkerMP
                   #898 # InfestedTerran
        },
        "air" : {
                    106, # Overlord
                    108, # Mutalisk
                    112, # Corruptor
                    114, # BroodLord
                    499, # Viper
                    893, # OverlordTransport
        },
        "defense" : {
                    98 , # SpineCrawler
                    99 , # SporeCrawler
        },
        "detection": {
                    129, # Overseer
        },
        "upgrades" : {
                    5  , # GlialReconstitution
                    6  , # TunnelingClaws
                    7  , # ChitinousPlating
                    56 , # ZergMeleeWeaponsLevel1
                    57 , # ZergMeleeWeaponsLevel2
                    58 , # ZergMeleeWeaponsLevel3
                    59 , # ZergGroundArmorsLevel1
                    60 , # ZergGroundArmorsLevel2
                    61 , # ZergGroundArmorsLevel3
                    62 , # ZergMissleWeaponsLevel
                    63 , # ZergMissleWeaponsLeve2
                    64 , # ZergMissleWeaponsLeve3
                    65 , # overlordsepeed
                    67 , # Burrow
                    68 , # zerglingattackspeed
                    69 , # zerglingmovementspeed
                    71 , # ZergFlyerWeaponsLevel1
                    72 , # ZergFlyerWeaponsLevel2
                    73 , # ZergFlyerWeaponsLevel3
                    74 , # ZergFlyerArmorsLevel1
                    75 , # ZergFlyerArmorsLevel2
                    76 , # ZergFlyerArmorsLevel3
                    77 , # InfestorEnergyUpgrade
                    78 , # CentrificalHooks
                    150, # NeuralParasite
                    199, # DiggingClaws
                    190, # EvolveGroovedSpines
                    191, # EvolveMuscularAguments
        },
    }
}
