from typing import List, TypedDict
from .Names import LocationName
from .Constants import AOD_BASE_ID

class LocationInfo(TypedDict):
    name: str
    id: int

location_table: List[LocationInfo] = [
    # Solves
    {"name": LocationName.solve_1, "id": AOD_BASE_ID + 1},
    {"name": LocationName.solve_2, "id": AOD_BASE_ID + 2},
    {"name": LocationName.solve_3, "id": AOD_BASE_ID + 3},
    {"name": LocationName.solve_4, "id": AOD_BASE_ID + 4},

    # Pickups
    {"name": LocationName.pickup_pp1, "id": AOD_BASE_ID + 5},
    {"name": LocationName.pickup_h1, "id": AOD_BASE_ID + 6},
    {"name": LocationName.pickup_c1, "id": AOD_BASE_ID + 7},
    {"name": LocationName.pickup_c12, "id": AOD_BASE_ID + 8},
    {"name": LocationName.pickup_c2, "id": AOD_BASE_ID + 9},
    {"name": LocationName.pickup_puzzle, "id": AOD_BASE_ID + 10},
    {"name": LocationName.pickup_scroll, "id": AOD_BASE_ID + 11},
    {"name": LocationName.pickup_ha, "id": AOD_BASE_ID + 12},
    {"name": LocationName.pickup_hb, "id": AOD_BASE_ID + 13},
    {"name": LocationName.pickup_hc, "id": AOD_BASE_ID + 14},
    {"name": LocationName.pickup_hd, "id": AOD_BASE_ID + 15},
    {"name": LocationName.pickup_he, "id": AOD_BASE_ID + 16},
    {"name": LocationName.pickup_hf, "id": AOD_BASE_ID + 17},
    {"name": LocationName.pickup_hi, "id": AOD_BASE_ID + 18},
    {"name": LocationName.pickup_hj, "id": AOD_BASE_ID + 19},
    {"name": LocationName.pickup_hk, "id": AOD_BASE_ID + 20},
    {"name": LocationName.pickup_hl, "id": AOD_BASE_ID + 21},
    {"name": LocationName.pickup_hm, "id": AOD_BASE_ID + 22},
    {"name": LocationName.pickup_sh, "id": AOD_BASE_ID + 23},
    {"name": LocationName.pickup_fc, "id": AOD_BASE_ID + 24},
    {"name": LocationName.pickup_gb, "id": AOD_BASE_ID + 25},
    {"name": LocationName.pickup_gc, "id": AOD_BASE_ID + 26},
    {"name": LocationName.pickup_pp2, "id": AOD_BASE_ID + 27},
    {"name": LocationName.pickup_gs, "id": AOD_BASE_ID + 28},
    {"name": LocationName.pickup_bm, "id": AOD_BASE_ID + 29},
    {"name": LocationName.pickup_bkt, "id": AOD_BASE_ID + 30},
    {"name": LocationName.pickup_ltr, "id": AOD_BASE_ID + 31},
    {"name": LocationName.pickup_mg, "id": AOD_BASE_ID + 32},
    {"name": LocationName.pickup_pp3, "id": AOD_BASE_ID + 33},
    {"name": LocationName.pickup_pp4, "id": AOD_BASE_ID + 34},

    # Actions
    {"name": LocationName.decipher_h1, "id": AOD_BASE_ID + 35},
    {"name": LocationName.unlock_sfe, "id": AOD_BASE_ID + 36},
    {"name": LocationName.reassemble_h3, "id": AOD_BASE_ID + 37},
    {"name": LocationName.decipher_h3, "id": AOD_BASE_ID + 38},
    {"name": LocationName.fill_bkt, "id": AOD_BASE_ID + 39},
    {"name": LocationName.open_tdr, "id": AOD_BASE_ID + 40},
    {"name": LocationName.burn_bm, "id": AOD_BASE_ID + 41},
    {"name": LocationName.extinguish_fire, "id": AOD_BASE_ID + 42},
    {"name": LocationName.get_key, "id": AOD_BASE_ID + 43},
    {"name": LocationName.unlock_ed, "id": AOD_BASE_ID + 44},
]