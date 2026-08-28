from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .Options import option_groups

class GlassAnimalsWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Glass Animals Discography for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["bennydreamly"]
    )]

    option_groups = option_groups