from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from . import BombTSAWorld


class BombTSALocation(Location):
    game = "Bomberman The Second Attack"


class BombTSALocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[["BombTSAWorld"], bool] = lambda world: True
    locked_item: Optional[str] = None

location_data_table: Dict[str, BombTSALocationData] = {

    "Alcatraz Baelfael Defeated": BombTSALocationData(
        region="Alcatraz, Sewage Disposal",
        address=0x1C3001,
    ),
    "Aquanet Behemos Defeated": BombTSALocationData(
        region="Aquanet, Behemos' Lair",
        address=0x1C3002,
    ),
    "Horizon Ashtarth Defeated": BombTSALocationData(
        region="Horizon, Resting Point",
        address=0x1C3003,
    ),
    "Starlight Zhael Defeated": BombTSALocationData(
        region="Starlight, Stage Area",
        address=0x1C3004,
    ),
    "Neverland Molok Defeated": BombTSALocationData(
        region="Neverland, Furnace",
        address=0x1C3005,
    ),
    "Epikyur Zoniha Defeated": BombTSALocationData(
        region="Epikyur, Coaster Finish",
        address=0x1C3006,
    ),
    "Thantos Bulzeeb Defeated": BombTSALocationData(
        region="Thantos, Top of the Tower",
        address=0x1C3007,
    ),
    "World Saved": BombTSALocationData(
        region="Noah Core",
        address=0x1C3008,
        locked_item="Victory"
    ),

    "Neverland Guardian Armor": BombTSALocationData(
        region="Neverland, Secret Room 1",
        address=0x1C300A,
    ),
    "Horizon Guardian Armor": BombTSALocationData(
        region="Horizon, Secret Room 2",
        address=0x1C300B,
    ),
    "Starlight Guardian Armor": BombTSALocationData(
        region="Starlight, Hidden Room",
        address=0x1C300C,
    ),
    "Aquanet Guardian Armor": BombTSALocationData(
        region="Aquanet, Secret Room 2",
        address=0x1C300D,
    ),

    "Alcatraz Generator": BombTSALocationData(
        region="Alcatraz, Gravity Generator Room",
        address=0x1C3010,
    ),
    "Aquanet Generator": BombTSALocationData(
        region="Aquanet, Gravity Generator Room",
        address=0x1C3011,
    ),
    "Horizon Generator": BombTSALocationData(
        region="Horizon, Gravity Generator Room",
        address=0x1C3012,
    ),
    "Starlight Generator": BombTSALocationData(
        region="Starlight, Gravity Generator Room",
        address=0x1C3013,
    ),
    "Neverland Generator": BombTSALocationData(
        region="Neverland, Gravity Generator Room",
        address=0x1C3014,
    ),
    "Epikyur Generator": BombTSALocationData(
        region="Epikyur, Gravity Generator Room",
        address=0x1C3015,
    ),
    "Thantos Generator": BombTSALocationData(
        region="Thantos, Gravity Generator Room",
        address=0x1C3016,
    ),

    "Epikyur Part Red": BombTSALocationData(
        region="Epikyur, Haunted House Coaster Start",
        address=0x1C3020,
    ),
    "Neverland Part Red": BombTSALocationData(
        region="Neverland, Through the Line of Fire",
        address=0x1C3021,
    ),
    "Thantos Part Red": BombTSALocationData(
        region="Thantos, Compactor",
        address=0x1C3022,
    ),
    "Starlight Part Red": BombTSALocationData(
        region="Starlight, Casino Entrance",
        address=0x1C3023,
    ),
    "Alcatraz Part Red": BombTSALocationData(
        region="Alcatraz, Prison",
        address=0x1C3024,
    ),
    "Aquanet Part Red": BombTSALocationData(
        region="Aquanet, Secret Room 1",
        address=0x1C3025,
    ),
    "Horizon Part Red": BombTSALocationData(
        region="Horizon, First Trial",
        address=0x1C3026,
    ),

    "Epikyur Part Green": BombTSALocationData(
        region="Epikyur, Haunted House Spike Pit",
        address=0x1C3028,
    ),
    "Neverland Part Green": BombTSALocationData(
        region="Neverland, Secret Room 2",
        address=0x1C3029,
    ),
    "Thantos Part Green": BombTSALocationData(
        region="Thantos, Secret Room 3",
        address=0x1C302A,
    ),
    "Starlight Part Green": BombTSALocationData(
        region="Starlight, Slots Room",
        address=0x1C302B,
    ),
    "Alcatraz Part Green": BombTSALocationData(
        region="Alcatraz, Secret Room 2",
        address=0x1C302C,
    ),
    "Aquanet Part Green": BombTSALocationData(
        region="Aquanet, Secret Room 3",
        address=0x1C302D,
    ),
    "Horizon Part Green": BombTSALocationData(
        region="Horizon, Resting Point",
        address=0x1C302E,
    ),

    "Epikyur Part Blue": BombTSALocationData(
        region="Epikyur, Haunted House Hidden Room",
        address=0x1C3030,
    ),
    "Neverland Part Blue": BombTSALocationData(
        region="Neverland, Carrier Works",
        address=0x1C3031,
    ),
    "Thantos Part Blue": BombTSALocationData(
        region="Thantos, Subway Destination",
        address=0x1C3032,
    ),
    "Starlight Part Blue": BombTSALocationData(
        region="Starlight, Parking Lot",
        address=0x1C3033,
    ),
    "Alcatraz Part Blue": BombTSALocationData(
        region="Alcatraz, Secret Room 1",
        address=0x1C3034,
    ),
    "Aquanet Part Blue": BombTSALocationData(
        region="Aquanet, Elevator Hub",
        address=0x1C3035,
    ),
    "Horizon Part Blue": BombTSALocationData(
        region="Horizon, Second Trial",
        address=0x1C3036,
    ),

    "Epikyur Part Yellow": BombTSALocationData(
        region="Epikyur, History Museum Military Puzzle",
        address=0x1C3038,
    ),
    "Neverland Part Yellow": BombTSALocationData(
        region="Neverland, Safe Point",
        address=0x1C3039,
    ),
    "Thantos Part Yellow": BombTSALocationData(
        region="Thantos, Secret Room 1",
        address=0x1C303A,
    ),
    "Starlight Part Yellow": BombTSALocationData(
        region="Starlight, Stage Area",
        address=0x1C303B,
    ),
    "Alcatraz Part Yellow": BombTSALocationData(
        region="Alcatraz, Final Defense Unit",
        address=0x1C303C,
    ),
    "Aquanet Part Yellow": BombTSALocationData(
        region="Aquanet, Tower 3F",
        address=0x1C303D,
    ),
    "Horizon Part Yellow": BombTSALocationData(
        region="Horizon, Secret Room 1",
        address=0x1C303E,
    ),

    # Stage Specific
    "Horizon Left Blue Jewel": BombTSALocationData(
        region="Horizon, Second Trial",
        address=0x1C3040,
    ),
    "Horizon Right Blue Jewel": BombTSALocationData(
        region="Horizon, First Trial",
        address=0x1C3041,
    ),
    "Horizon Left Green Jewel": BombTSALocationData(
        region="Horizon, Fourth Trial",
        address=0x1C3042,
    ),
    "Horizon Right Green Jewel": BombTSALocationData(
        region="Horizon, Third Trial",
        address=0x1C3043,
    ),
    "Horizon Middle Green Jewel": BombTSALocationData(
        region="Horizon, Last Trial",
        address=0x1C3044,
    ),
    "Horizon Red Jewel": BombTSALocationData(
        region="Horizon, Final Deposit",
        address=0x1C3045,
    ),

    "Starlight King Of Clubs": BombTSALocationData(
        region="Starlight, Betting Room",
        address=0x1C3046,
    ),
    "Starlight Knight Of Diamonds": BombTSALocationData(
        region="Starlight, Alleyway",
        address=0x1C3047,
    ),
    "Starlight Ace Of Spaces": BombTSALocationData(
        region="Starlight, Fountain Square",
        address=0x1C3048,
    ),
    "Starlight Queen Of Hearts": BombTSALocationData(
        region="Starlight, Parking Lot",
        address=0x1C3049,
    ),

    "Epikyur Haunted House Pass": BombTSALocationData(
        region="Epikyur, Haunted House Storeroom",
        address=0x1C304A,
    ),
    "Epikyur Museum Pass": BombTSALocationData(
        region="Epikyur, History Museum Military Puzzle",
        address=0x1C304B,
    ),
    "Epikyur Coaster Battery": BombTSALocationData(
        region="Epikyur, History Museum Showcase Room",
        address=0x1C304C,
    ),

    "Thantos Lower Train Battery": BombTSALocationData(
        region="Thantos, Battle for the Battery",
        address=0x1C304D,
    ),
    "Thantos Upper Train Battery": BombTSALocationData(
        region="Thantos, Battery Ambush",
        address=0x1C304E,
    ),

    "Noah Card Key 1": BombTSALocationData(
        region="Noah",
        address=0x1C302F,
    ),
    "Noah Card Key 2": BombTSALocationData(
        region="Noah",
        address=0x1C303F,
    ),
    "Noah Card Key 3": BombTSALocationData(
        region="Noah",
        address=0x1C304F,
    ),

 
}

powerup_data_table: Dict[str, BombTSALocationData] = {
   # Remote Bombs
    "Alcatraz Remote Security Room":BombTSALocationData(
        region="Alcatraz, Security Room A",
        address=0x1C3060,
    ),
    "Aquanet Remote To the Tower":BombTSALocationData(
        region="Aquanet, To the Tower",
        address=0x1C3061,
    ),
    "Aquanet Remote Fountain Room":BombTSALocationData(
        region="Aquanet, Fountain Room",
        address=0x1C306A,
    ),
    "Horizon Remote Second Trial":BombTSALocationData(
        region="Horizon, Second Trial",
        address=0x1C3062,
    ),
    "Horizon Remote Final Deposit":BombTSALocationData(
        region="Horizon, Final Deposit",
        address=0x1C3063,
    ),
    "Horizon Remote Secret Room":BombTSALocationData(
        region="Horizon, Secret Room 1",
        address=0x1C3064,
    ),
    "Starlight Remote Casino Lobby":BombTSALocationData(
        region="Starlight, Casino Lobby",
        address=0x1C3065,
    ),
    "Starlight Remote Waiting Room":BombTSALocationData(
        region="Starlight, Waiting Room",
        address=0x1C3066,
    ),
    "Neverland Remote Bonus Room":BombTSALocationData(
        region="Neverland, Bonus Room",
        address=0x1C306B,
    ),
    "Neverland Remote Underground Corridor":BombTSALocationData(
        region="Neverland, Underground Corridor",
        address=0x1C3067,
    ),
    "Epikyur Remote Haunted House Yard":BombTSALocationData(
        region="Epikyur, Haunted House Coaster Start",
        address=0x1C3068,
    ),
    "Thantos Remote Crevice":BombTSALocationData(
        region="Thantos, The Crevice",
        address=0x1C3069,
    ),
    "Aquanet Remote Secret Room":BombTSALocationData(
        region="Aquanet, Secret Room 3",
        address=0x1C3070,
    ),

    # Gloves
    "Alcatraz Glove Security Room B": BombTSALocationData(
        region="Alcatraz, Security Room B",
        address=0x1C30C0,
    ),
    "Alcatraz Glove Pipe Room": BombTSALocationData(
        region="Alcatraz, Pipe Room A",
        address=0x1C30C1,
    ),
    "Epikyur Glove Center Fountain": BombTSALocationData(
        region="Epikyur, Center Fountain",
        address=0x1C30C2,
    ),
    "Aquanet Glove Landing Site": BombTSALocationData(
        region="Aquanet, Around the Moat",
        address=0x1C30C3,
    ),
    "Aquanet Glove Crab Room": BombTSALocationData(
        region="Aquanet, Water Channels",
        address=0x1C30C4,
    ),
    "Aquanet Glove Fountain Room": BombTSALocationData(
        region="Aquanet, Fountain Room",
        address=0x1C30C5,
    ),
    "Starlight Glove Slot Machines": BombTSALocationData(
        region="Starlight, Slots Room",
        address=0x1C30C6,
    ),
    "Starlight Glove Magician Room": BombTSALocationData(
        region="Starlight, Lookout Point",
        address=0x1C30C7,
    ),
    "Horizon Glove Eastern Tower": BombTSALocationData(
        region="Horizon, Eastern Tower",
        address=0x1C30C8,
    ),
    "Horizon Glove Basement Hub": BombTSALocationData(
        region="Horizon, Floating Temple",
        address=0x1C30C9,
    ),
    "Thantos Glove Ladder": BombTSALocationData(
        region="Thantos, Up the Ladder",
        address=0x1C30CA,
    ),
    "Thantos Glove Manhole Room": BombTSALocationData(
        region="Thantos, Secret Room 1",
        address=0x1C30CB,
    ),
    "Thantos Glove Chasm": BombTSALocationData(
        region="Thantos, The Crevice",
        address=0x1C30CC,
    ),



    # Bomb Kicks
    "Alcatraz Kick Twisted Sewers": BombTSALocationData(
        region="Alcatraz, Twisted Sewers",
        address=0x1C30D0,
    ),
    "Alcatraz Kick Security Room": BombTSALocationData(
        region="Alcatraz, Security Room A",
        address=0x1C30D1,
    ),
    "Alcatraz Kick Through the Pipe": BombTSALocationData(
        region="Alcatraz, Through the Pipe",
        address=0x1C30D2,
    ),
    "Alcatraz Kick Pipe Room": BombTSALocationData(
        region="Alcatraz, Pipe Room A",
        address=0x1C30D3,
    ),
    "Neverland Kick Intersection": BombTSALocationData(
        region="Neverland, Intersection",
        address=0x1C30D4,
    ),
    "Neverland Kick Cage Room": BombTSALocationData(
        region="Neverland, Cage Room",
        address=0x1C30D5,
    ),
    "Neverland Kick Generator Passageway": BombTSALocationData(
        region="Neverland, Third Passageway",
        address=0x1C30D6,
    ),
    "Epikyur Kick Center Fountain": BombTSALocationData(
        region="Epikyur, Center Fountain",
        address=0x1C30D7,
    ),
    "Aquanet Kick Pool room": BombTSALocationData(
        region="Aquanet, Swimming Pool Spa",
        address=0x1C30D8,
    ),
    "Aquanet Kick Top of Elevator Room": BombTSALocationData(
        region="Aquanet, Elevator Hub",
        address=0x1C30D9,
    ),
    "Starlight Kick Alleyway": BombTSALocationData(
        region="Starlight, Alleyway",
        address=0x1C30DA,
    ),
    "Starlight Kick Waiting Room": BombTSALocationData(
        region="Starlight, Waiting Room",
        address=0x1C30DB,
    ),
    "Starlight Kick Betting Room": BombTSALocationData(
        region="Starlight, Betting Room",
        address=0x1C30DC,
    ),
    "Horizon Kick Leading Road": BombTSALocationData(
        region="Horizon, Leading Road",
        address=0x1C30DD,
    ),
    "Horizon Kick Last Route": BombTSALocationData(
        region="Horizon, Last Route",
        address=0x1C30DE,
    ),
    "Thantos Kick Lower Battery": BombTSALocationData(
        region="Thantos, Battle for the Battery",
        address=0x1C30DF,
    ),
    "Thantos Kick Chasm": BombTSALocationData(
        region="Thantos, The Crevice",
        address=0x1C30E0,
    ),

}

pommy_data_table: Dict[str, BombTSALocationData] = {
    # Pommy
    "Pommy Knuckle Transformation": BombTSALocationData(
        region="Menu",
        address=0x1C3050,
    ),
    "Pommy Animal Transformation": BombTSALocationData(
        region="Menu",
        address=0x1C3051,
    ),
    "Pommy Hammer Transformation": BombTSALocationData(
        region="Menu",
        address=0x1C3052,
    ),
    "Pommy Claw Transformation": BombTSALocationData(
        region="Menu",
        address=0x1C3053,
    ),
    "Pommy Penguin Transformation": BombTSALocationData(
        region="Menu",
        address=0x1C3054,
    ),
    "Pommy Beast Transformation": BombTSALocationData(
        region="Menu",
        address=0x1C3055,
    ),
    "Pommy Mage Transformation": BombTSALocationData(
        region="Menu",
        address=0x1C3056,
    ),
    "Pommy Knight Transformation": BombTSALocationData(
        region="Menu",
        address=0x1C3057,
    ),
    "Pommy Devil Transformation": BombTSALocationData(
        region="Menu",
        address=0x1C3058,
    ),
    "Pommy Cat Transformation": BombTSALocationData(
        region="Menu",
        address=0x1C3059,
    ),
    "Pommy Bird Transformation": BombTSALocationData(
        region="Menu",
        address=0x1C305A,
    ),
    "Pommy Chicken Transformation": BombTSALocationData(
        region="Menu",
        address=0x1C305B,
    ),
    "Pommy Dragon Transformation": BombTSALocationData(
        region="Menu",
        address=0x1C305C,
    ),
    "Pommy Dinosaur Transformation": BombTSALocationData(
        region="Menu",
        address=0x1C305D,
    ),
    "Pommy Pixie Transformation": BombTSALocationData(
        region="Menu",
        address=0x1C305E,
    ),
    "Pommy Shadow Transformation": BombTSALocationData(
        region="Menu",
        address=0x1C305F,
    ),


}
shop_data_table: Dict[str, BombTSALocationData] = {
    #"Shop Heart 1": BombTSALocationData(
    #    region="Shop",
    #    address=0x1C3081,
    #),
    #"Shop Heart 2": BombTSALocationData(
    #    region="Shop",
    #    address=0x1C3082,
    #),
    #"Shop Heart 3": BombTSALocationData(
    #    region="Shop",
    #    address=0x1C3083,
    #),
    #"Shop Heart 4": BombTSALocationData(
    #    region="Shop",
    #    address=0x1C3084,
    #),
    #"Shop Heart 5": BombTSALocationData(
    #    region="Shop",
    #    address=0x1C3085,
    #),
    #"Shop Full Power": BombTSALocationData(
    #    region="Shop",
    #    address=0x1C3086,
    #),
    "Shop Battle A": BombTSALocationData(
        region="Shop",
        address=0x1C308A,
    ),
    "Shop Battle B": BombTSALocationData(
        region="Shop",
        address=0x1C308B,
    ),
    "Shop Battle C": BombTSALocationData(
        region="Shop",
        address=0x1C308C,
    ),
    "Shop Battle D": BombTSALocationData(
        region="Shop",
        address=0x1C308D,
    ),


    "Shop Part Beard": BombTSALocationData(
        region="Shop",
        address=0x1C3090,
    ),
    "Shop Part Tank": BombTSALocationData(
        region="Shop",
        address=0x1C3091,
    ),
    "Shop Part Fan": BombTSALocationData(
        region="Shop",
        address=0x1C3092,
    ),
    "Shop Part Bigfoot Shoes": BombTSALocationData(
        region="Shop",
        address=0x1C3093,
    ),
    "Shop Part Topknot": BombTSALocationData(
        region="Shop",
        address=0x1C3094,
    ),
    "Shop Part Kimono": BombTSALocationData(
        region="Shop",
        address=0x1C3095,
    ),
    "Shop Part Sword": BombTSALocationData(
        region="Shop",
        address=0x1C3096,
    ),
    "Shop Part Sandals": BombTSALocationData(
        region="Shop",
        address=0x1C3097,
    ),
    "Shop Part Cat Ears": BombTSALocationData(
        region="Shop Aquanet",
        address=0x1C3098,
    ),
    "Shop Part Cat Suit": BombTSALocationData(
        region="Shop Aquanet",
        address=0x1C3099,
    ),
    "Shop Part Cat Gloves": BombTSALocationData(
        region="Shop Aquanet",
        address=0x1C309A,
    ),
    "Shop Part Cat Slippers": BombTSALocationData(
        region="Shop Aquanet",
        address=0x1C309B,
    ),
    "Shop Part Headgear": BombTSALocationData(
        region="Shop Horizon",
        address=0x1C309C,
    ),
    "Shop Part Elephant Suit": BombTSALocationData(
        region="Shop Horizon",
        address=0x1C309D,
    ),
    "Shop Part Gloves": BombTSALocationData(
        region="Shop Horizon",
        address=0x1C309E,
    ),
    "Shop Part Kung Fu Shoes": BombTSALocationData(
        region="Shop Horizon",
        address=0x1C309F,
    ),
    "Shop Part Ribbon": BombTSALocationData(
        region="Shop Starlight",
        address=0x1C30A0,
    ),
    "Shop Part Pink Dress": BombTSALocationData(
        region="Shop Starlight",
        address=0x1C30A1,
    ),
    "Shop Part Slash Claws": BombTSALocationData(
        region="Shop Starlight",
        address=0x1C30A2,
    ),
    "Shop Part High Heels": BombTSALocationData(
        region="Shop Starlight",
        address=0x1C30A3,
    ),
    "Shop Part Rabbit Ears": BombTSALocationData(
        region="Shop Neverland",
        address=0x1C30A4,
    ),
    "Shop Part Duck Suit": BombTSALocationData(
        region="Shop Neverland",
        address=0x1C30A5,
    ),
    "Shop Part Drill": BombTSALocationData(
        region="Shop Neverland",
        address=0x1C30A6,
    ),
    "Shop Part Sneakers": BombTSALocationData(
        region="Shop Neverland",
        address=0x1C30A7,
    ),
    "Shop Part Bald Head": BombTSALocationData(
        region="Shop Epikyur",
        address=0x1C30A8,
    ),
    "Shop Part Apron": BombTSALocationData(
        region="Shop Epikyur",
        address=0x1C30A9,
    ),
    "Shop Part Hand Puppets": BombTSALocationData(
        region="Shop Epikyur",
        address=0x1C30AA,
    ),
    "Shop Part Pommy Slippers": BombTSALocationData(
        region="Shop Epikyur",
        address=0x1C30AB,
    ),
    "Shop Part Gold Helmet": BombTSALocationData(
        region="Shop Thantos",
        address=0x1C30AC,
    ),
    "Shop Part Gold Suit": BombTSALocationData(
        region="Shop Thantos",
        address=0x1C30AD,
    ),
    "Shop Part Gold Gloves": BombTSALocationData(
        region="Shop Thantos",
        address=0x1C30AE,
    ),
    "Shop Part Gold Boots": BombTSALocationData(
        region="Shop Thantos",
        address=0x1C30AF,
    ),

    # "Shop Hint Baelfael": BombTSALocationData(
        # region="Shop",
        # address=0x1C30B0,
    # ),
    # "Shop Hint Behemos": BombTSALocationData(
        # region="Shop",
        # address=0x1C30B1,
    # ),
    # "Shop Hint Ashtarth": BombTSALocationData(
        # region="Shop",
        # address=0x1C30B2,
    # ),
    # "Shop Hint Zhael": BombTSALocationData(
        # region="Shop Horizon",
        # address=0x1C30B3,
    # ),
    # "Shop Hint Molok": BombTSALocationData(
        # region="Shop Horizon",
        # address=0x1C30B4,
    # ),
    # "Shop Hint Zoniha": BombTSALocationData(
        # region="Shop Neverland",
        # address=0x1C30B5,
    # ),
    # "Shop Hint Epikyur": BombTSALocationData(
        # region="Epikyur",
        # address=0x1C30B6,
    # ),
    # "Shop Hint Bulzeeb": BombTSALocationData(
        # region="Shop Epikyur",
        # address=0x1C30B7,
    # ),
    # "Shop Hint Thantos 1": BombTSALocationData(
        # region="Thantos",
        # address=0x1C30B8,
    # ),
    # "Shop Hint Thantos 2": BombTSALocationData(
        # region="Thantos",
        # address=0x1C30B9,
    # ),
    # "Shop Hint Thantos 3": BombTSALocationData(
        # region="Thantos",
        # address=0x1C30BA,
    # ),
    # "Shop Hint Lilith": BombTSALocationData(
        # region="Shop Thantos",
        # address=0x1C30BB,
    # ),
    # "Shop Hint Rukifellth": BombTSALocationData(
        # region="Shop Thantos",
        # address=0x1C30BC,
    # ),
    # "Shop Hint Guardian Aquanet": BombTSALocationData(
        # region="Noah",
        # address=0x1C30BD,
    # ),
    # "Shop Hint Guardian Horizon": BombTSALocationData(
        # region="Noah",
        # address=0x1C30BE,
    # ),
    # "Shop Hint Guardian Starlight": BombTSALocationData(
        # region="Noah",
        # address=0x1C30BF,
    # ),
    # "Shop Hint Guardian Neverland": BombTSALocationData(
        # region="Noah",
        # address=0x1C30C0,
    # ),
    
}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
shop_location_table = {name: data.address for name, data in shop_data_table.items() if data.address is not None}
pommy_location_table = {name: data.address for name, data in pommy_data_table.items() if data.address is not None}
powerup_location_table = {name: data.address for name, data in powerup_data_table.items() if data.address is not None}

locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}
