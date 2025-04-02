from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Location, MultiWorld


class PlokLocation(Location):
    game = "Plok"


class PlokLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True
    locked_item: Optional[str] = None

location_data_table: Dict[str, PlokLocationData] = {
    # Stage Clears
    "CI - Beach Clear": PlokLocationData(
        region="Cotton Island",
        address=0x1C0000
    ),
    "CI - Bridge Clear": PlokLocationData(
        region="Cotton Island",
        address=0x1C0001
    ),
    "CI - Columns Clear": PlokLocationData(
        region="Cotton Island",
        address=0x1C0002
    ),
    "CI - Log Falls Clear": PlokLocationData(
        region="Cotton Island",
        address=0x1C0003
    ),
    "CI - Rickety Bridge Clear": PlokLocationData(
        region="Cotton Island",
        address=0x1C0004
    ),
    "CI - Crazy Cradles Clear": PlokLocationData(
        region="Cotton Island",
        address=0x1C0005
    ),
    "CI - Blind Leap Clear": PlokLocationData(
        region="Cotton Island",
        address=0x1C0006
    ),
    "CI - Bobbin Bros Clear": PlokLocationData(
        region="Cotton Island",
        address=0x1C0007
    ),

    "AK - Garlen Beach Clear": PlokLocationData(
        region="Garlen Beach",
        address=0x1C0008
    ),
    "AK - Sleepy Dale Clear": PlokLocationData(
        region="Sleepy Dale",
        address=0x1C0009
    ),
    #"AK - Ploks House": PlokLocationData(
    #    region="Akrillic",
    #    address=0x1C000A
    #),
    "LI - Mace Cove Clear": PlokLocationData(
        region="Legacy Island",
        address=0x1C000B
    ),
    "LI - Fools Gap Clear": PlokLocationData(
        region="Legacy Island",
        address=0x1C000C
    ),
    "LI - Zig Zag Clear": PlokLocationData(
        region="Legacy Island",
        address=0x1C000D
    ),
    "LI - Sponge Rock Clear": PlokLocationData(
        region="Legacy Island",
        address=0x1C000E
    ),
    "LI - Swifty Peaks Clear": PlokLocationData(
        region="Legacy Island",
        address=0x1C000F
    ),

    "LI - Log Trail Clear": PlokLocationData(
        region="Legacy Island",
        address=0x1C0010
    ),
    "LI - Crouch Hill Clear": PlokLocationData(
        region="Legacy Island",
        address=0x1C0011
    ),
    "LI - Bobbin Bros Clear": PlokLocationData(
        region="Legacy Island",
        address=0x1C0012
    ),
    "AK - Plok Town Clear": PlokLocationData(
        region="Plok Town",
        address=0x1C0013
    ),
    "AK - Penkinos Clear": PlokLocationData(
        region="Akrillic",
        address=0x1C0014
    ),
    "AK - Venge Thicket Clear": PlokLocationData(
        region="Venge Thicket",
        address=0x1C0015
    ),
    "AK - Dreamy Cove Clear": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C0016
    ),

    "AK - Creepy Forest Clear": PlokLocationData(
        region="Creepy Forest",
        address=0x1C0017
    ),
    "AK - Womack Spider Clear": PlokLocationData(
        region="Akrillic Cave",
        address=0x1C0018
    ),
    "AK - Creepy Crag Clear": PlokLocationData(
        region="Creepy Crag",
        address=0x1C0019
    ),
    "AK - Gohome Cavern Clear": PlokLocationData(
        region="Gohome Cavern",
        address=0x1C001A
    ),
    "AK - Crashing Rocks Clear": PlokLocationData(
        region="Crashing Rocks",
        address=0x1C001B
    ),
    "AK - Rockyfella Clear": PlokLocationData(
        region="Akrillic Cave",
        address=0x1C001C
    ),

    "FP - Cycling Clever Clear": PlokLocationData(
        region="Cycling Clever",
        address=0x1C0020
    ),
    "FP - Road Hogging Clear": PlokLocationData(
        region="Road Hogging",
        address=0x1C0021
    ),
    "FP - High Flying Clear": PlokLocationData(
        region="High Flying",
        address=0x1C0022
    ),
    "FP - Easy Riding Clear": PlokLocationData(
        region="Easy Riding",
        address=0x1C0023
    ),
    "FP - In A Spin Clear": PlokLocationData(
        region="In A Spin",
        address=0x1C0024
    ),
    "FP - Real Rumblings Clear": PlokLocationData(
        region="Real Rumblings",
        address=0x1C0025
    ),
    "FP - Silent Running Clear": PlokLocationData(
        region="Silent Running",
        address=0x1C0026
    ),
    "FP - Flea Queen Clear": PlokLocationData(
        region="Flea Pit",
        #address=0x1C0027,
        locked_item="Flea Queen Dead"
    ),

    # Warps
    "CI - Beach Warp": PlokLocationData(
        region="Cotton Island",
        address=0x1C0030
    ),
    "CI - Columns Warp": PlokLocationData(
        region="Cotton Island",
        address=0x1C0031
    ),
    "CI - Rickety Bridge Warp": PlokLocationData(
        region="Cotton Island",
        address=0x1C0032
    ),
    "CI - Blind Leap Warp": PlokLocationData(
        region="Cotton Island",
        address=0x1C0033
    ),
    "AK - Dreamy Cove Warp": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C0034
    ),
    "AK - Crashing Rocks Warp": PlokLocationData(
        region="Crashing Rocks",
        address=0x1C0035
    ),

    # Fruits
    "CI - Beach Fruit": PlokLocationData(
        region="Cotton Island",
        address=0x1C0040
    ),
    "CI - Bridge Fruit": PlokLocationData(
        region="Cotton Island",
        address=0x1C0041
    ),
    "CI - Columns Fruit": PlokLocationData(
        region="Cotton Island",
        address=0x1C0042
    ),
    "CI - Log Falls Fruit": PlokLocationData(
        region="Cotton Island",
        address=0x1C0043
    ),
    "CI - Rickety Bridge Fruit": PlokLocationData(
        region="Cotton Island",
        address=0x1C0044
    ),
    "CI - Crazy Cradles Fruit": PlokLocationData(
        region="Cotton Island",
        address=0x1C0045
    ),
    "CI - Blind Leap Spire Fruit": PlokLocationData(
        region="Cotton Island",
        address=0x1C0046
    ),
    "CI - Blind Leap Sky Fruit": PlokLocationData(
        region="Cotton Island",
        address=0x1C0059
    ),
    "AK - Garlen Beach Upper Fruit": PlokLocationData(
        region="Garlen Beach",
        address=0x1C0047
    ),
    "AK - Garlen Beach Lower Fruit": PlokLocationData(
        region="Garlen Beach",
        address=0x1C005A
    ),
    "AK - Sleepy Dale Fruit": PlokLocationData(
        region="Sleepy Dale",
        address=0x1C0048
    ),
    "LI - Zig Zag Fruit": PlokLocationData(
        region="Legacy Island",
        address=0x1C0049
    ),
    "LI - Sponge Rocks Fruit": PlokLocationData(
        region="Legacy Island",
        address=0x1C004A
    ),
    "LI - Swifty Peaks Fruit": PlokLocationData(
        region="Legacy Island",
        address=0x1C004B
    ),
    "LI - Log Trail Fruit": PlokLocationData(
        region="Legacy Island",
        address=0x1C004C
    ),
    "LI - Crouch Hill Fruit": PlokLocationData(
        region="Legacy Island",
        address=0x1C004D
    ),
    "AK - Plok Town Left Fruit": PlokLocationData(
        region="Plok Town",
        address=0x1C004E
    ),
    "AK - Plok Town Right Fruit": PlokLocationData(
        region="Plok Town",
        address=0x1C004F
    ),
    "AK - Venge Thicket Fruit": PlokLocationData(
        region="Venge Thicket",
        address=0x1C0050
    ),
    "AK - Dreamy Cove Middle Fruit": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C0051
    ),
    "AK - Dreamy Cove Left Fruit": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C0052
    ),
    "AK - Dreamy Cove Right Fruit": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C0053
    ),
    "AK - Gohome Cavern Fruit": PlokLocationData(
        region="Gohome Cavern",
        address=0x1C0054
    ),
    "AK - Crashing Rocks Fruit": PlokLocationData(
        region="Crashing Rocks",
        address=0x1C0055
    ),
    "FP - Road Hogging Fruit": PlokLocationData(
        region="Road Hogging",
        address=0x1C0056
    ),
    "FP - Easy Riding Fruit": PlokLocationData(
        region="Easy Riding",
        address=0x1C0057
    ),
    "FP - High Flying Fruit": PlokLocationData(
        region="High Flying",
        address=0x1C005B
    ),
    "FP - In A Spin Fruit": PlokLocationData(
        region="In A Spin",
        address=0x1C0058
    ),
    "FP - Silent Running Fruit": PlokLocationData(
        region="Silent Running",
        address=0x1C005C
    ),
    

    # Gifts
    "CI - Bridge Plocky Gift": PlokLocationData(
        region="Cotton Island",
        address=0x1C0060
    ),
    "CI - Log Falls Squire Gift": PlokLocationData(
        region="Cotton Island",
        address=0x1C0061
    ),
    "CI - Crazy Cradles Flamethrower Gift": PlokLocationData(
        region="Cotton Island",
        address=0x1C006B
    ),
    "AK - Sleepy Dale Squire Gift": PlokLocationData(
        region="Sleepy Dale",
        address=0x1C0062
    ),
    "AK - Plok Town Rocketman Gift": PlokLocationData(
        region="Plok Town",
        address=0x1C0063
    ),
    "AK - Venge Thicket Plocky Gift": PlokLocationData(
        region="Venge Thicket",
        address=0x1C0064
    ),
    "AK - Venge Thicket Rocketman Gift": PlokLocationData(
        region="Venge Thicket",
        address=0x1C0065
    ),
    "AK - Dreamy Cove Flamethrower Gift": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C0066
    ),
    "AK - Creepy Forest Flamethrower Gift": PlokLocationData(
        region="Creepy Forest",
        address=0x1C0067
    ),
    "AK - Creepy Forest Rocketman Gift": PlokLocationData(
        region="Creepy Forest",
        address=0x1C0068
    ),
    "AK - Creepy Crag Flamethrower Gift": PlokLocationData(
        region="Creepy Crag",
        address=0x1C0069
    ),
    "AK - Creepy Crag Cowboy Gift": PlokLocationData(
        region="Creepy Crag",
        address=0x1C006A
    ),

    # Letters
    "AK - Garlen Beach Letter": PlokLocationData(
        region="Garlen Beach",
        address=0x1C0070
    ),
    "AK - Plok Town Letter Basement": PlokLocationData(
        region="Plok Town",
        address=0x1C0071
    ),
    "AK - Plok Town Letter Tower": PlokLocationData(
        region="Plok Town",
        address=0x1C0072
    ),
    "AK - Plok Town Letter Sky": PlokLocationData(
        region="Plok Town",
        address=0x1C0073
    ),
    "AK - Creepy Forest Left Letter": PlokLocationData(
        region="Creepy Forest",
        address=0x1C0074
    ),
    "AK - Creepy Forest Right Letter": PlokLocationData(
        region="Creepy Forest",
        address=0x1C0075
    ),
    "AK - Creepy Crag Letter": PlokLocationData(
        region="Creepy Crag",
        address=0x1C0076
    ),
    "FP - Real Rumblings Letter": PlokLocationData(
        region="Flea Pit",
        address=0x1C0077
    ),
}

location_flea_data_table: Dict[str, PlokLocationData] = {
    "AK - Garlen Beach Flea 1": PlokLocationData(
        region="Garlen Beach",
        address=0x1C0081
    ),
    "AK - Garlen Beach Flea 2": PlokLocationData(
        region="Garlen Beach",
        address=0x1C0082
    ),
    "AK - Garlen Beach Flea 3": PlokLocationData(
        region="Garlen Beach",
        address=0x1C0083
    ),
    "AK - Garlen Beach Flea 4": PlokLocationData(
        region="Garlen Beach",
        address=0x1C0084
    ),
    "AK - Garlen Beach Flea 5": PlokLocationData(
        region="Garlen Beach",
        address=0x1C0085
    ),
    "AK - Garlen Beach Flea 6": PlokLocationData(
        region="Garlen Beach",
        address=0x1C0086
    ),
    "AK - Garlen Beach Flea 7": PlokLocationData(
        region="Garlen Beach",
        address=0x1C0087
    ),
    "AK - Garlen Beach Flea 8": PlokLocationData(
        region="Garlen Beach",
        address=0x1C0088
    ),
    "AK - Garlen Beach Flea 9": PlokLocationData(
        region="Garlen Beach",
        address=0x1C0089
    ),
    "AK - Garlen Beach Flea 10": PlokLocationData(
        region="Garlen Beach",
        address=0x1C008A
    ),
    "AK - Garlen Beach Flea 11": PlokLocationData(
        region="Garlen Beach",
        address=0x1C008B
    ),
    "AK - Garlen Beach Flea 12": PlokLocationData(
        region="Garlen Beach",
        address=0x1C008C
    ),
    "AK - Garlen Beach Flea 13": PlokLocationData(
        region="Garlen Beach",
        address=0x1C008D
    ),
    "AK - Garlen Beach Flea 14": PlokLocationData(
        region="Garlen Beach",
        address=0x1C008E
    ),

    "AK - Sleepy Dale Flea 1": PlokLocationData(
        region="Sleepy Dale",
        address=0x1C0091
    ),
    "AK - Sleepy Dale Flea 2": PlokLocationData(
        region="Sleepy Dale",
        address=0x1C0092
    ),
    "AK - Sleepy Dale Flea 3": PlokLocationData(
        region="Sleepy Dale",
        address=0x1C0093
    ),
    "AK - Sleepy Dale Flea 4": PlokLocationData(
        region="Sleepy Dale",
        address=0x1C0094
    ),
    "AK - Sleepy Dale Flea 5": PlokLocationData(
        region="Sleepy Dale",
        address=0x1C0095
    ),
    "AK - Sleepy Dale Flea 6": PlokLocationData(
        region="Sleepy Dale",
        address=0x1C0096
    ),
    "AK - Sleepy Dale Flea 7": PlokLocationData(
        region="Sleepy Dale",
        address=0x1C0097
    ),
    "AK - Sleepy Dale Flea 8": PlokLocationData(
        region="Sleepy Dale",
        address=0x1C0098
    ),
    "AK - Sleepy Dale Flea 9": PlokLocationData(
        region="Sleepy Dale",
        address=0x1C0099
    ),
    "AK - Sleepy Dale Flea 10": PlokLocationData(
        region="Sleepy Dale",
        address=0x1C009A
    ),
    "AK - Sleepy Dale Flea 11": PlokLocationData(
        region="Sleepy Dale",
        address=0x1C009B
    ),
    "AK - Sleepy Dale Flea 12": PlokLocationData(
        region="Sleepy Dale",
        address=0x1C009C
    ),

    "AK - Plok Town Flea 1": PlokLocationData(
        region="Plok Town",
        address=0x1C00A1
    ),
    "AK - Plok Town Flea 2": PlokLocationData(
        region="Plok Town",
        address=0x1C00A2
    ),
    "AK - Plok Town Flea 3": PlokLocationData(
        region="Plok Town",
        address=0x1C00A3
    ),
    "AK - Plok Town Flea 4": PlokLocationData(
        region="Plok Town",
        address=0x1C00A4
    ),
    "AK - Plok Town Flea 5": PlokLocationData(
        region="Plok Town",
        address=0x1C00A5
    ),
    "AK - Plok Town Flea 6": PlokLocationData(
        region="Plok Town",
        address=0x1C00A6
    ),
    "AK - Plok Town Flea 7": PlokLocationData(
        region="Plok Town",
        address=0x1C00A7
    ),
    "AK - Plok Town Flea 8": PlokLocationData(
        region="Plok Town",
        address=0x1C00A8
    ),
    "AK - Plok Town Flea 9": PlokLocationData(
        region="Plok Town",
        address=0x1C00A9
    ),
    "AK - Plok Town Flea 10": PlokLocationData(
        region="Plok Town",
        address=0x1C00AA
    ),

    "AK - Venge Thicket Flea 1": PlokLocationData(
        region="Venge Thicket",
        address=0x1C00B1
    ),
    "AK - Venge Thicket Flea 2": PlokLocationData(
        region="Venge Thicket",
        address=0x1C00B2
    ),
    "AK - Venge Thicket Flea 3": PlokLocationData(
        region="Venge Thicket",
        address=0x1C00B3
    ),
    "AK - Venge Thicket Flea 4": PlokLocationData(
        region="Venge Thicket",
        address=0x1C00B4
    ),
    "AK - Venge Thicket Flea 5": PlokLocationData(
        region="Venge Thicket",
        address=0x1C00B5
    ),
    "AK - Venge Thicket Flea 6": PlokLocationData(
        region="Venge Thicket",
        address=0x1C00B6
    ),
    "AK - Venge Thicket Flea 7": PlokLocationData(
        region="Venge Thicket",
        address=0x1C00B7
    ),
    "AK - Venge Thicket Flea 8": PlokLocationData(
        region="Venge Thicket",
        address=0x1C00B8
    ),
    "AK - Venge Thicket Flea 9": PlokLocationData(
        region="Venge Thicket",
        address=0x1C00B9
    ),
    "AK - Venge Thicket Flea 10": PlokLocationData(
        region="Venge Thicket",
        address=0x1C00BA
    ),

    "AK - Dreamy Cove Flea 1": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C00C1
    ),
    "AK - Dreamy Cove Flea 2": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C00C2
    ),
    "AK - Dreamy Cove Flea 3": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C00C3
    ),
    "AK - Dreamy Cove Flea 4": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C00C4
    ),
    "AK - Dreamy Cove Flea 5": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C00C5
    ),
    "AK - Dreamy Cove Flea 6": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C00C6
    ),
    "AK - Dreamy Cove Flea 7": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C00C7
    ),
    "AK - Dreamy Cove Flea 8": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C00C8
    ),
    "AK - Dreamy Cove Flea 9": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C00C9
    ),
    "AK - Dreamy Cove Flea 10": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C00CA
    ),
    "AK - Dreamy Cove Flea 11": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C00CB
    ),
    "AK - Dreamy Cove Flea 12": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C00CC
    ),
    "AK - Dreamy Cove Flea 13": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C00CD
    ),
    "AK - Dreamy Cove Flea 14": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C00CE
    ),
    "AK - Dreamy Cove Flea 15": PlokLocationData(
        region="Dreamy Cove",
        address=0x1C00CF
    ),

    "AK - Creepy Forest Flea 1": PlokLocationData(
        region="Creepy Forest",
        address=0x1C00D1
    ),
    "AK - Creepy Forest Flea 2": PlokLocationData(
        region="Creepy Forest",
        address=0x1C00D2
    ),
    "AK - Creepy Forest Flea 3": PlokLocationData(
        region="Creepy Forest",
        address=0x1C00D3
    ),
    "AK - Creepy Forest Flea 4": PlokLocationData(
        region="Creepy Forest",
        address=0x1C00D4
    ),
    "AK - Creepy Forest Flea 5": PlokLocationData(
        region="Creepy Forest",
        address=0x1C00D5
    ),
    "AK - Creepy Forest Flea 6": PlokLocationData(
        region="Creepy Forest",
        address=0x1C00D6
    ),
    "AK - Creepy Forest Flea 7": PlokLocationData(
        region="Creepy Forest",
        address=0x1C00D7
    ),
    "AK - Creepy Forest Flea 8": PlokLocationData(
        region="Creepy Forest",
        address=0x1C00D8
    ),
    "AK - Creepy Forest Flea 9": PlokLocationData(
        region="Creepy Forest",
        address=0x1C00D9
    ),
    "AK - Creepy Forest Flea 10": PlokLocationData(
        region="Creepy Forest",
        address=0x1C00DA
    ),
    "AK - Creepy Forest Flea 11": PlokLocationData(
        region="Creepy Forest",
        address=0x1C00DB
    ),
    "AK - Creepy Forest Flea 12": PlokLocationData(
        region="Creepy Forest",
        address=0x1C00DC
    ),
    "AK - Creepy Forest Flea 13": PlokLocationData(
        region="Creepy Forest",
        address=0x1C00DD
    ),
    "AK - Creepy Forest Flea 14": PlokLocationData(
        region="Creepy Forest",
        address=0x1C00DE
    ),

    "AK - Creepy Crag Flea 1": PlokLocationData(
        region="Creepy Crag",
        address=0x1C00E1
    ),
    "AK - Creepy Crag Flea 2": PlokLocationData(
        region="Creepy Crag",
        address=0x1C00E2
    ),
    "AK - Creepy Crag Flea 3": PlokLocationData(
        region="Creepy Crag",
        address=0x1C00E3
    ),
    "AK - Creepy Crag Flea 4": PlokLocationData(
        region="Creepy Crag",
        address=0x1C00E4
    ),
    "AK - Creepy Crag Flea 5": PlokLocationData(
        region="Creepy Crag",
        address=0x1C00E5
    ),
    "AK - Creepy Crag Flea 6": PlokLocationData(
        region="Creepy Crag",
        address=0x1C00E6
    ),
    "AK - Creepy Crag Flea 7": PlokLocationData(
        region="Creepy Crag",
        address=0x1C00E7
    ),
    "AK - Creepy Crag Flea 8": PlokLocationData(
        region="Creepy Crag",
        address=0x1C00E8
    ),
    "AK - Creepy Crag Flea 9": PlokLocationData(
        region="Creepy Crag",
        address=0x1C00E9
    ),
    "AK - Creepy Crag Flea 10": PlokLocationData(
        region="Creepy Crag",
        address=0x1C00EA
    ),
    "AK - Creepy Crag Flea 11": PlokLocationData(
        region="Creepy Crag",
        address=0x1C00EB
    ),

    "AK - Gohome Cavern Flea 1": PlokLocationData(
        region="Gohome Cavern",
        address=0x1C00F1
    ),
    "AK - Gohome Cavern Flea 2": PlokLocationData(
        region="Gohome Cavern",
        address=0x1C00F2
    ),
    "AK - Gohome Cavern Flea 3": PlokLocationData(
        region="Gohome Cavern",
        address=0x1C00F3
    ),
    "AK - Gohome Cavern Flea 4": PlokLocationData(
        region="Gohome Cavern",
        address=0x1C00F4
    ),
    "AK - Gohome Cavern Flea 5": PlokLocationData(
        region="Gohome Cavern",
        address=0x1C00F5
    ),
    "AK - Gohome Cavern Flea 6": PlokLocationData(
        region="Gohome Cavern",
        address=0x1C00F6
    ),
    "AK - Gohome Cavern Flea 7": PlokLocationData(
        region="Gohome Cavern",
        address=0x1C00F7
    ),
    "AK - Gohome Cavern Flea 8": PlokLocationData(
        region="Gohome Cavern",
        address=0x1C00F8
    ),
    "AK - Gohome Cavern Flea 9": PlokLocationData(
        region="Gohome Cavern",
        address=0x1C00F9
    ),
    "AK - Gohome Cavern Flea 10": PlokLocationData(
        region="Gohome Cavern",
        address=0x1C00FA
    ),
    "AK - Gohome Cavern Flea 11": PlokLocationData(
        region="Gohome Cavern",
        address=0x1C00FB
    ),
    "AK - Gohome Cavern Flea 12": PlokLocationData(
        region="Gohome Cavern",
        address=0x1C00FC
    ),
    "AK - Gohome Cavern Flea 13": PlokLocationData(
        region="Gohome Cavern",
        address=0x1C00FD
    ),
    "AK - Gohome Cavern Flea 14": PlokLocationData(
        region="Gohome Cavern",
        address=0x1C00FE
    ),

    "AK - Crashing Rocks Flea 1": PlokLocationData(
        region="Crashing Rocks",
        address=0x1C0101
    ),
    "AK - Crashing Rocks Flea 2": PlokLocationData(
        region="Crashing Rocks",
        address=0x1C0102
    ),
    "AK - Crashing Rocks Flea 3": PlokLocationData(
        region="Crashing Rocks",
        address=0x1C0103
    ),
    "AK - Crashing Rocks Flea 4": PlokLocationData(
        region="Crashing Rocks",
        address=0x1C0104
    ),
    "AK - Crashing Rocks Flea 5": PlokLocationData(
        region="Crashing Rocks",
        address=0x1C0105
    ),
    "AK - Crashing Rocks Flea 6": PlokLocationData(
        region="Crashing Rocks",
        address=0x1C0106
    ),
    "AK - Crashing Rocks Flea 7": PlokLocationData(
        region="Crashing Rocks",
        address=0x1C0107
    ),
    "AK - Crashing Rocks Flea 8": PlokLocationData(
        region="Crashing Rocks",
        address=0x1C0108
    ),
}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
flea_location_table = {name: data.address for name, data in location_flea_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}
