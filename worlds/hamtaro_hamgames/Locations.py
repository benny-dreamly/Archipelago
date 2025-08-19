from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from . import HamGamesWorld


class HamGamesLocation(Location):
    game = "Hamtaro Hamham Games"

class HamGamesLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[["HamGamesWorld"], bool] = lambda world: True
    locked_item: Optional[str] = None
    type: Optional[str] = None
    flag_offset: Optional[int] = None
    flag_mask: Optional[int] = None
    day: Optional[int] = None
    # Talksanity
    rom_offset: Optional[int] = None
    text_data: Optional[int] = None

location_data_table: Dict[str, HamGamesLocation] = {
    "Day 1 Stadium - 100hm Dash Gold Medal": HamGamesLocationData(
        region="Day 1 - Stadium",
        address=0x1C2200,
        type = "Medal",
        day = 1,
    ),
    "Day 1 Stadium - 100hm Dash Silver Medal": HamGamesLocationData(
        region="Day 1 - Stadium",
        address=0x1C2201,
        type = "Medal",
        day = 1,
    ),
    "Day 1 Stadium - 100hm Dash Bronze Medal": HamGamesLocationData(
        region="Day 1 - Stadium",
        address=0x1C2202,
        type = "Medal",
        day = 1,
    ),

    "Day 2 Tennis - Win Tennis Prelim": HamGamesLocationData(
        region="Day 2 - Tennis",
        address=0x1C2203,
        type = "Medal",
        day = 2,
    ),
    #"Day 2 Tennis - Tennis Prelim Silver Medal": HamGamesLocationData(
    #    region="Day 2 - Tennis",
    #    address=0x1C2203,
    #    type = "Medal",
    #    day = 2,
    #),
    #"Day 2 Tennis - Tennis Prelim Bronze Medal": HamGamesLocationData(
    #    region="Day 2 - Tennis",
    #    address=0x1C2203,
    #    type = "Medal",
    #    day = 2,
    #),
    "Day 2 Stadium - Hammer Throw Gold Medal": HamGamesLocationData(
        region="Day 2 - Stadium",
        address=0x1C2206,
        type = "Medal",
        day = 2,
    ),
    "Day 2 Stadium - Hammer Throw Silver Medal": HamGamesLocationData(
        region="Day 2 - Stadium",
        address=0x1C2207,
        type = "Medal",
        day = 2,
    ),
    "Day 2 Stadium - Hammer Throw Bronze Medal": HamGamesLocationData(
        region="Day 2 - Stadium",
        address=0x1C2208,
        type = "Medal",
        day = 2,
    ),
    "Day 2 Pool - Diving Gold Medal": HamGamesLocationData(
        region="Day 2 - Pool",
        address=0x1C2209,
        type = "Medal",
        day = 2,
    ),
    "Day 2 Pool - Diving Silver Medal": HamGamesLocationData(
        region="Day 2 - Pool",
        address=0x1C220A,
        type = "Medal",
        day = 2,
    ),
    "Day 2 Pool - Diving Bronze Medal": HamGamesLocationData(
        region="Day 2 - Pool",
        address=0x1C220B,
        type = "Medal",
        day = 2,
    ),

    "Day 3 Beach - Win Beach Volleyball Premlim": HamGamesLocationData(
        region="Day 3 - Beach",
        address=0x1C220C,
        type = "Medal",
        day = 3,
    ),
    #"Day 3 Beach - Beach Volleyball Premlim Silver Medal": HamGamesLocationData(
    #    region="Day 3 - Beach",
    #    address=0x1C220D,
    #    type = "Medal",
    #    day = 3,
    #),
    #"Day 3 Beach - Beach Volleyball Premlim Bronze Medal": HamGamesLocationData(
    #    region="Day 3 - Beach",
    #    address=0x1C220E,
    #    type = "Medal",
    #    day = 3,
    #),
    "Day 3 Stadium - Hurdles Gold Medal": HamGamesLocationData(
        region="Day 3 - Stadium",
        address=0x1C220F,
        type = "Medal",
        day = 3,
    ),
    "Day 3 Stadium - Hurdles Silver Medal": HamGamesLocationData(
        region="Day 3 - Stadium",
        address=0x1C2210,
        type = "Medal",
        day = 3,
    ),
    "Day 3 Stadium - Hurdles Bronze Medal": HamGamesLocationData(
        region="Day 3 - Stadium",
        address=0x1C2211,
        type = "Medal",
        day = 3,
    ),
    "Day 3 Lawn - Birdback Riding Gold Medal": HamGamesLocationData(
        region="Day 3 - Lawn",
        address=0x1C2212,
        type = "Medal",
        day = 3,
    ),
    "Day 3 Lawn - Birdback Riding Silver Medal": HamGamesLocationData(
        region="Day 3 - Lawn",
        address=0x1C2213,
        type = "Medal",
        day = 3,
    ),
    "Day 3 Lawn - Birdback Riding Bronze Medal": HamGamesLocationData(
        region="Day 3 - Lawn",
        address=0x1C2214,
        type = "Medal",
        day = 3,
    ),

    "Day 4 Stadium - Pole Vault Gold Medal": HamGamesLocationData(
        region="Day 4 - Stadium",
        address=0x1C2215,
        type = "Medal",
        day = 4,
    ),
    "Day 4 Stadium - Pole Vault Silver Medal": HamGamesLocationData(
        region="Day 4 - Stadium",
        address=0x1C2216,
        type = "Medal",
        day = 4,
    ),
    "Day 4 Stadium - Pole Vault Bronze Medal": HamGamesLocationData(
        region="Day 4 - Stadium",
        address=0x1C2217,
        type = "Medal",
        day = 4,
    ),
    "Day 4 Tennis - Tennis Final Gold Medal": HamGamesLocationData(
        region="Day 4 - Tennis",
        address=0x1C2218,
        type = "Medal",
        day = 4,
    ),
    "Day 4 Tennis - Tennis Final Silver Medal": HamGamesLocationData(
        region="Day 4 - Tennis",
        address=0x1C2219,
        type = "Medal",
        day = 4,
    ),
    "Day 4 Tennis - Tennis Final Bronze Medal": HamGamesLocationData(
        region="Day 4 - Tennis",
        address=0x1C221A,
        type = "Medal",
        day = 4,
    ),
    "Day 4 Lawn - Carrot Pull Gold Medal": HamGamesLocationData(
        region="Day 4 - Lawn",
        address=0x1C221B,
        type = "Medal",
        day = 4,
    ),
    "Day 4 Lawn - Carrot Pull Silver Medal": HamGamesLocationData(
        region="Day 4 - Lawn",
        address=0x1C221C,
        type = "Medal",
        day = 4,
    ),
    "Day 4 Lawn - Carrot Pull Bronze Medal": HamGamesLocationData(
        region="Day 4 - Lawn",
        address=0x1C221D,
        type = "Medal",
        day = 4,
    ),

    "Day 5 Pool - Swimming Gold Medal": HamGamesLocationData(
        region="Day 5 - Pool",
        address=0x1C221E,
        type = "Medal",
        day = 5,
    ),
    "Day 5 Pool - Swimming Silver Medal": HamGamesLocationData(
        region="Day 5 - Pool",
        address=0x1C221F,
        type = "Medal",
        day = 5,
    ),
    "Day 5 Pool - Swimming Bronze Medal": HamGamesLocationData(
        region="Day 5 - Pool",
        address=0x1C2220,
        type = "Medal",
        day = 5,
    ),
    "Day 5 Lawn - Archery Gold Medal": HamGamesLocationData(
        region="Day 5 - Lawn",
        address=0x1C2221,
        type = "Medal",
        day = 5,
    ), 
    "Day 5 Lawn - Archery Silver Medal": HamGamesLocationData(
        region="Day 5 - Lawn",
        address=0x1C2222,
        type = "Medal",
        day = 5,
    ),
    "Day 5 Lawn - Archery Bronze Medal": HamGamesLocationData(
        region="Day 5 - Lawn",
        address=0x1C2223,
        type = "Medal",
        day = 5,
    ),
    "Day 5 Beach - Sailing Gold Medal": HamGamesLocationData(
        region="Day 5 - Beach",
        address=0x1C2224,
        type = "Medal",
        day = 5,
    ),
    "Day 5 Beach - Sailing Silver Medal": HamGamesLocationData(
        region="Day 5 - Beach",
        address=0x1C2225,
        type = "Medal",
        day = 5,
    ),  
    "Day 5 Beach - Sailing Bronze Medal": HamGamesLocationData(
        region="Day 5 - Beach",
        address=0x1C2226,
        type = "Medal",
        day = 5,
    ),

    "Day 6 Stadium - Triple Jump Gold Medal": HamGamesLocationData(
        region="Day 6 - Stadium",
        address=0x1C2227,
        type = "Medal",
        day = 6,
    ),
    "Day 6 Stadium - Triple Jump Silver Medal": HamGamesLocationData(
        region="Day 6 - Stadium",
        address=0x1C2228,
        type = "Medal",
        day = 6,
    ),
    "Day 6 Stadium - Triple Jump Bronze Medal": HamGamesLocationData(
        region="Day 6 - Stadium",
        address=0x1C2229,
        type = "Medal",
        day = 6,
    ),
    "Day 6 Pool - Sychnronized Swimming Gold Medal": HamGamesLocationData(
        region="Day 6 - Pool",
        address=0x1C222A,
        type = "Medal",
        day = 6,
    ),
    "Day 6 Pool - Sychnronized Swimming Silver Medal": HamGamesLocationData(
        region="Day 6 - Pool",
        address=0x1C222B,
        type = "Medal",
        day = 6,
    ),
    "Day 6 Pool - Sychnronized Swimming Bronze Medal": HamGamesLocationData(
        region="Day 6 - Pool",
        address=0x1C222C,
        type = "Medal",
        day = 6,
    ),
    "Day 6 Beach - Beach Volleyball Final Gold Medal": HamGamesLocationData(
        region="Day 6 - Beach",
        address=0x1C222D,
        type = "Medal",
        day = 6,
    ),
    "Day 6 Beach - Beach Volleyball Final Silver Medal": HamGamesLocationData(
        region="Day 6 - Beach",
        address=0x1C222E,
        type = "Medal",
        day = 6,
    ),
    "Day 6 Beach - Beach Volleyball Final Bronze Medal": HamGamesLocationData(
        region="Day 6 - Beach",
        address=0x1C222F,
        type = "Medal",
        day = 6,
    ),
    "Day 7 Stadium - Marathon": HamGamesLocationData(
        region="Day 7 - Stadium",
        address=0x1C2230,
        type = "Medal",
        day = 7,
        #locked_item= "Hamham Games Trophy",
    ),
    "Hamigo 1 - Bijou": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2300,
    flag_offset=0x200CF2C,
    flag_mask=0x80,
    type="Hamigo",
    ),

    "Hamigo 2 - Boss": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2301,
    flag_offset=0x200CF2D,
    flag_mask=0x01,
    type="Hamigo",
    ),

    "Hamigo 3 - Oxnard": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2302,
    flag_offset=0x200CF2D,
    flag_mask=0x02,
    type="Hamigo",
    ),

    "Hamigo 4 - Cappy": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2303,
    flag_offset=0x200CF2D,
    flag_mask=0x04,
    type="Hamigo",
    ),

    "Hamigo 5 - Pashmina": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2304,
    flag_offset=0x200CF2D,
    flag_mask=0x08,
    type="Hamigo",
    ),

    "Hamigo 6 - Penelope": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2305,
    flag_offset=0x200CF2D,
    flag_mask=0x10,
    type="Hamigo",
    ),

    "Hamigo 7 - Prince Bo": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2306,
    flag_offset=0x200CF2D,
    flag_mask=0x20,
    type="Hamigo",
    ),

    "Hamigo 8 - Daisy": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2307,
    flag_offset=0x200CF2D,
    flag_mask=0x40,
    type="Hamigo",
    ),

    "Hamigo 9 - Ivy": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2308,
    flag_offset=0x200CF2D,
    flag_mask=0x80,
    type="Hamigo",
    ),

    "Hamigo 10 - Rosy": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2309,
    flag_offset=0x200CF2E,
    flag_mask=0x01,
    type="Hamigo",
    ),

    "Hamigo 11 - Hamstern": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C230A,
    flag_offset=0x200CF2E,
    flag_mask=0x02,
    type="Hamigo",
    ),

    "Hamigo 12 - Hamberto": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C230B,
    flag_offset=0x200CF2E,
    flag_mask=0x04,
    type="Hamigo",
    ),

    "Hamigo 13 - Cubbie": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C230C,
    flag_offset=0x200CF2E,
    flag_mask=0x08,
    type="Hamigo",
    ),

    "Hamigo 14 - Hambone": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C230D,
    flag_offset=0x200CF2E,
    flag_mask=0x10,
    type="Hamigo",
    ),

    "Hamigo 15 - Hambeard": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C230E,
    flag_offset=0x200CF2E,
    flag_mask=0x20,
    type="Hamigo",
    ),

    "Hamigo 16 - Leo": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C230F,
    flag_offset=0x200CF2E,
    flag_mask=0x40,
    type="Hamigo",
    ),

    "Hamigo 17 - Stripes": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2310,
    flag_offset=0x200CF2E,
    flag_mask=0x80,
    type="Hamigo",
    ),

    "Hamigo 18 - Bunny": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2311,
    flag_offset=0x200CF2F,
    flag_mask=0x01,
    type="Hamigo",
    ),

    "Hamigo 19 - Warts": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2312,
    flag_offset=0x200CF2F,
    flag_mask=0x02,
    type="Hamigo",
    ),

    "Hamigo 20 - Maxwell": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2313,
    flag_offset=0x200CF2F,
    flag_mask=0x04,
    type="Hamigo",
    ),

    "Hamigo 21 - Howdy": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2314,
    flag_offset=0x200CF2F,
    flag_mask=0x08,
    type="Hamigo",
    ),

    "Hamigo 22 - Dexter": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2315,
    flag_offset=0x200CF2F,
    flag_mask=0x10,
    type="Hamigo",
    ),

    "Hamigo 23 - Panda": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2316,
    flag_offset=0x200CF2F,
    flag_mask=0x20,
    type="Hamigo",
    ),

    "Hamigo 24 - Stan": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2317,
    flag_offset=0x200CF2F,
    flag_mask=0x40,
    type="Hamigo",
    ),

    "Hamigo 25 - Sandy": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2318,
    flag_offset=0x200CF2F,
    flag_mask=0x80,
    type="Hamigo",
    ),

    "Hamigo 26 - Snoozer": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2319,
    flag_offset=0x200CF30,
    flag_mask=0x01,
    type="Hamigo",
    ),

    "Hamigo 27 - Jingle": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C231A,
    flag_offset=0x200CF30,
    flag_mask=0x02,
    type="Hamigo",
    ),

    "Hamigo 28 - Lapis": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C231B,
    flag_offset=0x200CF30,
    flag_mask=0x04,
    type="Hamigo",
    ),

    "Hamigo 29 - Lazuli": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C231C,
    flag_offset=0x200CF30,
    flag_mask=0x08,
    type="Hamigo",
    ),

    "Hamigo 30 - Bomegrante": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C231D,
    flag_offset=0x200CF30,
    flag_mask=0x10,
    type="Hamigo",
    ),

    "Hamigo 31 - Borange": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C231E,
    flag_offset=0x200CF30,
    flag_mask=0x20,
    type="Hamigo",
    ),

    "Hamigo 32 - Bopaya": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C231F,
    flag_offset=0x200CF30,
    flag_mask=0x40,
    type="Hamigo",
    ),

    "Hamigo 33 - Bolime": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2320,
    flag_offset=0x200CF30,
    flag_mask=0x80,
    type="Hamigo",
    ),

    "Hamigo 34 - Boberry": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2321,
    flag_offset=0x200CF31,
    flag_mask=0x01,
    type="Hamigo",
    ),

    "Hamigo 35 - Bogrape": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2322,
    flag_offset=0x200CF31,
    flag_mask=0x02,
    type="Hamigo",
    ),

    "Hamigo 36 - Boplum": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2323,
    flag_offset=0x200CF31,
    flag_mask=0x04,
    type="Hamigo",
    ),

    "Hamigo 37 - Dewey": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2324,
    flag_offset=0x200CF31,
    flag_mask=0x08,
    type="Hamigo",
    ),

    "Hamigo 38 - Crystal": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2325,
    flag_offset=0x200CF31,
    flag_mask=0x10,
    type="Hamigo",
    ),

    "Hamigo 39 - Robo-Joe": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2326,
    flag_offset=0x200CF31,
    flag_mask=0x20,
    type="Hamigo",
    ),

    "Hamigo 40 - Flora": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2327,
    flag_offset=0x200CF31,
    flag_mask=0x40,
    type="Hamigo",
    ),

    "Hamigo 41 - Sparkle": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2328,
    flag_offset=0x200CF31,
    flag_mask=0x80,
    type="Hamigo",
    ),

    "Hamigo 42 - DJ": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2329,
    flag_offset=0x200CF32,
    flag_mask=0x01,
    type="Hamigo",
    ),

    "Hamigo 43 - Omar": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C232A,
    flag_offset=0x200CF32,
    flag_mask=0x02,
    type="Hamigo",
    ),

    "Hamigo 44 - Hamstarr": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C232B,
    flag_offset=0x200CF32,
    flag_mask=0x04,
    type="Hamigo",
    ),

    "Hamigo 45 - Djungarian Chorus": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C232C,
    flag_offset=0x200CF32,
    flag_mask=0x08,
    type="Hamigo",
    ),

    "Hamigo 46 - Postie": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C232D,
    flag_offset=0x200CF32,
    flag_mask=0x10,
    type="Hamigo",
    ),

    "Hamigo 47 - Carrobo": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C232E,
    flag_offset=0x200CF32,
    flag_mask=0x20,
    type="Hamigo",
    ),

    "Hamigo 48 - Ninham": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C232F,
    flag_offset=0x200CF32,
    flag_mask=0x40,
    type="Hamigo",
    ),

    "Hamigo 49 - Stucky": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2330,
    flag_offset=0x200CF32,
    flag_mask=0x80,
    type="Hamigo",
    ),

    "Hamigo 50 - Mister Matsu": HamGamesLocationData(
    region="Hamigo",
    address= 0x1C2331,
    flag_offset=0x200CF33,
    flag_mask=0x01,
    type="Hamigo",
    ),
    

    #"Clubhouse - Arcade 25 Points": HamGamesLocationData(
    #    region="Day 1 - Clubhouse",
    #    address=0x1C223F,
    #    type= "Event",
    #    day = 1,
    #),




}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}

hamigo_flag_data = {data.address: [data.flag_offset, data.flag_mask] for name, data in location_data_table.items() if data.type == "Hamigo"}