from typing import List, TypedDict
from BaseClasses import ItemClassification
from .Names import ItemName
from .Constants import AOD_BASE_ID

class ItemDict(TypedDict):
    name: str
    id: int
    classification: ItemClassification

item_table: List[TypedDict] = [
    # Puzzles
    {"name": ItemName.puzzle_piece_one, "id": AOD_BASE_ID + 1, "classification":ItemClassification.progression},
    {"name": ItemName.puzzle_piece_two, "id": AOD_BASE_ID + 2, "classification": ItemClassification.progression},
    {"name": ItemName.puzzle_piece_three, "id": AOD_BASE_ID + 3, "classification": ItemClassification.progression},
    {"name": ItemName.puzzle_piece_four, "id": AOD_BASE_ID + 4, "classification": ItemClassification.progression},
    {"name": ItemName.empty_puzzle, "id": AOD_BASE_ID + 5, "classification": ItemClassification.progression},
    {"name": ItemName.partially_empty_puzzle, "id": AOD_BASE_ID + 6, "classification": ItemClassification.progression},
    {"name": ItemName.half_finished_puzzle, "id": AOD_BASE_ID + 7, "classification": ItemClassification.progression},
    {"name": ItemName.almost_finished_puzzle, "id": AOD_BASE_ID + 8, "classification": ItemClassification.progression},
    {"name": ItemName.finished_puzzle, "id": AOD_BASE_ID + 9, "classification": ItemClassification.progression},

    # Hints
    {"name": ItemName.hint_one, "id": AOD_BASE_ID + 10, "classification": ItemClassification.useful},
    {"name": ItemName.scroll_hint, "id": AOD_BASE_ID + 11, "classification": ItemClassification.useful},
    {"name": ItemName.gold_bar, "id": AOD_BASE_ID + 12, "classification": ItemClassification.useful},
    {"name": ItemName.fragment_clue, "id": AOD_BASE_ID + 13, "classification": ItemClassification.useful},
    {"name": ItemName.hint_three, "id": AOD_BASE_ID + 14, "classification": ItemClassification.progression_skip_balancing},
    {"name": ItemName.clue_one, "id": AOD_BASE_ID + 15, "classification": ItemClassification.useful},
    {"name": ItemName.clue_one_part_two, "id": AOD_BASE_ID + 16, "classification": ItemClassification.useful},
    {"name": ItemName.clue_two, "id": AOD_BASE_ID + 17, "classification": ItemClassification.useful},
    {"name": ItemName.hint_fragment_a, "id": AOD_BASE_ID + 18, "classification": ItemClassification.progression_skip_balancing},
    {"name": ItemName.hint_fragment_b, "id": AOD_BASE_ID + 19, "classification": ItemClassification.progression_skip_balancing},
    {"name": ItemName.hint_fragment_c, "id": AOD_BASE_ID + 20, "classification": ItemClassification.progression_skip_balancing},
    {"name": ItemName.hint_fragment_d, "id": AOD_BASE_ID + 21, "classification": ItemClassification.progression_skip_balancing},
    {"name": ItemName.hint_fragment_e, "id": AOD_BASE_ID + 22, "classification": ItemClassification.progression_skip_balancing},
    {"name": ItemName.hint_fragment_f, "id": AOD_BASE_ID + 23, "classification": ItemClassification.progression_skip_balancing},
    {"name": ItemName.hint_fragment_g, "id": AOD_BASE_ID + 24, "classification": ItemClassification.progression_skip_balancing},
    {"name": ItemName.hint_fragment_h, "id": AOD_BASE_ID + 25, "classification": ItemClassification.progression_skip_balancing},
    {"name": ItemName.hint_fragment_i, "id": AOD_BASE_ID + 26, "classification": ItemClassification.progression_skip_balancing},
    {"name": ItemName.hint_fragment_j, "id": AOD_BASE_ID + 27, "classification": ItemClassification.progression_skip_balancing},
    {"name": ItemName.hint_fragment_k, "id": AOD_BASE_ID + 28, "classification": ItemClassification.progression_skip_balancing},
    {"name": ItemName.hint_fragment_l, "id": AOD_BASE_ID + 29, "classification": ItemClassification.progression_skip_balancing},
    {"name": ItemName.hint_fragment_m, "id": AOD_BASE_ID + 30, "classification": ItemClassification.progression_skip_balancing},

    # Progression Items
    {"name": ItemName.key, "id": AOD_BASE_ID + 31, "classification": ItemClassification.progression},
    {"name": ItemName.glue_stick, "id": AOD_BASE_ID + 32, "classification": ItemClassification.progression},
    {"name": ItemName.broom, "id": AOD_BASE_ID + 33, "classification": ItemClassification.progression},
    {"name": ItemName.empty_bucket, "id": AOD_BASE_ID + 34, "classification": ItemClassification.progression},
    {"name": ItemName.filled_bucket, "id": AOD_BASE_ID + 35, "classification": ItemClassification.progression},
    {"name": ItemName.magnifying_glass, "id": AOD_BASE_ID + 36, "classification": ItemClassification.progression},
    {"name": ItemName.lighter, "id": AOD_BASE_ID + 37, "classification": ItemClassification.progression},
]