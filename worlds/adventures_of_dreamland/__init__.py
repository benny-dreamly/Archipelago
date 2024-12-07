from BaseClasses import Region, Entrance, Tutorial, ItemClassification
from Options import PerGameCommonOptions
from worlds.AutoWorld import World, WebWorld

class AdventuresOfDreamlandWorld(World):
    """
    Adventures of Dreamland is an Adventure Game! Have fun.
    """
    game = "Adventures of Dreamland"
    options_dataclass = PerGameCommonOptions

