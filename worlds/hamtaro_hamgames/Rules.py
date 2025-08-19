from typing import Callable, TYPE_CHECKING

from BaseClasses import CollectionState

if TYPE_CHECKING:
    from . import HamGamesWorld

def non_day_one(state, player):
    return state.has("Day 2", player) or state.has("Day 3", player) or state.has("Day 4", player) or state.has("Day 5", player) or state.has("Day 6", player)

def have_everything(state, player):
    return \
    state.has("Day 2", player) and \
    state.has("Day 3", player) and \
    state.has("Day 4", player) and \
    state.has("Day 5", player) and \
    state.has("Day 6", player) and \
    state.has("Beach Pass", player) and \
    state.has("Tennis Pass", player) and \
    state.has("Pool Pass", player) and \
    state.has("Stadium Pass", player) and \
    state.has("Lawn Pass", player)

def have_all_passes(state,player):
    return \
    state.has("Beach Pass", player) and \
    state.has("Tennis Pass", player) and \
    state.has("Pool Pass", player) and \
    state.has("Stadium Pass", player) and \
    state.has("Lawn Pass", player) and \
    state.has("Village Pass", player) and  \
    state.has("Studio Pass", player)

def have_all_days(state, player):
    return \
    state.has("Day 2", player) and \
    state.has("Day 3", player) and \
    state.has("Day 4", player) and \
    state.has("Day 5", player) and \
    state.has("Day 6", player)

def get_region_rules(player,fortune_area):
    fortune_conversion = {
        0xAB: "Studio Pass",
        0xAC: "Studio Pass",
        0xAD: "Village Pass",
        0xAE: "Stadium Pass",
        0xAF: "Stadium Pass",
        0xB0: "Tennis Pass",
        0xB1: "Tennis Pass",
        0xB2: "Beach Pass",
        0xB3: "Beach Pass",
        0xB4: "Lawn Pass",
        0xB5: "Lawn Pass",
        0xB6: "Pool Pass",
        0xB7: "Pool Pass",
    }
    return {
        "Menu -> Day 2":
            lambda state: state.has("Day 2", player),
        "Menu -> Day 3":
            lambda state: state.has("Day 3", player),
        "Menu -> Day 4":
            lambda state: state.has("Day 4", player),
        "Menu -> Day 5":
            lambda state: state.has("Day 5", player),
        "Menu -> Day 6":
            lambda state: state.has("Day 6", player),
        "Menu -> Day 7":
            lambda state: have_all_passes(state,player) and have_all_days(state, player),
        
        "Menu -> Hamigo":
            lambda state: state.has("Hamigo File",player),
        "Menu -> TV Shop":
            lambda state: state.has("Day 2", player),
        "TV Shop -> TV Shop Latenight":
            lambda state: state.has("Hamigo File", player),
        "Menu -> Fortune Teller":
            lambda state: state.has("Day 2", player) and state.has(fortune_conversion[fortune_area], player),

        "Day 1 -> Day 1 - Studio":
            lambda state: state.has("Studio Pass", player),
        "Day 1 -> Day 1 - Beach":
            lambda state: state.has("Beach Pass", player),
        "Day 1 -> Day 1 - Tennis":
            lambda state: state.has("Tennis Pass", player),
        "Day 1 -> Day 1 - Village":
            lambda state: state.has("Village Pass", player),
        "Day 1 -> Day 1 - Pool":
            lambda state: state.has("Pool Pass", player),
        "Day 1 -> Day 1 - Stadium":
            lambda state: state.has("Stadium Pass", player),
        "Day 1 -> Day 1 - Lawn":
            lambda state: state.has("Lawn Pass", player),

        "Day 2 -> Day 2 - Studio":
            lambda state: state.has("Studio Pass", player),
        "Day 2 -> Day 2 - Beach":
            lambda state: state.has("Beach Pass", player),
        "Day 2 -> Day 2 - Tennis":
            lambda state: state.has("Tennis Pass", player),
        "Day 2 -> Day 2 - Village":
            lambda state: state.has("Village Pass", player),
        "Day 2 -> Day 2 - Pool":
            lambda state: state.has("Pool Pass", player),
        "Day 2 -> Day 2 - Stadium":
            lambda state: state.has("Stadium Pass", player),
        "Day 2 -> Day 2 - Lawn":
            lambda state: state.has("Lawn Pass", player),
            
        "Day 3 -> Day 3 - Studio":
            lambda state: state.has("Studio Pass", player),
        "Day 3 -> Day 3 - Beach":
            lambda state: state.has("Beach Pass", player),
        "Day 3 -> Day 3 - Tennis":
            lambda state: state.has("Tennis Pass", player),
        "Day 3 -> Day 3 - Village":
            lambda state: state.has("Village Pass", player),
        "Day 3 -> Day 3 - Pool":
            lambda state: state.has("Pool Pass", player),
        "Day 3 -> Day 3 - Stadium":
            lambda state: state.has("Stadium Pass", player),
        "Day 3 -> Day 3 - Lawn":
            lambda state: state.has("Lawn Pass", player),

        "Day 4 -> Day 4 - Studio":
            lambda state: state.has("Studio Pass", player),
        "Day 4 -> Day 4 - Beach":
            lambda state: state.has("Beach Pass", player),
        "Day 4 -> Day 4 - Tennis":
            lambda state: state.has("Tennis Pass", player), 
        "Day 4 -> Day 4 - Village":
            lambda state: state.has("Village Pass", player),
        "Day 4 -> Day 4 - Pool":
            lambda state: state.has("Pool Pass", player),   
        "Day 4 -> Day 4 - Stadium":
            lambda state: state.has("Stadium Pass", player),
        "Day 4 -> Day 4 - Lawn":
            lambda state: state.has("Lawn Pass", player),

        "Day 5 -> Day 5 - Studio":
            lambda state: state.has("Studio Pass", player),
        "Day 5 -> Day 5 - Beach":
            lambda state: state.has("Beach Pass", player),
        "Day 5 -> Day 5 - Tennis":
            lambda state: state.has("Tennis Pass", player),
        "Day 5 -> Day 5 - Village":
            lambda state: state.has("Village Pass", player),
        "Day 5 -> Day 5 - Pool":
            lambda state: state.has("Pool Pass", player),
        "Day 5 -> Day 5 - Stadium":
            lambda state: state.has("Stadium Pass", player),
        "Day 5 -> Day 5 - Lawn":
            lambda state: state.has("Lawn Pass", player),

        "Day 6 -> Day 6 - Studio":
            lambda state: state.has("Studio Pass", player),
        "Day 6 -> Day 6 - Beach":
            lambda state: state.has("Beach Pass", player),
        "Day 6 -> Day 6 - Tennis":
            lambda state: state.has("Tennis Pass", player),
        "Day 6 -> Day 6 - Village":
            lambda state: state.has("Village Pass", player),
        "Day 6 -> Day 6 - Pool":
            lambda state: state.has("Pool Pass", player),
        "Day 6 -> Day 6 - Stadium":
            lambda state: state.has("Stadium Pass", player),
        "Day 6 -> Day 6 - Lawn":
            lambda state: state.has("Lawn Pass", player),

        "Day 7 -> Day 7 - Studio":
            lambda state: state.has("Studio Pass", player),
        "Day 7 -> Day 7 - Beach":
            lambda state: state.has("Beach Pass", player),
        "Day 7 -> Day 7 - Tennis":
            lambda state: state.has("Tennis Pass", player),
        "Day 7 -> Day 7 - Village":
            lambda state: state.has("Village Pass", player),
        "Day 7 -> Day 7 - Pool":
            lambda state: state.has("Pool Pass", player),
        "Day 7 -> Day 7 - Stadium":
            lambda state: state.has("Stadium Pass", player),
        "Day 7 -> Day 7 - Lawn":
            lambda state: state.has("Lawn Pass", player),
        

    }

def get_location_rules(player):
    area_items = [
        "Studio Pass",
        "Beach Pass",
        "Tennis Pass",
        "Village Pass",
        "Pool Pass",
        "Stadium Pass",
        "Lawn Pass"
    ]
    day_items = [
        "Day 2",
        "Day 3",
        "Day 4",
        "Day 5",
        "Day 6"
    ]
    rules = {
        "Day 4 Tennis - Tennis Final Gold Medal":
            lambda state: state.has("Day 2", player),
        "Day 4 Tennis - Tennis Final Silver Medal":
            lambda state: state.has("Day 2", player),
        "Day 6 Beach - Beach Volleyball Final Gold Medal":
            lambda state: state.has("Day 3", player),
        "Day 6 Beach - Beach Volleyball Final Silver Medal":
            lambda state: state.has("Day 3", player),
        "Hamigo 2 - Boss":
            lambda state: state.has("Stadium Pass", player) or state.has("Village Pass", player),
        "Hamigo 3 - Oxnard":
            lambda state: state.has("Stadium Pass", player) or state.has("Village Pass", player),
        "Hamigo 4 - Cappy":
            lambda state: state.has("Stadium Pass", player) or state.has("Village Pass", player),
        "Hamigo 5 - Pashmina":
            lambda state: (state.has("Stadium Pass", player) or state.has("Village Pass", player)) or
            (state.has("Day 2",player)),
        "Hamigo 6 - Penelope":
            lambda state: (state.has("Stadium Pass", player) or state.has("Village Pass", player)) or 
            (state.has("Day 2",player)),
        "Hamigo 7 - Prince Bo":
            lambda state: have_all_passes(state,player) and have_all_days(state,player),
        "Hamigo 8 - Daisy":
            lambda state: state.has("Stadium Pass", player) or state.has("Village Pass", player),
        "Hamigo 9 - Ivy":
            lambda state: state.has("Tennis Pass", player) or state.has("Village Pass", player),
        "Hamigo 10 - Rosy":
            lambda state: state.has("Tennis Pass", player) or state.has("Village Pass", player),
        "Hamigo 11 - Hamstern":
            lambda state: state.has("Village Pass", player),
        "Hamigo 12 - Hamberto":
            lambda state: state.has("Beach Pass", player) or state.has("Village Pass", player),
        "Hamigo 13 - Cubbie":
            lambda state: state.has("Village Pass", player),
        "Hamigo 14 - Hambone":
            lambda state: state.has("Beach Pass", player) or state.has("Village Pass", player),
        "Hamigo 15 - Hambeard":
            lambda state: state.has("Beach Pass", player) or state.has("Village Pass", player),
        "Hamigo 16 - Leo":
            lambda state: state.has("Lawn Pass", player) or state.has("Village Pass", player),
        "Hamigo 17 - Stripes":
            lambda state: state.has("Village Pass", player),
        "Hamigo 18 - Bunny":
            lambda state: state.has("Lawn Pass", player) or state.has("Village Pass", player),
        "Hamigo 19 - Warts":
            lambda state: state.has("Lawn Pass", player) or state.has("Village Pass", player),
        "Hamigo 20 - Maxwell":
            lambda state: state.has("Tennis Pass", player),
        "Hamigo 21 - Howdy":
            lambda state: state.has("Stadium Pass", player),
        # "Hamigo 22 - Dexter":
        # "Hamigo 23 - Panda":
        # "Hamigo 24 - Stan":
        # "Hamigo 25 - Sandy":
        # "Hamigo 26 - Snoozer":
        "Hamigo 27 - Jingle":
            lambda state: state.has("Studio Pass", player),
        "Hamigo 28 - Lapis":
            lambda state: state.has("Tennis Pass", player),
        "Hamigo 29 - Lazuli":
            lambda state: state.has("Tennis Pass", player),
        "Hamigo 30 - Bomegrante":
            lambda state: state.has("Studio Pass", player) and non_day_one(state, player),
        "Hamigo 31 - Borange":
            lambda state: state.has("Studio Pass", player) and non_day_one(state, player),
        "Hamigo 32 - Bopaya":
            lambda state: state.has("Studio Pass", player) and non_day_one(state, player),
        "Hamigo 33 - Bolime":
            lambda state: state.has("Studio Pass", player) and non_day_one(state, player),
        "Hamigo 34 - Boberry":
            lambda state: state.has("Studio Pass", player) and non_day_one(state, player),
        "Hamigo 35 - Bogrape":
            lambda state: state.has("Studio Pass", player) and non_day_one(state, player),
        "Hamigo 36 - Boplum":
            lambda state: state.has("Studio Pass", player) and non_day_one(state, player),
        "Hamigo 37 - Dewey":
            lambda state: state.has("Beach Pass", player) and non_day_one(state, player) and state.has("Tennis Pass", player),
        "Hamigo 38 - Crystal":
            lambda state: state.has("Beach Pass", player) and non_day_one(state, player) and state.has("Tennis Pass", player),
        "Hamigo 39 - Robo-Joe":
            lambda state: state.has("Tennis Pass", player) and state.has("Stadium Pass", player),
        "Hamigo 40 - Flora":
            lambda state: state.has("Village Pass", player) and non_day_one(state, player),
        "Hamigo 41 - Sparkle":
            lambda state: have_all_days(state, player) and have_all_days(state, player),
        "Hamigo 42 - DJ":
            lambda state: state.has("Studio Pass", player) and non_day_one(state, player),
        "Hamigo 43 - Omar":
            lambda state: have_all_passes(state, player) and state.has("Day 4", player),
        "Hamigo 44 - Hamstarr":
            lambda state: state.has("Studio Pass", player) and non_day_one(state, player),
        "Hamigo 45 - Djungarian Chorus":
            lambda state: have_all_passes(state, player) and have_all_days(state,player),
        "Hamigo 46 - Postie":
            lambda state: non_day_one(state, player),
        "Hamigo 47 - Carrobo":
            lambda state: state.has("Lawn Pass", player) and state.has("Day 4", player),
        "Hamigo 48 - Ninham":
            lambda state: state.has("Tennis Pass", player) and (state.has("Day 2", player) or state.has("Day 4", player)),
        "Hamigo 49 - Stucky":
            lambda state: state.has("Stadium Pass", player) and state.has("Day 3", player),
        "Hamigo 50 - Mister Matsu":
            lambda state: state.has("Studio Pass", player),

        "TV Shop - Raccoon Costume":
            lambda state: state.has_from_list(area_items, player,2),
        "TV Shop - Withered Tree Costume":
            lambda state: state.has_from_list(area_items, player,2) and state.has_from_list(day_items, player,2),
        "TV Shop - Ant Costume":
            lambda state: state.has_from_list(area_items, player,3) and state.has_from_list(day_items, player,2),
        "TV Shop - Scallop Costume":
            lambda state: state.has_from_list(area_items, player,3) and state.has_from_list(day_items, player,2),
        "TV Shop - Polar Bear Costume":
            lambda state: state.has_from_list(area_items, player,4) and state.has_from_list(day_items, player,3),
        "TV Shop - Swan Costume":
            lambda state: state.has_from_list(area_items, player,4) and state.has_from_list(day_items, player,3),
        "TV Shop - Armadillo Costume":
            lambda state: state.has_from_list(area_items, player,5) and state.has_from_list(day_items, player,3),
        "TV Shop - Cat Costume":
            lambda state: state.has_from_list(area_items, player,5) and state.has_from_list(day_items, player,4),
        "TV Shop - Crab Costume":
            lambda state: state.has_from_list(area_items, player,6) and state.has_from_list(day_items, player,4),
        "TV Shop - Snowman Costume":
            lambda state: state.has_from_list(area_items, player,6) and state.has_from_list(day_items, player,4),
        "TV Shop - Fir Tree Costume":
            lambda state: state.has_from_list(area_items, player,7) and state.has_from_list(day_items, player,5),

        "TV Shop Late Night - Rose Costume":
            lambda state: state.has_from_list(area_items, player,4) and state.has_from_list(day_items, player,3),
        "TV Shop Late Night - Willow Tree Costume":
            lambda state: state.has_from_list(area_items, player,5) and state.has_from_list(day_items, player,3),
        "TV Shop Late Night - Bat Costume":
            lambda state: state.has_from_list(area_items, player,5) and state.has_from_list(day_items, player,4),
        "TV Shop Late Night - Owl Costume":
            lambda state: state.has_from_list(area_items, player,6) and state.has_from_list(day_items, player,4),
        "TV Shop Late Night - Firefly Costume":
            lambda state: state.has_from_list(area_items, player,7) and state.has_from_list(day_items, player,5),
    }
    return rules