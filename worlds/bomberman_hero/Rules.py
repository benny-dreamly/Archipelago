from typing import Callable, TYPE_CHECKING

from BaseClasses import CollectionState

if TYPE_CHECKING:
    from . import BombHWorld

STAGE_ITEMS = [
    "Battle Room",
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
    #"Innder Road",
    #"Vs Evil Bomber",
]

def get_region_rules(player):
    return {
        #"Garaden -> Vs Bagular":
        #    lambda state: state.has("Adok Bomb", player, 24),
        

        "Planet Bomber -> Hyper Room":
            lambda state: state.has("Hyper Room", player),
        "Planet Bomber -> Secret Room":
            lambda state: state.has("Secret Room", player),
        "Planet Bomber -> Heavy Room":
            lambda state: state.has("Heavy Room", player),
        "Planet Bomber -> Sky Room":
            lambda state: state.has("Sky Room", player),

        "Planet Bomber -> Blue Cave":
            lambda state: state.has("Blue Cave", player),
        "Planet Bomber -> Hole Lake":
            lambda state: state.has("Hole Lake", player),
        "Planet Bomber -> Red Cave":
            lambda state: state.has("Red Cave", player),
        "Planet Bomber -> Big Cannon":
            lambda state: state.has("Big Cannon", player),
        "Planet Bomber -> Dark Wood":
            lambda state: state.has("Dark Wood", player),
        "Planet Bomber -> Dragon Road":
            lambda state: state.has("Dragon Road", player),

        "Planet Bomber -> Vs Nitros Planet Bomber":
            lambda state: state.has("Vs Nitros Planet Bomber", player),
        "Planet Bomber -> Clown Valley":
            lambda state: state.has("Clown Valley", player),
        "Planet Bomber -> Great Rock":
            lambda state: state.has("Great Rock", player),
        "Planet Bomber -> Fog Route":
            lambda state: state.has("Fog Route", player),
        "Planet Bomber -> Vs Endol":
            lambda state: state.has("Vs Endol", player),


        "Primus -> Groog Hills":
            lambda state: state.has("Groog Hills", player),
        "Primus -> Bubble Hole":
            lambda state: state.has("Bubble Hole", player),
        "Primus -> Erars Lake":
            lambda state: state.has("Erars Lake", player),
        "Primus -> Waterway":
            lambda state: state.has("Waterway", player),
        "Primus -> Water Slider":
            lambda state: state.has("Water Slider", player),

        "Primus -> Rockn Road":
            lambda state: state.has("Rockn Road", player),
        "Primus -> Water Pool":
            lambda state: state.has("Water Pool", player),
        "Primus -> Millian Road":
            lambda state: state.has("Millian Road", player),
        "Primus -> Warp Room":
            lambda state: state.has("Warp Room", player),
        "Primus -> Dark Prison":
            lambda state: state.has("Dark Prison", player),
        "Primus -> Vs Nitros Primus":
            lambda state: state.has("Vs Nitros Primus", player),

        "Primus -> Killer Gate":
            lambda state: state.has("Killer Gate", player),
        "Primus -> Spiral Tower":
            lambda state: state.has("Spiral Tower", player),
        "Primus -> Snake Route":
            lambda state: state.has("Snake Route", player),
        "Primus -> Vs Baruda":
            lambda state: state.has("Vs Baruda", player),


        "Kanatia -> Hades Crater":
            lambda state: state.has("Hades Crater", player),
        "Kanatia -> Magma Lake":
            lambda state: state.has("Magma Lake", player),
        "Kanatia -> Magma Dam":
            lambda state: state.has("Magma Dam", player),
        "Kanatia -> Crysta Hole":
            lambda state: state.has("Crysta Hole", player),
        "Kanatia -> Emerald Tube":
            lambda state: state.has("Emerald Tube", player),

        "Kanatia -> Death Temple":
            lambda state: state.has("Death Temple", player),
        "Kanatia -> Death Road":
            lambda state: state.has("Death Road", player),
        "Kanatia -> Death Garden":
            lambda state: state.has("Death Garden", player),
        "Kanatia -> Float Zone":
            lambda state: state.has("Float Zone", player),
        "Kanatia -> Aqua Tank":
            lambda state: state.has("Aqua Tank", player),
        "Kanatia -> Aqua Way":
            lambda state: state.has("Aqua Way", player),
        "Kanatia -> Vs Nitros Kanatia":
            lambda state: state.has("Vs Nitros Kanatia", player),

        "Kanatia -> Hard Coaster":
            lambda state: state.has("Hard Coaster", player) and state.has("Bombup", player, ),
        "Kanatia -> Dark Maze":
            lambda state: state.has("Dark Maze", player),
        "Kanatia -> Mad Coaster":
            lambda state: state.has("Mad Coaster", player),
        "Kanatia -> Move Stone":
            lambda state: state.has("Move Stone", player),
        "Kanatia -> Vs Bolban":
            lambda state: state.has("Vs Bolban", player),
            
        "Mazone -> Hopper Land":
            lambda state: state.has("Hopper Land", player),
        "Mazone -> Junfalls":
            lambda state: state.has("Junfalls", player),
        "Mazone -> Freeze Lake":
            lambda state: state.has("Freeze Lake", player),
        "Mazone -> Cool Cave":
            lambda state: state.has("Cool Cave", player),

        "Mazone -> Snowland":
            lambda state: state.has("Snowland", player),
        "Mazone -> Storm Valley":
            lambda state: state.has("Storm Valley", player),
        "Mazone -> Snow Circuit":
            lambda state: state.has("Snow Circuit", player),
        "Mazone -> Heaven Sky":
            lambda state: state.has("Heaven Sky", player),
        "Mazone -> Eye Snake":
            lambda state: state.has("Eye Snake", player),

        "Mazone -> Vs Nitros Mazone":
            lambda state: state.has("Vs Nitros Mazone", player),
        "Mazone -> Air Room":
            lambda state: state.has("Air Room", player),
        "Mazone -> Zero G Room":
            lambda state: state.has("Zero G Room", player),
        "Mazone -> Mirror Room":
            lambda state: state.has("Mirror Room", player),
        "Mazone -> Vs Natia":
            lambda state: state.has("Vs Natia", player),

        "Garaden -> Boss Room 1":
            lambda state: state.has("Boss Room 1", player),
        "Garaden -> Boss Room 2":
            lambda state: state.has("Boss Room 2", player),
        "Garaden -> Boss Room 3":
            lambda state: state.has("Boss Room 3", player),
        "Garaden -> Boss Room 4":
            lambda state: state.has("Boss Room 4", player),
        "Garaden -> Boss Room 5":
            lambda state: state.has("Boss Room 5", player),
        "Garaden -> Boss Room 6":
            lambda state: state.has("Boss Room 6", player),

        #"Gossick -> Outter Road":
        #    lambda state: state.has("Outter Road", player),
        #"Gossick -> Inner Road":
        #    lambda state: state.has("Inner Road", player),
        #"Gossick -> Vs Evil Bomber":
        #    lambda state: state.has("Vs Evil Bomber", player),
 }      

def get_location_rules(player):
    return {
        "Heaven Sky Clear":
            lambda state: state.has("Bombup", player),
        "Heaven Sky Points":
            lambda state: state.has("Bombup", player),
        "Vs Endol Points":
            lambda state: state.has("Fireup", player, 3),
        "Vs Baruda Points":
            lambda state: state.has("Bombup", player, 2),
        "Vs Bolban Points":
            lambda state: state.has("Fireup", player, 2),
        "Vs Natia Clear":
            lambda state: state.has("Fireup", player, 3) and state.has("Healthup", player, 2),
        "Vs Natia Points":
            lambda state: state.has("Fireup", player, 3) and state.has("Healthup", player, 2),
        "Boss Room 2 Points":
            lambda state: state.has("Fireup", player, 3),
        "Boss Room 5 Clear":
            lambda state: state.has("Bombup", player, 1),
        "Boss Room 5 Points":
            lambda state: state.has("Bombup", player, 2),
        "Boss Room 6 Clear":
            lambda state: state.has("Fireup", player, 3),
        "Boss Room 6 Points":
            lambda state: state.has("Fireup", player, 3),
        "Aqua Way Points":
           lambda state: state.has("Bombup",player),
        "Freeze Lake Points":
            lambda state: state.has("Bombup",player, 3),
    
        "Crystals 1":
            lambda state: state.has_from_list(STAGE_ITEMS, player,5),
        "Crystals 2":
            lambda state: state.has_from_list(STAGE_ITEMS, player,10),
        "Crystals 3":
            lambda state: state.has_from_list(STAGE_ITEMS, player,20),
        "Crystals 4":
            lambda state: state.has_from_list(STAGE_ITEMS, player,30),
        "Crystals 5":
            lambda state: state.has_from_list(STAGE_ITEMS, player,40),
        "Crystals 6":
            lambda state: state.has_from_list(STAGE_ITEMS, player,45),
        "Crystals 7":
            lambda state: state.has_from_list(STAGE_ITEMS, player,50),
        "Crystals 8":
            lambda state: state.has_from_list(STAGE_ITEMS, player,55),
        "Crystals 9":
            lambda state: state.has_from_list(STAGE_ITEMS, player,60),
        "Crystals 10":
            lambda state: state.has_from_list(STAGE_ITEMS, player,65),
    }
