from typing import Dict
import LocationName

cell_region_locations: Dict = {
    LocationName.pickup_pp1: None,
    LocationName.pickup_h1: None,
    LocationName.pickup_c1: None,
    LocationName.pickup_c12: None,
    LocationName.pickup_c2: None,
    LocationName.pickup_puzzle: None,
    LocationName.pickup_scroll: None,
}

vault_region_locations: Dict = {
    LocationName.pickup_sh: None,
    LocationName.pickup_gb: None,
    LocationName.pickup_gc: None
}

cell_puzzle_locations: Dict = {
    LocationName.solve_1: None
}

vault_puzzle_locations: Dict = {
    LocationName.solve_2: None
}

hallway_puzzle_locations: Dict = {
    LocationName.solve_3: None
}