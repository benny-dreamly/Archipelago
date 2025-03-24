from typing import Dict
from dataclasses import dataclass
from Options import Choice, Range, Option, Toggle, StartInventoryPool, PerGameCommonOptions, DeathLink

class Fleasanity(Toggle):
    """Adds killing fleas as extra checks"""
class RandomMusic(Toggle):
    display_name = "Randomize Music"

class RandomAtkSFX(Toggle):
    display_name= "Random Limb Attack Sound"

class QueenItems(Range):
    """Number of Mcguffin items required to reach the Flea Queen"""
    display_name = "Required Queen Items"
    range_start = 4
    range_end = 13
    default = 10

class StartingLives(Range):
    display_name = "Starting Lives"
    range_start = 1
    range_end = 9
    default = 3

@dataclass
class PlokOptions(PerGameCommonOptions):
    fleasanity: Fleasanity
    queen_items: QueenItems
    random_music: RandomMusic
    random_limbsfx: RandomAtkSFX
    start_lives: StartingLives
    death_link: DeathLink