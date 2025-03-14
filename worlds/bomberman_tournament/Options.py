from dataclasses import dataclass
from Options import Choice, Toggle, PerGameCommonOptions, Range, StartInventoryPool, DeathLink

class ZoneNaviation(Choice):
    """
    Determines how traversing regions should function
    Normal: Defeat the dastardly bomber in the base to progress to the next zone
    Key: Zone Keys will be added to the item pool to allow progression into the next region
    Open: Beach, Snow, and Desert Zones will all be open by default 
    Fantasy Region will always require the 4 medals to access
    """
    option_normal = 0
    option_key = 1
    option_open = 2
    default = 0

class PoolMedals(Toggle):
    """If enabled Adds the medals into the item pool
    Otherwise the 4 Medals will be earned by clearing dungeons"""
    display_name = "Pool Medals"

class Mapsanity(Toggle):
    """If enabled Every Room in a Dungeon will become seperate Locations"""
    display_name = "Mapsanity"

class Rocksanity(Toggle):
    """If enabled every hidden Elifan room will become a check"""
    display_name = "Rocksanity"

class KaraMultiply(Range):
    """Multiplies the amount of stats you gain from Karabon stat tiles"""
    auto_display_name = "Karabon Multiplier"
    range_start = 1
    range_end = 10
    default = 2


class BaseSpeed(Range):
    """Sets the base movement speed, the games vanilla base value is 2"""
    display_name = "Movement Speed"
    range_start = 2
    range_end = 8
    default = 4

class RandomEnemy(Choice):
    """Randomizes Enemy objects in maps
    vanilla - No Randomization
    shuffle - Shuffles Enemy types with each other
    chaotic - Randomizes the enemies in each region with any enemy type
    only 8 unqiue enemy types will be shuffled to a region
    """
    display_name = "Randomize Enemies"
    option_vanilla = 0
    option_shuffle = 1
    option_chaotic = 2
    default = 0

class RandomFuse(Choice):
    """Randomizes Fusion Materials for Karabon Fusions
    vanilla - No Randomization
    materials - Only the materials are randomized
    materialandresult - Both the materials and the result are randomized (currently broken)"""
    display_name = "Random SID Fusion"
    option_vanilla = 0
    option_materials = 1
    option_materialandresult = 2
    default = 0

class RandomMusic(Toggle):
    """Randomizes the music table every time the client is loaded"""
class RandomSound(Toggle):
    """Randomizes the Sound Effect table every time the client is loaded"""

class Autosave(Toggle):
    """If enabled will attempt to autosave between every map transition"""

class NPCSprite(Toggle):
    """If enabled NPCs will have a random sprite"""
    display_name = "Randomize NPC Sprites"

class BomberColor(Choice):
    """Determines Bomberman's Color Palette
    by part - Select each color of each part individually"""
    option_white = 0
    option_black = 1
    option_red = 2
    option_blue = 3
    option_purple = 9
    option_magnet = 4
    option_pretty = 5
    option_plasma = 6
    option_golem = 7
    option_max = 8
    option_bypart = 16
    default = 0

class PrimaryColor(Choice):
    """If By part is chosen for the Bomber Color option then this will set the body and head color"""
    option_classic = 0
    option_black = 1
    option_magnet = 2
    option_pretty = 3
    option_plasma = 4
    option_golem = 5
    option_max = 6
    option_red = 7
    option_orange = 8
    option_yellow = 9
    option_green = 10
    option_mint = 11
    option_cyan = 12
    option_blue = 13
    option_purple = 14
    option_magenta = 15
    option_pink = 16
    option_white = 17
    option_brown = 18

    
class LimbColor(Choice):
    """If By part is chosen for the Bomber Color option then this will set the hand and feet color"""
    option_classic = 0
    option_green = 1
    option_blue = 2
    option_red = 3
    option_gold = 4
    option_orange = 5
    option_yellow = 6
    option_purple = 7
    option_pink = 12
    option_beige = 8
    option_brown = 9
    option_white = 10
    option_black = 11
    default = 0

class AntennaColor(Choice):
    """If By part is chosen for the Bomber Color option then this will set the antenna color"""
    option_classic = 0
    option_green = 1
    option_blue = 2
    option_red = 3
    option_gold = 4
    option_orange = 5
    option_yellow = 6
    option_purple = 7
    option_pink = 12
    option_beige = 8
    option_brown = 9
    option_white = 10
    option_black = 11
    default = 0

class armColor(Choice):
    """If By part is chosen for the Bomber Color option then this will set the arm color"""
    option_classic = 10
    option_green = 1
    option_blue = 2
    option_red = 3
    option_gold = 4
    option_orange = 5
    option_yellow = 6
    option_purple = 7
    option_pink = 12
    option_beige = 8
    option_brown = 9
    option_black = 11
    default = 10

@dataclass
class BomberTOptions(PerGameCommonOptions):
    #color: ButtonColor
    #hard_mode: HardMode
    #start_inventory_from_pool: StartInventoryPool
    zone_navigation: ZoneNaviation
    pool_medals: PoolMedals
    mapsanity: Mapsanity
    rocksanity: Rocksanity
    random_enemy: RandomEnemy
    random_fuse: RandomFuse
    random_npc: NPCSprite
    move_speed: BaseSpeed
    kara_multiply: KaraMultiply
    random_music: RandomMusic
    random_sound: RandomSound
    autosave: Autosave
    death_link: DeathLink
    bomber_color: BomberColor
    bomber_body_color: PrimaryColor
    bomber_limb_color: LimbColor
    bomber_antenna_color: AntennaColor
    bomber_arm_color: armColor
