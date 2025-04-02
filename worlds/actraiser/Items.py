from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification, MultiWorld


class ActraiserItem(Item):
    game = "Actraiser"


class ActraiserItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True

item_data_table: Dict[str, ActraiserItemData] = {
    "Magical Fire": ActraiserItemData(
        code=0x1C1001,
        type=ItemClassification.useful
    ),
    "Magical Stardust": ActraiserItemData(
        code=0x1C1002,
        type=ItemClassification.useful
    ),
    "Magical Aura": ActraiserItemData(
        code=0x1C1003,
        type=ItemClassification.useful
    ),
    "Magical Light": ActraiserItemData(
        code=0x1C1004,
        type=ItemClassification.useful
    ),
    "Source of Life": ActraiserItemData(
        code=0x1C1005,
        type=ItemClassification.useful,
        num_exist=4
    ),
    "Source of Magic": ActraiserItemData(
        code=0x1C1006,
        type=ItemClassification.useful,
        num_exist=7
    ),
    "Loaf of Bread": ActraiserItemData(
        code=0x1C1007,
        type=ItemClassification.progression
    ),

    "Wheat": ActraiserItemData(
        code=0x1C1008,
        type=ItemClassification.progression
    ),
    "Herb": ActraiserItemData(
        code=0x1C1009,
        type=ItemClassification.progression
    ),
    "Bridge": ActraiserItemData(
        code=0x1C100A,
        type=ItemClassification.progression
    ),
    "Music": ActraiserItemData(
        code=0x1C100B,
        type=ItemClassification.progression
    ),
    #"Ancient Tablet": ActraiserItemData(
    #    code=0x1C100C,
    #    type=ItemClassification.progression
    #),
    "Ancient Tablet": ActraiserItemData(
        code=0x1C100D,
        type=ItemClassification.progression
    ),
    "Magic Skull": ActraiserItemData(
        code=0x1C100E,
        type=ItemClassification.progression
    ),
    "Fleece": ActraiserItemData(
        code=0x1C100F,
        type=ItemClassification.progression
    ),
    #"Bomb": ActraiserItemData(
    #    code=0x1C1010,
    #    type=ItemClassification.filler
    #),
    "Fertility": ActraiserItemData(
        code=0x1C1011,
        type=ItemClassification.useful,
        num_exist=6
    ),
    "Bomb": ActraiserItemData(
        code=0x1C1012,
        type=ItemClassification.useful,
        num_exist=6
    ),
    "Compass": ActraiserItemData(
        code=0x1C1013,
        type=ItemClassification.progression
    ),
    "Strength of Angel": ActraiserItemData(
        code=0x1C1014,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Level Up": ActraiserItemData(
        code=0x1C1015,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "Apple": ActraiserItemData(
        code=0x1C1016,
        type=ItemClassification.filler
    ),
    "Flame Sword": ActraiserItemData(
        code=0x1C1017,
        type=ItemClassification.useful,
        num_exist=0
    ),

    "Fillmore Advancement": ActraiserItemData(
        code=0x1C1018,
        type=ItemClassification.progression_skip_balancing,
        num_exist=2
    ),
    "Bloodpool Advancement": ActraiserItemData(
        code=0x1C1019,
        type=ItemClassification.progression_skip_balancing,
        num_exist=2
    ),
    "Kasandora Advancement": ActraiserItemData(
        code=0x1C101A,
        type=ItemClassification.progression_skip_balancing,
        num_exist=2
    ),
    "Aitos Advancement": ActraiserItemData(
        code=0x1C101B,
        type=ItemClassification.progression_skip_balancing,
        num_exist=2
    ),
    "Marahna Advancement": ActraiserItemData(
        code=0x1C101C,
        type=ItemClassification.progression_skip_balancing,
        num_exist=2
    ),
    "Northwall Advancement": ActraiserItemData(
        code=0x1C101D,
        type=ItemClassification.progression_skip_balancing,
        num_exist=2
    ),
    "Progressive Arrow": ActraiserItemData(
        code=0x1C101E,
        type=ItemClassification.useful,
        num_exist=0
    ),
    "Dheim Crystal": ActraiserItemData(
        code=0x1C101F,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "Lightning": ActraiserItemData(
        code=0x1C1020,
        type=ItemClassification.progression
    ),
    "Rain": ActraiserItemData(
        code=0x1C1021,
        type=ItemClassification.progression
    ),
    "Sun": ActraiserItemData(
        code=0x1C1022,
        type=ItemClassification.progression
    ),
    "Wind": ActraiserItemData(
        code=0x1C1023,
        type=ItemClassification.progression
    ),
    "Earthquake": ActraiserItemData(
        code=0x1C1024,
        type=ItemClassification.progression
    ),
    "1UP": ActraiserItemData(
        code=0x1C1025,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "1000 Points": ActraiserItemData(
        code=0x1C1026,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Magic": ActraiserItemData(
        code=0x1C1027,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Smite": ActraiserItemData( # Bomb Effect
        code=0x1C1028,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Population Boom": ActraiserItemData(
        code=0x1C1029,
        type=ItemClassification.useful,
        num_exist=0
    ),

    "Skull Trap": ActraiserItemData( # Spawns Skull Heads 
        code=0x1C1030,
        type=ItemClassification.trap,
        num_exist=0
    ),
    "Redirect Trap": ActraiserItemData( 
        code=0x1C1031,
        type=ItemClassification.trap,
        num_exist=0
    ),

    "Savior": ActraiserItemData(
        type=ItemClassification.progression,
        code=0x1C102A,
        num_exist=0
    ),
    "Prosperity": ActraiserItemData(
        type=ItemClassification.progression,
        code=0x1C102B,
        num_exist=0
    ) 
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
