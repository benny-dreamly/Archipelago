from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .Options import option_groups

class TaylorSwiftWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Taylor Swift Discography for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["bennydreamly"]
    )]

    option_groups = option_groups