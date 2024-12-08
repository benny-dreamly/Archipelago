from BaseClasses import Region, Entrance, Tutorial, ItemClassification
from Options import PerGameCommonOptions
from worlds.AutoWorld import World, WebWorld
from .Names import ItemName
from .Items import AODItem, puzzle_related_item_data_table, hint_related_data_table, other_progression_data_table, item_data_table, item_table

class AdventuresOfDreamlandWorld(World):
    """
    Adventures of Dreamland is an Adventure Game! Have fun.
    """
    game = "Adventures of Dreamland"
    options_dataclass = PerGameCommonOptions
    item_name_to_id = item_table