from typing import Dict, TypedDict
from .data import LocationName
from .Constants import *

class LocationInfo(TypedDict):
    id: int
    region: str

location_table: Dict[str, LocationInfo] = {
    # Solves
    LocationName.solve_1: {"id": AOD_BASE_ID + 1, "region": CELL_PUZZLE},
    LocationName.solve_2: {"id": AOD_BASE_ID + 2, "region": VAULT_PUZZLE},
    LocationName.solve_3: {"id": AOD_BASE_ID + 3},
    LocationName.solve_4: {"id": AOD_BASE_ID + 4},

    # Pickups
    LocationName.pickup_pp1: {"id": AOD_BASE_ID + 5, "region": CELL},
    LocationName.pickup_h1: {"id": AOD_BASE_ID + 6, "region": CELL},
    LocationName.pickup_c1: {"id": AOD_BASE_ID + 7, "region": CELL},
    LocationName.pickup_c12: {"id": AOD_BASE_ID + 8, "region": CELL},
    LocationName.pickup_c2: {"id": AOD_BASE_ID + 9, "region": CELL},
    LocationName.pickup_puzzle: {"id": AOD_BASE_ID + 10, "region": CELL},
    LocationName.pickup_scroll: {"id": AOD_BASE_ID + 11, "region": CELL},
    LocationName.pickup_ha: {"id": AOD_BASE_ID + 12},
    LocationName.pickup_hb: {"id": AOD_BASE_ID + 13},
    LocationName.pickup_hc: {"id": AOD_BASE_ID + 14},
    LocationName.pickup_hd: {"id": AOD_BASE_ID + 15},
    LocationName.pickup_he: {"id": AOD_BASE_ID + 16},
    LocationName.pickup_hf: {"id": AOD_BASE_ID + 17},
    LocationName.pickup_hi: {"id": AOD_BASE_ID + 18},
    LocationName.pickup_hj: {"id": AOD_BASE_ID + 19},
    LocationName.pickup_hk: {"id": AOD_BASE_ID + 20},
    LocationName.pickup_hl: {"id": AOD_BASE_ID + 21},
    LocationName.pickup_hm: {"id": AOD_BASE_ID + 22},
    LocationName.pickup_sh: {"id": AOD_BASE_ID + 23},
    LocationName.pickup_fc: {"id": AOD_BASE_ID + 24},
    LocationName.pickup_gb: {"id": AOD_BASE_ID + 25},
    LocationName.pickup_gc: {"id": AOD_BASE_ID + 26},
    LocationName.pickup_pp2: {"id": AOD_BASE_ID + 27},
    LocationName.pickup_gs: {"id": AOD_BASE_ID + 28},
    LocationName.pickup_bm: {"id": AOD_BASE_ID + 29},
    LocationName.pickup_bkt: {"id": AOD_BASE_ID + 30},
    LocationName.pickup_ltr: {"id": AOD_BASE_ID + 31},
    LocationName.pickup_mg: {"id": AOD_BASE_ID + 32},
    LocationName.pickup_pp3: {"id": AOD_BASE_ID + 33},
    LocationName.pickup_pp4: {"id": AOD_BASE_ID + 34},

    # Actions
    LocationName.decipher_h1: {"id": AOD_BASE_ID + 35},
    LocationName.unlock_sfe: {"id": AOD_BASE_ID + 36},
    LocationName.reassemble_h3: {"id": AOD_BASE_ID + 37},
    LocationName.decipher_h3: {"id": AOD_BASE_ID + 38},
    LocationName.fill_bkt: {"id": AOD_BASE_ID + 39},
    LocationName.open_tdr: {"id": AOD_BASE_ID + 40},
    LocationName.burn_bm: {"id": AOD_BASE_ID + 41},
    LocationName.extinguish_fire: {"id": AOD_BASE_ID + 42},
    LocationName.get_key: {"id": AOD_BASE_ID + 43},
    LocationName.unlock_ed: {"id": AOD_BASE_ID + 44},
}