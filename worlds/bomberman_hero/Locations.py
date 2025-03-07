from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from . import BombHWorld

stage_names = [
    #"Battle Room",
    "Hyper Room",
    "Secret Room",
    "Heavy Room",
    "Sky Room",

    "Blue Cave",
    "Hole Lake",
    "Red Cave",
    "Big Cannon",
    "Dark Wood",
    "Dragon Road",
    "Vs Nitros Planet Bomber",

    "Clown Valley",
    "Great Rock",
    "Fog Route",
    "Vs Endol",

    "Groog Hills",
    "Bubble Hole",
    "Erars Lake",
    "Waterway",
    "Water Slider",

    "Rockn Road",
    "Water Pool",
    "Millian Road",
    "Warp Room",
    "Dark Prison",
    "Vs Nitros Primus",

    "Killer Gate",
    "Spiral Tower",
    "Snake Route",
    "Vs Baruda",

    "Hades Crater",
    "Magma Lake",
    "Magma Dam",
    "Crysta Hole",
    "Emerald Tube",

    "Death Temple",
    "Death Road",
    "Death Garden",
    "Float Zone",
    "Aqua Tank",
    "Aqua Way",
    "Vs Nitros Kanatia",

    "Hard Coaster",
    "Dark Maze",
    "Mad Coaster",
    "Move Stone",
    "Vs Bolban",

    "Hopper Land",
    "Junfalls",
    "Freeze Lake",
    "Cool Cave",
    "Snowland",

    "Storm Valley",
    "Snow Circuit",
    "Heaven Sky",
    "Eye Snake",

    "Vs Nitros Mazone",
    "Air Room",
    "Zero G Room",
    "Mirror Room",
    "Vs Natia",

    "Boss Room 1",
    "Boss Room 2",
    "Boss Room 3",
    "Boss Room 4",
    "Boss Room 5",
    "Boss Room 6",
    #"Vs Bagular",

    #"Outter Road",
    #"Inner Road",
    #"Vs Evil Bomber",

]


class BombHLocation(Location):
    game = "Bomberman Hero"


class BombHLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[["BombHWorld"], bool] = lambda world: True
    locked_item: Optional[str] = None




location_data_table: Dict[str, BombHLocationData] = {
 
    "Battle Room Clear": BombHLocationData(
        region="Battle Room",
        address=0x1348088,
    ),
    "Hyper Room Clear": BombHLocationData(
        region="Hyper Room",
        address=0x1348098,
    ),
    "Secret Room Clear": BombHLocationData(
        region="Secret Room",
        address=0x13480A8,
    ),
    "Heavy Room Clear": BombHLocationData(
        region="Heavy Room",
        address=0x13480B8,
    ),
    "Sky Room Clear": BombHLocationData(
        region="Sky Room",
        address=0x13480C8,
    ),

    "Blue Cave Clear": BombHLocationData(
        region="Blue Cave",
        address=0x13480F8,
    ),
    "Hole Lake Clear": BombHLocationData(
        region="Hole Lake",
        address=0x1348108,
    ),
    "Red Cave Clear": BombHLocationData(
        region="Red Cave",
        address=0x1348118,
    ),
    "Big Cannon Clear": BombHLocationData(
        region="Big Cannon",
        address=0x1348128,
    ),
    "Dark Wood Clear": BombHLocationData(
        region="Dark Wood",
        address=0x1348138,
    ),
    "Dragon Road Clear": BombHLocationData(
        region="Dragon Road",
        address=0x1348148,
    ),
    "Vs Nitros Planet Bomber Clear": BombHLocationData(
        region="Vs Nitros Planet Bomber",
        address=0x1348158,
    ),

    "Clown Valley Clear": BombHLocationData(
        region="Clown Valley",
        address=0x1348168,
    ),
    "Great Rock Clear": BombHLocationData(
        region="Great Rock",
        address=0x1348178,
    ),
    "Fog Route Clear": BombHLocationData(
        region="Fog Route",
        address=0x1348188,
    ),
    "Vs Endol Clear": BombHLocationData(
        region="Vs Endol",
        address=0x1348198,
    ),

    # Primus
    "Groog Hills Clear": BombHLocationData(
        region="Groog Hills",
        address=0x13481D8,
    ),
    "Bubble Hole Clear": BombHLocationData(
        region="Bubble Hole",
        address=0x13481E8,
    ),
    "Erars Lake Clear": BombHLocationData(
        region="Erars Lake",
        address=0x13481F8,
    ),
    "Waterway Clear": BombHLocationData(
        region="Waterway",
        address=0x1348208,
    ),
    "Water Slider Clear": BombHLocationData(
        region="Water Slider",
        address=0x1348218,
    ),

    "Rockn Road Clear": BombHLocationData(
        region="Rockn Road",
        address=0x1348248,
    ),
    "Water Pool Clear": BombHLocationData(
        region="Water Pool",
        address=0x1348258,
    ),
    "Millian Road Clear": BombHLocationData(
        region="Water Pool",
        address=0x1348268,
    ),
    "Warp Room Clear": BombHLocationData(
        region="Warp Room",
        address=0x1348278,
    ),
    "Dark Prison Clear": BombHLocationData(
        region="Dark Prison",
        address=0x1348288,
    ),
    "Vs Nitros Primus Clear": BombHLocationData(
        region="Vs Nitros Primus",
        address=0x1348298,
    ),

    "Killer Gate Clear": BombHLocationData(
        region="Killer Gate",
        address=0x13482B8,
    ),
    "Spiral Tower Clear": BombHLocationData(
        region="Spiral Tower",
        address=0x13482C8,
    ),
    "Snake Route Clear": BombHLocationData(
        region="Snake Route",
        address=0x13482D8,
    ),
    "Vs Baruda Clear": BombHLocationData(
        region="Vs Baruda",
        address=0x13482E8,
    ),

    # Kanatia
    "Hades Crater Clear": BombHLocationData(
        region="Hades Crater",
        address=0x1348328,
    ),
    "Magma Lake Clear": BombHLocationData(
        region="Magma Lake",
        address=0x1348338,
    ),
    "Magma Dam Clear": BombHLocationData(
        region="Magma Dam",
        address=0x1348348,
    ),
    "Crysta Hole Clear": BombHLocationData(
        region="Crysta Hole",
        address=0x1348358,
    ),
    "Emerald Tube Clear": BombHLocationData(
        region="Emerald Tube",
        address=0x1348368,
    ),

    "Death Temple Clear": BombHLocationData(
        region="Death Temple",
        address=0x1348398,
    ),
    "Death Road Clear": BombHLocationData(
        region="Death Road",
        address=0x13483A8,
    ),
    "Death Garden Clear": BombHLocationData(
        region="Death Garden",
        address=0x13483B8,
    ),
    "Float Zone Clear": BombHLocationData(
        region="Float Zone",
        address=0x13483C8,
    ),
    "Aqua Tank Clear": BombHLocationData(
        region="Aqua Tank",
        address=0x13483D8,
    ),
    "Aqua Way Clear": BombHLocationData(
        region="Aqua Way",
        address=0x13483E8,
    ),
    "Vs Nitros Kanatia Clear": BombHLocationData(
        region="Vs Nitros Kanatia",
        address=0x13483F8,
    ),

    "Hard Coaster Clear": BombHLocationData(
        region="Hard Coaster",
        address=0x1348408,
    ),
    "Dark Maze Clear": BombHLocationData(
        region="Dark Maze",
        address=0x1348418,
    ),
    "Mad Coaster Clear": BombHLocationData(
        region="Mad Coaster",
        address=0x1348428,
    ),
    "Move Stone Clear": BombHLocationData(
        region="Move Stone",
        address=0x1348438,
    ),
    "Vs Bolban Clear": BombHLocationData(
        region="Vs Bolban",
        address=0x1348448,
    ),

    # Mazone
    "Hopper Land Clear": BombHLocationData(
        region="Hopper Land",
        address=0x1348478,
    ),
    "Junfalls Clear": BombHLocationData(
        region="Junfalls",
        address=0x1348488,
    ),
    "Freeze Lake Clear": BombHLocationData(
        region="Freeze Lake",
        address=0x1348498,
    ),
    "Cool Cave Clear": BombHLocationData(
        region="Cool Cave",
        address=0x13484A8,
    ),

    "Snowland Clear": BombHLocationData(
        region="Snowland",
        address=0x13484E8,
    ),
    "Storm Valley Clear": BombHLocationData(
        region="Storm Valley",
        address=0x13484F8,
    ),
    "Snow Circuit Clear": BombHLocationData(
        region="Snow Circuit",
        address=0x1348508,
    ),
    "Heaven Sky Clear": BombHLocationData(
        region="Heaven Sky",
        address=0x1348518,
    ),
    "Eye Snake Clear": BombHLocationData(
        region="Eye Snake",
        address=0x1348528,
    ),

    "Vs Nitros Mazone Clear": BombHLocationData(
        region="Vs Nitros Mazone",
        address=0x1348558,
    ),
    "Air Room Clear": BombHLocationData(
        region="Air Room",
        address=0x1348568,
    ),
    "Zero G Room Clear": BombHLocationData(
        region="Zero G Room",
        address=0x1348578,
    ),
    "Mirror Room Clear": BombHLocationData(
        region="Mirror Room",
        address=0x1348588,
    ),
    "Vs Natia Clear": BombHLocationData(
        region="Vs Natia",
        address=0x1348598,
    ),

    #Garadan
    
    "Boss Room 1 Clear": BombHLocationData(
        region="Boss Room 1",
        address=0x13485C8,
    ),
    "Boss Room 2 Clear": BombHLocationData(
        region="Boss Room 2",
        address=0x13485D8,
    ),
    "Boss Room 3 Clear": BombHLocationData(
        region="Boss Room 3",
        address=0x13485E8,
    ),
    "Boss Room 4 Clear": BombHLocationData(
        region="Boss Room 4",
        address=0x13485F8,
    ),
    "Boss Room 5 Clear": BombHLocationData(
        region="Boss Room 5",
        address=0x1348608,
    ),
    "Boss Room 6 Clear": BombHLocationData(
        region="Boss Room 6",
        address=0x1348618,
    ),
    "Vs Bagular": BombHLocationData(
        region="Vs Bagular",
        address=0x1348628,
        locked_item="Disk"
    ),

    # Gossick
    #"Outter Road Clear": BombHLocationData(
    #    region="Outter Road",
    #    address=0x1348718,
    #),
    #"Inner Road Clear": BombHLocationData(
    #    region="Inner Road",
    #    address=0x1348728,
    #),
    #"Vs Evil Bomber Clear": BombHLocationData(
    #    region="Vs Evil Bomber",
    #    address=0x1348738,
    #),


    # Clear Points
    # Bomber Planet
    "Battle Room Points": BombHLocationData(
        region="Battle Room",
        address=0x1348089,
    ),
    "Hyper Room Points": BombHLocationData(
        region="Hyper Room",
        address=0x1348099,
    ),
    "Secret Room Points": BombHLocationData(
        region="Secret Room",
        address=0x13480A9,
    ),
    "Heavy Room Points": BombHLocationData(
        region="Heavy Room",
        address=0x13480B9,
    ),
    "Sky Room Points": BombHLocationData(
        region="Sky Room",
        address=0x13480C9,
    ),

    "Blue Cave Points": BombHLocationData(
        region="Blue Cave",
        address=0x13480F9,
    ),
    "Hole Lake Points": BombHLocationData(
        region="Hole Lake",
        address=0x1348109,
    ),
    "Red Cave Points": BombHLocationData(
        region="Red Cave",
        address=0x1348119,
    ),
    "Big Cannon Points": BombHLocationData(
        region="Big Cannon",
        address=0x1348129,
    ),
    "Dark Wood Points": BombHLocationData(
        region="Dark Wood",
        address=0x1348139,
    ),
    "Dragon Road Points": BombHLocationData(
        region="Dragon Road",
        address=0x1348149,
    ),
    "Vs Nitros Planet Bomber Points": BombHLocationData(
        region="Vs Nitros Planet Bomber",
        address=0x1348159,
    ),

    "Clown Valley Points": BombHLocationData(
        region="Clown Valley",
        address=0x1348169,
    ),
    "Great Rock Points": BombHLocationData(
        region="Great Rock",
        address=0x1348179,
    ),
    "Fog Route Points": BombHLocationData(
        region="Fog Route",
        address=0x1348189,
    ),
    "Vs Endol Points": BombHLocationData(
        region="Vs Endol",
        address=0x1348199,
    ),

    # Primus
    "Groog Hills Points": BombHLocationData(
        region="Groog Hills",
        address=0x13481D9,
    ),
    "Bubble Hole Points": BombHLocationData(
        region="Bubble Hole",
        address=0x13481E9,
    ),
    "Erars Lake Points": BombHLocationData(
        region="Erars Lake",
        address=0x13481F9,
    ),
    "Waterway Points": BombHLocationData(
        region="Waterway",
        address=0x1348209,
    ),
    "Water Slider Points": BombHLocationData(
        region="Water Slider",
        address=0x1348219,
    ),

    "Rockn Road Points": BombHLocationData(
        region="Rockn Road",
        address=0x1348249,
    ),
    "Water Pool Points": BombHLocationData(
        region="Water Pool",
        address=0x1348259,
    ),
    "Millian Road Points": BombHLocationData(
        region="Water Pool",
        address=0x1348269,
    ),
    "Warp Room Points": BombHLocationData(
        region="Warp Room",
        address=0x1348279,
    ),
    "Dark Prison Points": BombHLocationData(
        region="Dark Prison",
        address=0x1348289,
    ),
    "Vs Nitros Primus Points": BombHLocationData(
        region="Vs Nitros Primus",
        address=0x1348299,
    ),

    "Killer Gate Points": BombHLocationData(
        region="Killer Gate",
        address=0x13482B9,
    ),
    "Spiral Tower Points": BombHLocationData(
        region="Spiral Tower",
        address=0x13482C9,
    ),
    "Snake Route Points": BombHLocationData(
        region="Snake Route",
        address=0x13482D9,
    ),
    "Vs Baruda Points": BombHLocationData(
        region="Vs Baruda",
        address=0x13482E9,
    ),

    # Kanatia
    "Hades Crater Points": BombHLocationData(
        region="Hades Crater",
        address=0x1348329,
    ),
    "Magma Lake Points": BombHLocationData(
        region="Magma Lake",
        address=0x1348339,
    ),
    "Magma Dam Points": BombHLocationData(
        region="Magma Dam",
        address=0x1348349,
    ),
    "Crysta Hole Points": BombHLocationData(
        region="Crysta Hole",
        address=0x1348359,
    ),
    #"Emerald Tube Points": BombHLocationData(
    #    region="Emerald Tube",
    #    address=0x1348369,
    #),

    "Death Temple Points": BombHLocationData(
        region="Death Temple",
        address=0x1348399,
    ),
    "Death Road Points": BombHLocationData(
        region="Death Road",
        address=0x13483A9,
    ),
    "Death Garden Points": BombHLocationData(
        region="Death Garden",
        address=0x13483B9,
    ),
    "Float Zone Points": BombHLocationData(
        region="Float Zone",
        address=0x13483C9,
    ),
    "Aqua Tank Points": BombHLocationData(
        region="Aqua Tank",
        address=0x13483D9,
    ),
    "Aqua Way Points": BombHLocationData(
        region="Aqua Way",
        address=0x13483E9,
    ),
    "Vs Nitros Kanatia Points": BombHLocationData(
        region="Vs Nitros Kanatia",
        address=0x13483F9,
    ),

    "Hard Coaster Points": BombHLocationData(
        region="Hard Coaster",
        address=0x1348409,
    ),
    "Dark Maze Points": BombHLocationData(
        region="Dark Maze",
        address=0x1348419,
    ),
    "Mad Coaster Points": BombHLocationData(
        region="Mad Coaster",
        address=0x1348429,
    ),
    "Move Stone Points": BombHLocationData(
        region="Move Stone",
        address=0x1348439,
    ),
    "Vs Bolban Points": BombHLocationData(
        region="Vs Bolban",
        address=0x1348449,
    ),

    # Mazone
    "Hopper Land Points": BombHLocationData(
        region="Hopper Land",
        address=0x1348479,
    ),
    "Junfalls Points": BombHLocationData(
        region="Junfalls",
        address=0x1348489,
    ),
    "Freeze Lake Points": BombHLocationData(
        region="Freeze Lake",
        address=0x1348499,
    ),
    "Cool Cave Points": BombHLocationData(
        region="Cool Cave",
        address=0x13484A9,
    ),

    "Snowland Points": BombHLocationData(
        region="Snowland",
        address=0x13484E9,
    ),
    "Storm Valley Points": BombHLocationData(
        region="Storm Valley",
        address=0x13484F9,
    ),
    "Snow Circuit Points": BombHLocationData(
        region="Snow Circuit",
        address=0x1348509,
    ),
    "Heaven Sky Points": BombHLocationData(
        region="Heaven Sky",
        address=0x1348519,
    ),
    "Eye Snake Points": BombHLocationData(
        region="Eye Snake",
        address=0x1348529,
    ),

    "Vs Nitros Mazone Points": BombHLocationData(
        region="Vs Nitros Mazone",
        address=0x1348559,
    ),
    "Air Room Points": BombHLocationData(
        region="Air Room",
        address=0x1348569,
    ),
    "Zero G Room Points": BombHLocationData(
        region="Zero G Room",
        address=0x1348579,
    ),
    "Mirror Room Points": BombHLocationData(
        region="Mirror Room",
        address=0x1348589,
    ),
    "Vs Natia Points": BombHLocationData(
        region="Vs Natia",
        address=0x1348599,
    ),

    #Garadan
    
    "Boss Room 1 Points": BombHLocationData(
        region="Boss Room 1",
        address=0x13485C9,
    ),
    "Boss Room 2 Points": BombHLocationData(
        region="Boss Room 2",
        address=0x13485D9,
    ),
    "Boss Room 3 Points": BombHLocationData(
        region="Boss Room 3",
        address=0x13485E9,
    ),
    "Boss Room 4 Points": BombHLocationData(
        region="Boss Room 4",
        address=0x13485F9,
    ),
    "Boss Room 5 Points": BombHLocationData(
        region="Boss Room 5",
        address=0x1348609,
    ),
    "Boss Room 6 Points": BombHLocationData(
        region="Boss Room 6",
        address=0x1348619,
    ),

    # Gossick
    #"Outter Road Points": BombHLocationData(
    #    region="Outter Road",
    #    address=0x1348719,
    #),
    #"Inner Road Points": BombHLocationData(
    #    region="Inner Road",
    #    address=0x1348729,
    #),
    #"Evil Bomber Points": BombHLocationData(
    #    region="Vs Evil Bomber",
    #    address=0x1348739,
    #),

    # Adok Bombs

    "Heavy Room Adok Bomb": BombHLocationData(
        region="Heavy Room",
        address=0x574950,
    ),
    "Sky Room Adok Bomb": BombHLocationData(
        region="Sky Room",
        address=0x574951,
    ),
    "Dark Wood Adok Bomb": BombHLocationData(
        region="Dark Wood",
        address=0x574952,
    ),
    "Dragon Road Adok Bomb": BombHLocationData(
        region="Dragon Road",
        address=0x574953,
    ),
    "Clown Valley Adok Bomb": BombHLocationData(
        region="Clown Valley",
        address=0x574954,
    ),
    "Great Rock Adok Bomb": BombHLocationData(
        region="Great Rock",
        address=0x574955,
    ),
    "Bubble Hole Adok Bomb": BombHLocationData(
        region="Bubble Hole",
        address=0x574956,
    ),
    "Water Slider Adok Bomb": BombHLocationData(
        region="Water Slider",
        address=0x574957,
    ),

    "Water Pool Adok Bomb": BombHLocationData(
        region="Water Pool",
        address=0x574960,
    ),
    "Warp Room Adok Bomb": BombHLocationData(
        region="Warp Room",
        address=0x574961,
    ),
    "Killer Gate Adok Bomb": BombHLocationData(
        region="Killer Gate",
        address=0x574962,
    ),
    "Spiral Tower Adok Bomb": BombHLocationData(
        region="Spiral Tower",
        address=0x574963,
    ),
    "Magma Dam Adok Bomb": BombHLocationData(
        region="Magma Dam",
        address=0x574964,
    ),
    "Crysta Hole Adok Bomb": BombHLocationData(
        region="Crysta Hole",
        address=0x574965,
    ),
    "Death Garden Adok Bomb": BombHLocationData(
        region="Death Garden",
        address=0x574966,
    ),
    "Float Zone Adok Bomb": BombHLocationData(
        region="Float Zone",
        address=0x574967,
    ),

    "Hard Coaster Adok Bomb": BombHLocationData(
        region="Hard Coaster",
        address=0x574970,
    ),
    "Dark Maze Adok Bomb": BombHLocationData(
        region="Dark Maze",
        address=0x574971,
    ),
    "Junfalls Adok Bomb": BombHLocationData(
        region="Junfalls",
        address=0x574972,
    ),
    "Cool Cave Adok Bomb": BombHLocationData(
        region="Cool Cave",
        address=0x574973,
    ),
    "Snowland Adok Bomb": BombHLocationData(
        region="Snowland",
        address=0x574974,
    ),
    "Heaven Sky Adok Bomb": BombHLocationData(
        region="Heaven Sky",
        address=0x574975,
    ),
    "Air Room Adok Bomb": BombHLocationData(
        region="Air Room",
        address=0x574976,
    ),
    "Zero G Room Adok Bomb": BombHLocationData(
        region="Zero G Room",
        address=0x574977,
    ),

}
gem_data_table: Dict[str, BombHLocationData] = {
    "Crystals 1": BombHLocationData(
        region="Planet Bomber",
        address=0x1348061,
    ),
    "Crystals 2": BombHLocationData(
        region="Planet Bomber",
        address=0x1348062,
    ),
    "Crystals 3": BombHLocationData(
        region="Planet Bomber",
        address=0x1348063,
    ),
    "Crystals 4": BombHLocationData(
        region="Planet Bomber",
        address=0x1348064,
    ),
    "Crystals 5": BombHLocationData(
        region="Planet Bomber",
        address=0x1348065,
    ),
    "Crystals 6": BombHLocationData(
        region="Planet Bomber",
        address=0x1348066,
    ),
    "Crystals 7": BombHLocationData(
        region="Planet Bomber",
        address=0x1348067,
    ),
    "Crystals 8": BombHLocationData(
        region="Planet Bomber",
        address=0x1348068,
    ),
    "Crystals 9": BombHLocationData(
        region="Planet Bomber",
        address=0x1348069,
    ),
    "Crystals 10": BombHLocationData(
        region="Planet Bomber",
        address=0x134806A,
    ),
}
radio_data_table: Dict[str, BombHLocationData] = {
    "Battle Room Radio Entrance": BombHLocationData(
        region="Battle Room",
        address=0x134808A,
    ),
    "Battle Room Radio Platform": BombHLocationData(
        region="Battle Room",
        address=0x134808B,
    ),
    "Battle Room Radio Switch": BombHLocationData(
        region="Battle Room",
        address=0x134808C,
    ),
    "Hyper Room Radio Entrance": BombHLocationData(
        region="Hyper Room",
        address=0x134809A,
    ),
    "Hyper Room Radio Door": BombHLocationData(
        region="Hyper Room",
        address=0x134809B,
    ),
    "Secret Room Radio Entrance": BombHLocationData(
        region="Secret Room",
        address=0x13480AA,
    ),
    "Heavy Room Radio Entrance": BombHLocationData(
        region="Heavy Room",
        address=0x13480BA,
    ),
    "Heavy Room Radio Barrier Tower": BombHLocationData(
        region="Heavy Room",
        address=0x13480BB,
    ),
    "Sky Room Radio Entrance": BombHLocationData(
        region="Sky Room",
        address=0x13480CA,
    ),
    "Red Cave Radio Lower Path": BombHLocationData(
        region="Red Cave",
        address=0x134811A,
    ),
    "Dark Wood Radio Entrance": BombHLocationData(
        region="Dark Wood",
        address=0x134813A,
    ),
    "Groog Hills Radio Entrance": BombHLocationData(
        region="Groog Hills",
        address=0x13481DA,
    ),
    "Groog Hills Radio Right Big Tree": BombHLocationData(
        region="Groog Hills",
        address=0x13481DB,
    ),
    "Groog Hills Radio Freeze Flower": BombHLocationData(
        region="Groog Hills",
        address=0x13481DC,
    ),
    "Bubble Hole Radio Entrance": BombHLocationData(
        region="Bubble Hole",
        address=0x13481EA,
    ),
    "Erars Lake Radio Entrance": BombHLocationData(
        region="Erars Lake",
        address=0x13481FA,
    ),
    "Dark Prison Radio Entrance": BombHLocationData(
        region="Dark Prison",
        address= 0x134828A,
    ),
    "Killer Gate Radio Entrance": BombHLocationData(
        region="Killer Gate",
        address=0x13482BA,
    ),
    "Hades Crater Radio Entrance": BombHLocationData(
        region="Hades Crater",
        address=0x134832A,
    ),
    "Magma Dam Radio Entrance": BombHLocationData(
        region="Magma Dam",
        address=0x134833A,
    ),
    "Magma Dam Radio Left Dam": BombHLocationData(
        region="Magma Dam",
        address=0x134833B,
    ),
    "Float Zone Radio Entrance": BombHLocationData(
        region="Float Zone",
        address=0x13483CA,
    ),
    "Aqua Tank Radio Entrance": BombHLocationData(
        region="Aqua Tank",
        address=0x13483DA,
    ),
    "Hard Coaster Radio Green Warp": BombHLocationData(
        region="Hard Coaster",
        address=0x134840A,
    ),
    "Move Stone Radio Entrance": BombHLocationData(
        region="Move Stone",
        address=0x134843A,
    ),
    "Hopper Land Radio Entrance": BombHLocationData(
        region="Hopper Land",
        address=0x134847A,
    ),
    "Storm Valley Radio Entrance": BombHLocationData(
        region="Storm Valley",
        address=0x13484FA,
    ),
    "Zero G Room Radio Switch": BombHLocationData(
        region="Zero G Room",
        address=0x134857A,
    ),
    "Mirror Room Radio Entrance": BombHLocationData(
        region="Mirror Room",
        address=0x134858A,
    ),
    "Mirror Room Radio Right Ramp": BombHLocationData(
        region="Mirror Room",
        address=0x134858B,
    ),

}


location_table =   {name: data.address for name, data in location_data_table.items() if data.address is not None}
radio_name_table = {name: data.address for name, data in radio_data_table.items() if data.address is not None}
gem_name_table =   {name: data.address for name, data in gem_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}
