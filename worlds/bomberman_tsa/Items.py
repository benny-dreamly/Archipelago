from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from . import BombTSAWorld


class BombTSAItem(Item):
    game = "Bomberman The Second Attack"


class BombTSAItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable[["BombTSAWorld"], bool] = lambda world: True


item_data_table: Dict[str, BombTSAItemData] = {
    "Fire Stone": BombTSAItemData(
        code=0x1C30000,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "Ice Stone": BombTSAItemData(
        code=0x1C30001,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "Wind Stone": BombTSAItemData(
        code=0x1C30002,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "Earth Stone": BombTSAItemData(
        code=0x1C30003,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "Lightning Stone": BombTSAItemData(
        code=0x1C30004,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "Dark Stone": BombTSAItemData(
        code=0x1C30005,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "Light Stone": BombTSAItemData(
        code=0x1C30006,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "BombUp": BombTSAItemData(
        code=0x1C30007,
        type=ItemClassification.progression,
        num_exist= 3
    ),
    "FireUp": BombTSAItemData(
        code=0x1C30008,
        type=ItemClassification.progression,
        num_exist= 2
    ),
    "HealthUp": BombTSAItemData(
        code=0x1C30009,
        type=ItemClassification.useful,
        num_exist=5
    ),
    "Guardian Glove": BombTSAItemData(
        code=0x1C3000A,
        type=ItemClassification.progression,
    ),
    "Guardian Boots": BombTSAItemData(
        code=0x1C3000B,
        type=ItemClassification.progression,
    ),
    "Guardian Helmet": BombTSAItemData(
        code=0x1C3000C,
        type=ItemClassification.progression,
    ),
    "Guardian Armor": BombTSAItemData(
        code=0x1C3000D,
        type=ItemClassification.useful,
    ),
    "Skates": BombTSAItemData(
        code=0x1C3000E,
        type=ItemClassification.progression,
    ),


    #"Alcatraz": BombTSAItemData(
    #    code=0x1C30010,
    #    type=ItemClassification.progression,
    #),
    "Aquanet Coordinates": BombTSAItemData(
        code=0x1C30011,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "Horizon Coordinates": BombTSAItemData(
        code=0x1C30012,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "Starlight Coordinates": BombTSAItemData(
        code=0x1C30013,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "Neverland Coordinates": BombTSAItemData(
        code=0x1C30014,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "Epikyur Coordinates": BombTSAItemData(
        code=0x1C30015,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "Thantos Coordinates": BombTSAItemData(
        code=0x1C30016,
        type=ItemClassification.progression,
        num_exist=0
    ),
    "Noah Coordinates": BombTSAItemData(
        code=0x1C30017,
        type=ItemClassification.progression,
        num_exist= 0
    ),


    "Pommy Knuckle Gene": BombTSAItemData(
        code=0x1C30020,
        type=ItemClassification.progression,
        num_exist= 0
    ),
    "Pommy Animal Gene": BombTSAItemData(
        code=0x1C30021,
        type=ItemClassification.progression,
        num_exist= 0
    ),
    "Pommy Hammer Gene": BombTSAItemData(
        code=0x1C30022,
        type=ItemClassification.progression,
        num_exist= 0
    ),
    "Pommy Claw Gene": BombTSAItemData(
        code=0x1C30023,
        type=ItemClassification.progression,
        num_exist= 0
    ),
    "Pommy Penguin Gene": BombTSAItemData(
        code=0x1C30024,
        type=ItemClassification.progression,
        num_exist= 0
    ),
    "Pommy Beast Gene": BombTSAItemData(
        code=0x1C30025,
        type=ItemClassification.progression,
        num_exist= 0
    ),
    "Pommy Mage Gene": BombTSAItemData(
        code=0x1C30026,
        type=ItemClassification.useful,
        num_exist= 0
    ),
    "Pommy Knight Gene": BombTSAItemData(
        code=0x1C30027,
        type=ItemClassification.useful,
        num_exist= 0
    ),
    "Pommy Devil Gene": BombTSAItemData(
        code=0x1C30028,
        type=ItemClassification.useful,
        num_exist= 0
    ),
    "Pommy Cat Gene": BombTSAItemData(
        code=0x1C30029,
        type=ItemClassification.useful,
        num_exist= 0
    ),
    "Pommy Bird Gene": BombTSAItemData(
        code=0x1C3002A,
        type=ItemClassification.useful,
        num_exist= 0
    ),
    "Pommy Chicken Gene": BombTSAItemData(
        code=0x1C3002B,
        type=ItemClassification.useful,
        num_exist= 0
    ),
    "Pommy Dragon Gene": BombTSAItemData(
        code=0x1C3002C,
        type=ItemClassification.useful,
        num_exist= 0
    ),
    "Pommy Dinosaur Gene": BombTSAItemData(
        code=0x1C3002D,
        type=ItemClassification.useful,
        num_exist= 0
    ),
    "Pommy Pixie Gene": BombTSAItemData(
        code=0x1C3002E,
        type=ItemClassification.useful,
        num_exist= 0
    ),
    "Pommy Shadow Gene": BombTSAItemData(
        code=0x1C3002F,
        type=ItemClassification.useful,
        num_exist= 0
    ),

    # Filler
    "200 Coins": BombTSAItemData(
        code=0x1C30030,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Heart": BombTSAItemData(
        code=0x1C30031,
        type=ItemClassification.filler,
        num_exist=0
    ),
    "Gold Heart": BombTSAItemData(
        code=0x1C30032,
        type=ItemClassification.filler,
        num_exist=0
    ),

    # Traps
    "Stun Trap": BombTSAItemData(
        code=0x1C30040,
        type=ItemClassification.trap,
        num_exist=0
    ),
    "Panic Bomb Trap": BombTSAItemData(
        code=0x1C30041,
        type=ItemClassification.trap,
        num_exist=0
    ),
    "Fire Trap": BombTSAItemData(
        code=0x1C30042,
        type=ItemClassification.trap,
        num_exist=0
    ),
    "Reverse Trap": BombTSAItemData(
        code=0x1C30043,
        type=ItemClassification.trap,
        num_exist=0
    ),
    "Ejection Trap": BombTSAItemData(
        code=0x1C30044,
        type=ItemClassification.trap,
        num_exist=0
    ),
    
    # Stage Key Items
    "Blue Gems": BombTSAItemData(
        code=0x1C30018,
        type=ItemClassification.progression,
    ),
    "Green Gems": BombTSAItemData(
        code=0x1C30019,
        type=ItemClassification.progression,
    ),
    "Red Gem": BombTSAItemData(
        code=0x1C3001A,
        type=ItemClassification.progression,
    ),

    "Royal Straight": BombTSAItemData(
        code=0x1C3001B,
        type=ItemClassification.progression,
    ),

    "Haunted House Pass": BombTSAItemData(
        code=0x1C3001C,
        type=ItemClassification.progression,
    ),
    "Museum Pass": BombTSAItemData(
        code=0x1C3001D,
        type=ItemClassification.progression,
    ),
    "Coaster Battery": BombTSAItemData(
        code=0x1C3001E,
        type=ItemClassification.progression,
    ),

    "Train Batteries": BombTSAItemData(
        code=0x1C3001F,
        type=ItemClassification.progression,
    ),
    "Warship key": BombTSAItemData(
        code=0x1C30050,
        type=ItemClassification.progression,
        num_exist= 0
    ),


    #"Shop Coordinates": BombTSAItemData(
    #    code=0x1C30018,
    #    type=ItemClassification.progression,
    #),

    



    "Victory": BombTSAItemData(
        code=0x1CAEE12,
        type=ItemClassification.progression,
        num_exist=0
    ),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
