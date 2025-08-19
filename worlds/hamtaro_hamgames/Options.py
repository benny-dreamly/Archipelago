from dataclasses import dataclass
from Options import Choice, Range, Toggle, DefaultOnToggle, Removed, PerGameCommonOptions, OptionSet, StartInventoryPool, DeathLink

class Goal(Choice):
    """Game's Goal
    Marathon - Complete the Day 7 Marathon
    Bo - Collect all 49 hamigo files then collect Prince Bo's hamigo
    """
    display_name = "Goal"
    option_marathon = 1
    option_bohamigo = 2
    default = 1

class MoveSpeed(Choice):
    """Determines the movement speed of Hamtaro in the game"""
    display_name = "Movement Speed"
    option_normal = 1
    option_fast = 2
    option_hasty_hamster = 3
    default = 1

class NeededMedals(Range):
    """Number of gold medals needed to access the day 7 marathon"""
    display_name = "Medals Needed"
    range_start = 10
    range_end = 14
    default = 14

class NeededNominations(Range):
    """Number of Marathon Nomation items needed to access to day 7 marathon"""
    display_name = "Nominations Needed"
    range_start = 0
    range_end = 50
    default = 0

class MaxNominations(Range):
    """Total number of Marathon Nomination items added into the pool"""
    display_name = "Max Nominations"
    range_start = 0
    range_end = 60

class HamigoStart(Toggle):
    """Start with Hamigo file"""

class Seedsanity(Toggle):
    """Overworld seeds become checks"""

class Costumesanity(DefaultOnToggle):
    """Some Costumes become checks"""

class Talksanity(Removed):
    """Talking to NPCs provide checks"""

class MusicRando(Toggle):
    """Randomizes Music"""

class SoundRando(Toggle):
    """Randomizes sound effects"""

class TextRando(Toggle):
    """Randomizes NPC dialog"""

@dataclass
class HamGamesOptions(PerGameCommonOptions):
    game_goal: Goal
    needed_medals: NeededMedals
    needed_nomination: NeededNominations
    max_nomination: MaxNominations
    seedsanity: Seedsanity
    costumesanity: Costumesanity
    #talksanity: Talksanity
    starthamigo: HamigoStart
    move_speed: MoveSpeed
    death_link: DeathLink
    random_music: MusicRando
    random_sound: SoundRando
    random_text: TextRando

    
