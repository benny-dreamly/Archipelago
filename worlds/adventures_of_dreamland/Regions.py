from BaseClasses import Entrance, Region
from .Locations import location_table
from .data import RegionData
from .Constants import *
from . import AODLocation

def create_regions(self) -> None:
    cell_region = Region("Cell", self.player, self.multiworld)
    cell_region.add_locations(RegionData.cell_region_locations, AODLocation)

    puzzle1_region = Region(CELL_PUZZLE, self.player, self.multiworld)
    puzzle1_region.add_locations(RegionData.cell_puzzle_locations, AODLocation)

    cell_region.connect(puzzle1_region)

    puzzle2_region = Region(VAULT_PUZZLE, self.player, self.multiworld)
    puzzle2_region.add_locations(RegionData.vault_puzzle_locations, AODLocation)

    hallway_region = Region(HALLWAY, self.player, self.multiworld)

    cell_region.connect(hallway_region)

    vault_region = Region(VAULT, self.player, self.multiworld)
    vault_region.add_locations(RegionData.vault_region_locations, AODLocation)

