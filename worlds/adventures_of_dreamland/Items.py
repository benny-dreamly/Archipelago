from typing import Dict, NamedTuple, Optional
from BaseClasses import Item, ItemClassification
from .Names import ItemName
from .Constants import AOD_BASE_ID

class AODItem(Item):
    game: str = "Adventures of Dreamland"

class AODItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler

puzzle_related_item_data_table: Dict[str, AODItemData] = {
    ItemName.puzzle_piece_one: AODItemData(AOD_BASE_ID + 1, ItemClassification.progression),
    ItemName.puzzle_piece_two: AODItemData(AOD_BASE_ID + 2, ItemClassification.progression),
    ItemName.puzzle_piece_three: AODItemData(AOD_BASE_ID + 3, ItemClassification.progression),
    ItemName.puzzle_piece_four: AODItemData(AOD_BASE_ID + 4, ItemClassification.progression),
    ItemName.empty_puzzle: AODItemData(AOD_BASE_ID + 5, ItemClassification.progression),
    ItemName.partially_empty_puzzle: AODItemData(AOD_BASE_ID + 6, ItemClassification.progression),
    ItemName.half_finished_puzzle: AODItemData(AOD_BASE_ID + 7, ItemClassification.progression),
    ItemName.almost_finished_puzzle: AODItemData(AOD_BASE_ID + 8, ItemClassification.progression),
    ItemName.finished_puzzle: AODItemData(AOD_BASE_ID + 9, ItemClassification.progression),
}

hint_related_data_table: Dict[str, AODItemData] = {
    ItemName.hint_one: AODItemData(AOD_BASE_ID + 10, ItemClassification.useful),
    ItemName.scroll_hint: AODItemData(AOD_BASE_ID + 11, ItemClassification.useful),
    ItemName.gold_bar: AODItemData(AOD_BASE_ID + 12, ItemClassification.useful),
    ItemName.fragment_clue: AODItemData(AOD_BASE_ID + 13, ItemClassification.useful),
    ItemName.hint_three: AODItemData(AOD_BASE_ID + 14, ItemClassification.progression_skip_balancing),
    ItemName.clue_one: AODItemData(AOD_BASE_ID + 15, ItemClassification.useful),
    ItemName.clue_one_part_two: AODItemData(AOD_BASE_ID + 16, ItemClassification.useful),
    ItemName.clue_two: AODItemData(AOD_BASE_ID + 17, ItemClassification.useful),
    ItemName.hint_fragment_a: AODItemData(AOD_BASE_ID + 18, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_b: AODItemData(AOD_BASE_ID + 19, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_c: AODItemData(AOD_BASE_ID + 20, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_d: AODItemData(AOD_BASE_ID + 21, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_e: AODItemData(AOD_BASE_ID + 22, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_f: AODItemData(AOD_BASE_ID + 23, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_g: AODItemData(AOD_BASE_ID + 24, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_h: AODItemData(AOD_BASE_ID + 25, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_i: AODItemData(AOD_BASE_ID + 26, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_j: AODItemData(AOD_BASE_ID + 27, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_k: AODItemData(AOD_BASE_ID + 28, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_l: AODItemData(AOD_BASE_ID + 29, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_m: AODItemData(AOD_BASE_ID + 30, ItemClassification.progression_skip_balancing),
}

other_progression_data_table: Dict[str, AODItemData] = {
    ItemName.key: AODItemData(AOD_BASE_ID + 31, ItemClassification.progression),
    ItemName.glue_stick: AODItemData(AOD_BASE_ID + 32, ItemClassification.progression),
    ItemName.broom: AODItemData(AOD_BASE_ID + 33, ItemClassification.progression),
    ItemName.empty_bucket: AODItemData(AOD_BASE_ID + 34, ItemClassification.progression),
    ItemName.filled_bucket: AODItemData(AOD_BASE_ID + 35, ItemClassification.progression),
    ItemName.magnifying_glass: AODItemData(AOD_BASE_ID + 36, ItemClassification.progression),
    ItemName.lighter: AODItemData(AOD_BASE_ID + 37, ItemClassification.progression),
}

item_data_table: Dict[str, AODItemData] = {**puzzle_related_item_data_table, **hint_related_data_table, **other_progression_data_table}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}