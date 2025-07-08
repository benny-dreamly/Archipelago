from dataclasses import dataclass
from Options import Choice, Range, Toggle, PerGameCommonOptions, StartInventoryPool, DeathLink

class Goal(Choice):
    """
    Required Goal to complete the seed
    Altair - Clear the game by defeating the final boss
    Gold Cards - Clear the game by getting enough gold cards for shorter seeds
    Bosses - Clear the game by beating the 4 main world bosses
    """
    #display_name = "Goal"
    option_altair = 0
    option_goalcards = 1
    option_mainbosses = 2
    default = 0

class OpenStages(Toggle):
    """If Selected The first 3 stages of the main 4 worlds will be open from the start
    You will still require a key to access the Boss Stage"""

class HardMode(Choice):
    """Determines The Logic Used for Gold Card Checks, 
    This should be Set to the in game difficulty you want to use"""
    display_name = "Game Difficulty"
    option_normal = 0
    option_hard = 1
    default = 0

class GoldCards(Range):
    """Number of Gold Cards required to access Black Fortress
    Keep in mind 3 black keys will also be required to reach the goal
    if Final Boss is Selected
    If Gold Card Goal is Selected then this determines the number of Cards 
    Needed to hit your goal"""
    display_name = "Required Gold Cards"
    range_start = 8
    range_end = 100
    default = 45

class MaxCards(Range):
    """Max number of Gold Cards in the pool"""
    display_name = "Max Gold Cards"
    range_start = 8
    range_end = 100
    default = 50

class IncludePalace(Toggle):
    """Includes Locations for Rainbow Palace stages, 
    When this option is disabled, filler items will be placed in Rainbow Palace's locations but the stages will still unlock
    Stages are unlocked for every 25% of required gold cards."""

class RandomMusic(Toggle):
    """Shuffles the game music"""

class RandomSound(Toggle):
    """Shuffles the game sounds"""

class RandomEnemyModel(Choice):
    """If enabled will randomize enemies
    This option will require the use of the companion bomberman_64.lua script to function
    Shuffle: Suffles the enemy models consistently
    Chaotic: Randomizes enemy model every load"""
    option_off = 0
    option_shuffle = 1
    option_chaos = 2
    default = 0

class RandomEnemyAI(Choice):
    """If enabled will randomize enemies
    This option will require the use of the companion bomberman_64.lua script to function
    Shuffle: Suffles the enemy AI consistently
    Chaotic: Randomizes enemy AI every load"""
    option_off = 0
    option_shuffle = 1
    option_chaos = 2
    default = 0

class BombermanColor(Choice):
    """Changes Bomberman's model color"""
    option_white = 0
    option_black = 1
    #option_red = 2
    #option_blue = 3
    default = 0

class BomberHead(Choice):
    """Changes Bomberman's head model"""
    option_bomber = 0xFF
    option_knight = 0x56
    option_dragon = 0x53
    option_iron =   0x55
    option_cat =    0x52
    option_girl =   0x54
    option_cool =   0x51
    option_chicken =0x58
    option_samurai =0x59
    option_clown =  0x57
    option_gold =   0x50
    default =       0xFF

class BomberBody(Choice):
    """Changes Bomberman's body model"""
    option_bomber = 0xFF
    option_knight = 0x60
    option_dragon = 0x5D
    option_iron =   0x5F
    option_cat =    0x5C
    option_girl =   0x5E
    option_cool =   0x5B
    option_chicken =0x62
    option_samurai =0x63
    option_clown =  0x61
    option_gold =   0x5A
    default =       0xFF

class BomberArmLeft(Choice):
    """Changes Bomberman's left arm model"""
    option_bomber = 0xFF
    option_knight = 0x6A
    option_dragon = 0x67
    option_iron =   0x69
    option_cat =    0x66
    option_girl =   0x68
    option_cool =   0x65
    option_chicken =0x6C
    option_samurai =0x6D
    option_clown =  0x6B
    option_gold =   0x64
    default =       0xFF

class BomberArmRight(Choice):
    """Changes Bomberman's right arm model"""
    option_bomber = 0xFF
    option_knight = 0x7E
    option_dragon = 0x7B
    option_iron =   0x7D
    option_cat =    0x7A
    option_girl =   0x7C
    option_cool =   0x79
    option_chicken =0x80
    option_samurai =0x81
    option_clown =  0x7F
    option_gold =   0x78
    default =       0xFF

class BomberLegLeft(Choice):
    """Changes Bomberman's left leg model"""
    option_bomber = 0xFF
    option_knight = 0x74
    option_dragon = 0x71
    option_iron =   0x73
    option_cat =    0x70
    option_girl =   0x72
    option_cool =   0x6F
    option_chicken =0x76
    option_samurai =0x77
    option_clown =  0x75
    option_gold =   0x6E
    default =       0xFF

class BomberLegRight(Choice):
    """Changes Bomberman's right leg model"""
    option_bomber = 0xFF
    option_knight = 0x88
    option_dragon = 0x85
    option_iron =   0x87
    option_cat =    0x84
    option_girl =   0x86
    option_cool =   0x83
    option_chicken =0x8A
    option_samurai =0x8B
    option_clown =  0x89
    option_gold =   0x82
    default =       0xFF

@dataclass
class Bomb64Options(PerGameCommonOptions):
    #start_inventory_from_pool: StartInventoryPool
    open_stages: OpenStages
    gold_cards: GoldCards
    max_cards: MaxCards
    game_goal: Goal
    difficulty: HardMode
    random_music: RandomMusic
    random_sound: RandomSound
    enemy_model : RandomEnemyModel
    color: BombermanColor
    palace_on: IncludePalace
    enemy_ai: RandomEnemyAI
    death_link: DeathLink
    head_part: BomberHead
    body_part: BomberBody
    arm_left_part: BomberArmLeft
    arm_right_part: BomberArmRight
    leg_left_part: BomberLegLeft
    leg_right_part: BomberLegRight
