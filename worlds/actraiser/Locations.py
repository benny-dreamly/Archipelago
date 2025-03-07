from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Location, MultiWorld


class ActraiserLocation(Location):
    game = "Actraiser"


class ActraiserLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True
    locked_item: Optional[str] = None

location_data_table: Dict[str, ActraiserLocationData] = {
    "FMF - Centaur": ActraiserLocationData(
        region="Fillmore Forest",
        address=0x1C1000
    ),
    "FMC - Minotaurus": ActraiserLocationData(
        region="Fillmore Chasm",
        address=0x1C1001
    ),
    "BPB - Manticore": ActraiserLocationData(
        region="Bloodpool Bridge",
        address=0x1C1002
    ),
    "BPC - Zeppelin Wolf": ActraiserLocationData(
        region="Bloodpool Castle",
        address=0x1C1003
    ),
    "KDD - Dagoba": ActraiserLocationData(
        region="Kasandora Desert",
        address=0x1C1004
    ),
    "KDP - Pharaoh": ActraiserLocationData(
        region="Kasandora Pyramid",
        address=0x1C1005
    ),
    "ATM - Serpent": ActraiserLocationData(
        region="Aitos Mountain",
        address=0x1C1006
    ),
    "ATV - Fire Wheel": ActraiserLocationData(
        region="Aitos Volcano",
        address=0x1C1007
    ),
    "MHS - Rafflasher": ActraiserLocationData(
        region="Marahna Swamp",
        address=0x1C1008
    ),
    "MHT - Kalia": ActraiserLocationData(
        region="Marahna Temple",
        address=0x1C1009
    ),
    "NWC - Merman Fly": ActraiserLocationData(
        region="Northwall Cave",
        address=0x1C100A
    ),
    "NWT - Arctic Wyvern": ActraiserLocationData(
        region="Northwall Tree",
        address=0x1C100B
    ),


    "FM - Advancement 1": ActraiserLocationData(
        region="Fillmore",
        address=0x1C1010
    ),
    "FM - Advancement 2": ActraiserLocationData(
        region="Fillmore",
        address=0x1C1011
    ),
    "BP - Advancement 1": ActraiserLocationData(
        region="Bloodpool",
        address=0x1C1012
    ),
    "BP - Advancement 2": ActraiserLocationData(
        region="Bloodpool",
        address=0x1C1013
    ),
    "KD - Advancement 1": ActraiserLocationData(
        region="Kasandora",
        address=0x1C1014
    ),
    "KD - Advancement 2": ActraiserLocationData(
        region="Kasandora",
        address=0x1C1015
    ),
    "AT - Advancement 1": ActraiserLocationData(
        region="Aitos",
        address=0x1C1016
    ),
    "AT - Advancement 2": ActraiserLocationData(
        region="Aitos",
        address=0x1C1017
    ),
    "MH - Advancement 1": ActraiserLocationData(
        region="Marahna",
        address=0x1C1018
    ),
    "MH - Advancement 2": ActraiserLocationData(
        region="Marahna",
        address=0x1C1019
    ),
    "NW - Advancement 1": ActraiserLocationData(
        region="Northwall",
        address=0x1C101A
    ),
    "NW - Advancement 2": ActraiserLocationData(
        region="Northwall",
        address=0x1C101B
    ),

    #"BP - Calmed Citizens": ActraiserLocationData(
    #    region="Bloodpool",
    #    address=0x1C101D
    #),
    "KD - Cured Plague": ActraiserLocationData(
        region="Kasandora",
        address=0x1C101C
    ),
    "NW - Warm Clothes": ActraiserLocationData(
        region="Northwall",
        address=0x1C101E
    ),

    "FM - Max Population": ActraiserLocationData(
        region="Fillmore",
        address=0x1C101F
    ),
    "BP - Max Population": ActraiserLocationData(
        region="Bloodpool",
        address=0x1C1020
    ),
    "KD - Max Population": ActraiserLocationData(
        region="Kasandora",
        address=0x1C1021
    ),
    "AT - Max Population": ActraiserLocationData(
        region="Aitos",
        address=0x1C1022
    ),
    "MH - Max Population": ActraiserLocationData(
        region="Marahna",
        address=0x1C1023
    ),
    "NW - Max Population": ActraiserLocationData(
        region="Northwall",
        address=0x1C1024
    ),

    "FM - Population 64": ActraiserLocationData(
        region="Fillmore",
        address=0x1C1025
    ),
    "FM - Population 128": ActraiserLocationData(
        region="Fillmore",
        address=0x1C1026
    ),
    "FM - Population 256": ActraiserLocationData(
        region="Fillmore",
        address=0x1C1027
    ),
    "FM - Population 512": ActraiserLocationData(
        region="Fillmore",
        address=0x1C1028
    ),

    "BP - Population 64": ActraiserLocationData(
        region="Bloodpool",
        address=0x1C1029
    ),
    "BP - Population 128": ActraiserLocationData(
        region="Bloodpool",
        address=0x1C102A
    ),
    "BP - Population 256": ActraiserLocationData(
        region="Bloodpool",
        address=0x1C102B
    ),
    "BP - Population 512": ActraiserLocationData(
        region="Bloodpool",
        address=0x1C102C
    ),

    "KD - Population 64": ActraiserLocationData(
        region="Kasandora",
        address=0x1C102D
    ),
    "KD - Population 128": ActraiserLocationData(
        region="Kasandora",
        address=0x1C102E
    ),
    "KD - Population 256": ActraiserLocationData(
        region="Kasandora",
        address=0x1C102F
    ),
    "KD - Population 512": ActraiserLocationData(
        region="Kasandora",
        address=0x1C1030
    ),

    "AT - Population 64": ActraiserLocationData(
        region="Aitos",
        address=0x1C1031
    ),
    "AT - Population 128": ActraiserLocationData(
        region="Aitos",
        address=0x1C1032
    ),
    "AT - Population 256": ActraiserLocationData(
        region="Aitos",
        address=0x1C1033
    ),
    "AT - Population 512": ActraiserLocationData(
        region="Aitos",
        address=0x1C1034
    ),

    "MH - Population 64": ActraiserLocationData(
        region="Marahna",
        address=0x1C1035
    ),
    "MH - Population 128": ActraiserLocationData(
        region="Marahna",
        address=0x1C1036
    ),
    "MH - Population 256": ActraiserLocationData(
        region="Marahna",
        address=0x1C1037
    ),
   # "MH - Population 512": ActraiserLocationData(
    #    region="Marahna",
   #     address=0x1C1038
   # ),

    "NW - Population 64": ActraiserLocationData(
        region="Northwall",
        address=0x1C1039
    ),
    "NW - Population 128": ActraiserLocationData(
        region="Northwall",
        address=0x1C103A
    ),
    "NW - Population 256": ActraiserLocationData(
        region="Northwall",
        address=0x1C103B
    ),
    "NW - Population 512": ActraiserLocationData(
        region="Northwall",
        address=0x1C103C
    ),

    "SK - Level 2": ActraiserLocationData(
        region="Sky",
        address=0x1C103D
    ),
    "SK - Level 3": ActraiserLocationData(
        region="Sky",
        address=0x1C103E
    ),
    "SK - Level 4": ActraiserLocationData(
        region="Sky",
        address=0x1C103f
    ),
    "SK - Level 5": ActraiserLocationData(
        region="Sky",
        address=0x1C1040
    ),
    "SK - Level 6": ActraiserLocationData(
        region="Sky",
        address=0x1C1041
    ),
    "SK - Level 7": ActraiserLocationData(
        region="Sky",
        address=0x1C1042
    ),
    "SK - Level 8": ActraiserLocationData(
        region="Sky",
        address=0x1C1043
    ),
    "SK - Level 9": ActraiserLocationData(
        region="Sky",
        address=0x1C1044
    ),
    "SK - Level 10": ActraiserLocationData(
        region="Sky",
        address=0x1C1045
    ),
    "SK - Level 11": ActraiserLocationData(
        region="Sky",
        address=0x1C1046
    ),
    "SK - Level 12": ActraiserLocationData(
        region="Sky",
        address=0x1C1047
    ),
    "SK - Level 13": ActraiserLocationData(
        region="Sky",
        address=0x1C1048
    ),
    "SK - Level 14": ActraiserLocationData(
        region="Sky",
        address=0x1C1049
    ),
    "SK - Level 15": ActraiserLocationData(
        region="Sky",
        address=0x1C104A
    ),
    "SK - Level 16": ActraiserLocationData(
        region="Sky",
        address=0x1C104B
    ),
    "SK - Level 17": ActraiserLocationData(
        region="Sky",
        address=0x1C104C
    ),

    "FM - Magical Fire": ActraiserLocationData(
        region="Fillmore",
        address=0x1C1050
    ),
    "BP - Magical Stardust": ActraiserLocationData(
        region="Bloodpool",
        address=0x1C1051
    ),
    "MH - Magical Aura": ActraiserLocationData(
        region="Marahna",
        address=0x1C1052
    ),
    "NW - Magical Light": ActraiserLocationData(
        region="Northwall",
        address=0x1C1053
    ),

    "BP - Bread": ActraiserLocationData(
        region="Bloodpool",
        address=0x1C1054
    ),
    "BP - Wheat": ActraiserLocationData(
        region="Bloodpool",
        address=0x1C1055
    ),
    "MH - Herb": ActraiserLocationData(
        region="Marahna",
        address=0x1C1056
    ),
    "FM - Bridge": ActraiserLocationData(
        region="Fillmore",
        address=0x1C1057
    ),
    "KD - Music": ActraiserLocationData(
        region="Kasandora",
        address=0x1C1058
    ),
    "KD - Ancient Tablet": ActraiserLocationData(
        region="Kasandora",
        address=0x1C1059
    ),
    "BP - Magic Skull": ActraiserLocationData(
        region="Bloodpool",
        address=0x1C105A
    ),
    "AT - Fleece": ActraiserLocationData(
        region="Aitos",
        address=0x1C105B
    ),
    "BP - Compass": ActraiserLocationData(
        region="Bloodpool",
        address=0x1C105C
    ),

    "FM - Bomb": ActraiserLocationData(
        region="Fillmore",
        address=0x1C1060
    ),
    "FM - Strength of Angel": ActraiserLocationData(
        region="Fillmore",
        address=0x1C1061
    ),
    "FM - Source of Magic": ActraiserLocationData(
        region="Fillmore",
        address=0x1C1062
    ),
    "FM - Source of Life": ActraiserLocationData(
        region="Fillmore",
        address=0x1C1063
    ),

    "BP - Bomb": ActraiserLocationData(
        region="Bloodpool",
        address=0x1C1064
    ),
    "BP - Source of Life": ActraiserLocationData(
        region="Bloodpool",
        address=0x1C1065
    ),
    "BP - Source of Magic": ActraiserLocationData(
        region="Bloodpool",
        address=0x1C1066
    ),

    "KD - Strength of Angel": ActraiserLocationData(
        region="Kasandora",
        address=0x1C1067
    ),
    "KD - Bomb": ActraiserLocationData(
        region="Kasandora",
        address=0x1C1068
    ),
    "KD - Source of Magic": ActraiserLocationData(
        region="Kasandora",
        address=0x1C1069
    ),
    "KD - Source of Life": ActraiserLocationData(
        region="Kasandora",
        address=0x1C106A
    ),

    "AT - Bomb": ActraiserLocationData(
        region="Aitos",
        address=0x1C106B
    ),
    "AT - Strength of Angel": ActraiserLocationData(
        region="Aitos",
        address=0x1C106C
    ),
    "AT - Source of Magic": ActraiserLocationData(
        region="Aitos",
        address=0x1C106D
    ),

    "MH - Strength of Angel": ActraiserLocationData(
        region="Marahna",
        address=0x1C106E
    ),
    "MH - Bomb": ActraiserLocationData(
        region="Marahna",
        address=0x1C106F
    ),
    "MH - Source of Magic": ActraiserLocationData(
        region="Marahna",
        address=0x1C1074
    ),

    "NW - Strength of Angel": ActraiserLocationData(
        region="Northwall",
        address=0x1C1070
    ),
    "NW - Bomb": ActraiserLocationData(
        region="Northwall",
        address=0x1C1071
    ),
    "NW - Source of Magic": ActraiserLocationData(
        region="Northwall",
        address=0x1C1072
    ),
    "NW - Source of Life": ActraiserLocationData(
        region="Northwall",
        address=0x1C1073
    ),



    "FMF - Tree Near Entrance": ActraiserLocationData(
        region="Fillmore Forest",
        address=0x1C1080
    ),
    "FMF - Tree From Ropeway": ActraiserLocationData(
        region="Fillmore Forest",
        address=0x1C1081
    ),
    "FMF - Top and Center": ActraiserLocationData(
        region="Fillmore Forest",
        address=0x1C1082
    ),
    "FMF - Spiky Plants": ActraiserLocationData(
        region="Fillmore Forest",
        address=0x1C1083
    ),
    "FMF - Tree Near Centaur": ActraiserLocationData(
        region="Fillmore Forest",
        address=0x1C1084
    ),

    "FMC - Lower Right Of Waterfall": ActraiserLocationData(
        region="Fillmore Chasm",
        address=0x1C1085
    ),
    "FMC - Bone Pile": ActraiserLocationData(
        region="Fillmore Chasm",
        address=0x1C1086
    ),
    "FMC - Left Of Column": ActraiserLocationData(
        region="Fillmore Chasm",
        address=0x1C1087
    ),
    "FMC - Right Of Column": ActraiserLocationData(
        region="Fillmore Chasm",
        address=0x1C1088
    ),
    "FMC - Left Of Waterfall": ActraiserLocationData(
        region="Fillmore Chasm",
        address=0x1C1089
    ),
    "FMC - Tunnel": ActraiserLocationData(
        region="Fillmore Chasm",
        address=0x1C108A
    ),
    "FMC - S-Shaped Tunnel": ActraiserLocationData(
        region="Fillmore Chasm",
        address=0x1C108B
    ),
    "FMC - Falling Spikes": ActraiserLocationData(
        region="Fillmore Chasm",
        address=0x1C108C
    ),

    "BPB - Platform Near Entrance": ActraiserLocationData(
        region="Bloodpool Bridge",
        address=0x1C108D
    ),
    "BPB - Center Bridge": ActraiserLocationData(
        region="Bloodpool Bridge",
        address=0x1C108E
    ),
    "BPB - Falling Bridge": ActraiserLocationData(
        region="Bloodpool Bridge",
        address=0x1C108F
    ),
    "BPB - Platform Near Manitcore": ActraiserLocationData(
        region="Bloodpool Bridge",
        address=0x1C1090
    ),

    "BPC - Left Elevator": ActraiserLocationData(
        region="Bloodpool Castle",
        address=0x1C1091
    ),
    "BPC - Dark Room": ActraiserLocationData(
        region="Bloodpool Castle",
        address=0x1C1092
    ),
    "BPC - Moat": ActraiserLocationData(
        region="Bloodpool Castle",
        address=0x1C1093
    ),
    "BPC - Right Elevator": ActraiserLocationData(
        region="Bloodpool Castle",
        address=0x1C1094
    ),
    "BPC - Stone Ledges": ActraiserLocationData(
        region="Bloodpool Castle",
        address=0x1C1095
    ),

    "KDD - Rock Spires": ActraiserLocationData(
        region="Kasandora Desert",
        address=0x1C1096
    ),
    "KDD - Top of Left Tower": ActraiserLocationData(
        region="Kasandora Desert",
        address=0x1C1097
    ),
    "KDD - Top of Right Tower": ActraiserLocationData(
        region="Kasandora Desert",
        address=0x1C1098
    ),
    "KDD - Below Towers": ActraiserLocationData(
        region="Kasandora Desert",
        address=0x1C1099
    ),
    "KDD - Rocks Near Dagoba": ActraiserLocationData(
        region="Kasandora Desert",
        address=0x1C109A
    ),

    "KDP - Statue Room Center Platform": ActraiserLocationData(
        region="Kasandora Pyramid",
        address=0x1C109B
    ),
    "KDP - Statue Room High Ledge": ActraiserLocationData(
        region="Kasandora Pyramid",
        address=0x1C109C
    ),
    "KDP - Ledge With Scorman": ActraiserLocationData(
        region="Kasandora Pyramid",
        address=0x1C109D
    ),
    "KDP - Red Bird God": ActraiserLocationData(
        region="Kasandora Pyramid",
        address=0x1C109E
    ),

    "ATM - Between Lava Pits": ActraiserLocationData(
        region="Aitos Mountain",
        address=0x1C109F
    ),
    "ATM - Pass to Crater": ActraiserLocationData(
        region="Aitos Mountain",
        address=0x1C10A0
    ),
    "ATM - Bottom Of Crater": ActraiserLocationData(
        region="Aitos Mountain",
        address=0x1C10A1
    ),
    "ATM - Waterfall Left": ActraiserLocationData(
        region="Aitos Mountain",
        address=0x1C10A2
    ),
    "ATM - Waterfall Center": ActraiserLocationData(
        region="Aitos Mountain",
        address=0x1C10A3
    ),
    "ATM - Waterfall Right": ActraiserLocationData(
        region="Aitos Mountain",
        address=0x1C10A4
    ),

    "ATV - Dragon Mouths": ActraiserLocationData(
        region="Aitos Volcano",
        address=0x1C10A5
    ),
    "ATV - Near Flame Wheel": ActraiserLocationData(
        region="Aitos Volcano",
        address=0x1C10A6
    ),

    "MHS - Ruins Left": ActraiserLocationData(
        region="Marahna Swamp",
        address=0x1C10A7
    ),
    "MHS - Ruins Right": ActraiserLocationData(
        region="Marahna Swamp",
        address=0x1C10A8
    ),
    "MHS - Hut": ActraiserLocationData(
        region="Marahna Swamp",
        address=0x1C10A9
    ),
    "MHS - Pillars": ActraiserLocationData(
        region="Marahna Swamp",
        address=0x1C10AA
    ),

    "MHT - Falling Platforms": ActraiserLocationData(
        region="Marahna Temple",
        address=0x1C10AB
    ),
    "MHT - Left Path Ledge": ActraiserLocationData(
        region="Marahna Temple",
        address=0x1C10AC
    ),
    "MHT - Right Path Between Spikes": ActraiserLocationData(
        region="Marahna Temple",
        address=0x1C10AD
    ),
    "MHT - Hidden Pillar": ActraiserLocationData(
        region="Marahna Temple",
        address=0x1C10C3
    ),
    
    "NWC - Outside Between Spikes": ActraiserLocationData(
        region="Northwall Cave",
        address=0x1C10AE
    ),
    "NWC - Right Cliff Near Cave Entrance": ActraiserLocationData(
        region="Northwall Cave",
        address=0x1C10AF
    ),
    "NWC - River Platform": ActraiserLocationData(
        region="Northwall Cave",
        address=0x1C10B0
    ),
    "NWC - Subterranean River": ActraiserLocationData(
        region="Northwall Cave",
        address=0x1C10B1
    ),
    "NWC - Hidden Passage Pillars": ActraiserLocationData(
        region="Northwall Cave",
        address=0x1C10B2
    ),
    "NWC - Hidden Passage Wall": ActraiserLocationData(
        region="Northwall Cave",
        address=0x1C10B3
    ),
    "NWC - Icy Platoforms": ActraiserLocationData(
        region="Northwall Cave",
        address=0x1C10B4
    ),
    "NWC - Eyeball Platform": ActraiserLocationData(
        region="Northwall Cave",
        address=0x1C10B5
    ),
    "NWC - Snowman Shaft": ActraiserLocationData(
        region="Northwall Cave",
        address=0x1C10B6
    ),
    "NWC - Left Ledge Near Merman Fly": ActraiserLocationData(
        region="Northwall Cave",
        address=0x1C10B7
    ),

    "NWT - Trunk Neighboring Tree": ActraiserLocationData(
        region="Northwall Tree",
        address=0x1C10B8
    ),
    "NWT - Trunk Left Side": ActraiserLocationData(
        region="Northwall Tree",
        address=0x1C10B9
    ),
    "NWT - Trunk Right Side": ActraiserLocationData(
        region="Northwall Tree",
        address=0x1C10BA
    ),
    "NWT - Root": ActraiserLocationData(
        region="Northwall Tree",
        address=0x1C10BB
    ),
    "NWT - Right Second Branch": ActraiserLocationData(
        region="Northwall Tree",
        address=0x1C10BC
    ),
    "NWT - Left Second Branch": ActraiserLocationData(
        region="Northwall Tree",
        address=0x1C10BD
    ),
    "NWT - Right Atop Third Branch": ActraiserLocationData(
        region="Northwall Tree",
        address=0x1C10BE
    ),
    "NWT - Right Atop Fourth Branch": ActraiserLocationData(
        region="Northwall Tree",
        address=0x1C10BF
    ),
    "NWT - Top Of Tree Shaft": ActraiserLocationData(
        region="Northwall Tree",
        address=0x1C10C0
    ),
    "NWT - Right Treeside Third Branch": ActraiserLocationData(
        region="Northwall Tree",
        address=0x1C10C1
    ),
    "NWT - Trunk Center": ActraiserLocationData(
        region="Northwall Tree",
        address=0x1C10C2
    ),
    

    "Tanzra Dead": ActraiserLocationData(
        address=0x1C100C,
        region="Death Heim",
        locked_item="Savior"
    ),
    "Population Goal": ActraiserLocationData(
        address=0x1C100D,
        region="Sky",
        locked_item="Prosperity"
    ),
}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}
