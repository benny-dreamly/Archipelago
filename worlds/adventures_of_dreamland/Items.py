from typing import Dict, NamedTuple, Optional
from BaseClasses import Item, ItemClassification
from .Names import ItemName

adventures_of_dreamland_base_id: int = 64000

class AODItem(Item):
    game: str = "Adventures of Dreamland"

class AODItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler

puzzle_related_item_data_table: Dict[str, AODItemData]{
    ItemName.puzzle_piece_one: AODItemData(adventures_of_dreamland_base_id + 1, ItemClassification.progression),
    ItemName.puzzle_piece_two: AODItemData(adventures_of_dreamland_base_id + 2, ItemClassification.progression),
    ItemName.puzzle_piece_three: AODItemData(adventures_of_dreamland_base_id + 3, ItemClassification.progression),
    ItemName.puzzle_piece_four: AODItemData(adventures_of_dreamland_base_id + 4, ItemClassification.progression),
    ItemName.empty_puzzle: AODItemData(adventures_of_dreamland_base_id + 5, ItemClassification.progression),
    ItemName.partially_empty_puzzle: AODItemData(adventures_of_dreamland_base_id + 6, ItemClassification.progression),
    ItemName.half_finished_puzzle: AODItemData(adventures_of_dreamland_base_id + 7, ItemClassification.progression),
    ItemName.almost_finished_puzzle: AODItemData(adventures_of_dreamland_base_id + 8, ItemClassification.progression),
    ItemName.finished_puzzle: AODItemData(adventures_of_dreamland_base_id + 9, ItemClassification.progression),
}

hint_related_data_table: Dict[str, AODItemData]{
    ItemName.hint_one: AODItemData(adventures_of_dreamland_base_id + 10, ItemClassification.useful),
    ItemName.scroll_hint: AODItemData(adventures_of_dreamland_base_id + 11, ItemClassification.useful),
    ItemName.gold_bar: AODItemData(adventures_of_dreamland_base_id + 12, ItemClassification.useful),
    ItemName.fragment_clue: AODItemData(adventures_of_dreamland_base_id + 13, ItemClassification.useful),
    ItemName.hint_three: AODItemData(adventures_of_dreamland_base_id + 14, ItemClassification.progression_skip_balancing),
    ItemName.clue_one: AODItemData(adventures_of_dreamland_base_id + 15, ItemClassification.useful),
    ItemName.clue_one_part_two: AODItemData(adventures_of_dreamland_base_id + 16, ItemClassification.useful),
    ItemName.clue_two: AODItemData(adventures_of_dreamland_base_id + 17, ItemClassification.useful),
    ItemName.hint_fragment_a: AODItemData(adventures_of_dreamland_base_id + 18, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_b: AODItemData(adventures_of_dreamland_base_id + 19, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_c: AODItemData(adventures_of_dreamland_base_id + 20, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_d: AODItemData(adventures_of_dreamland_base_id + 21, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_e: AODItemData(adventures_of_dreamland_base_id + 22, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_f: AODItemData(adventures_of_dreamland_base_id + 23, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_g: AODItemData(adventures_of_dreamland_base_id + 24, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_h: AODItemData(adventures_of_dreamland_base_id + 25, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_i: AODItemData(adventures_of_dreamland_base_id + 26, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_j: AODItemData(adventures_of_dreamland_base_id + 27, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_k: AODItemData(adventures_of_dreamland_base_id + 28, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_l: AODItemData(adventures_of_dreamland_base_id + 29, ItemClassification.progression_skip_balancing),
    ItemName.hint_fragment_m: AODItemData(adventures_of_dreamland_base_id + 30, ItemClassification.progression_skip_balancing),
}

other_progression_data_table: Dict[str, AODItemData]{
    ItemName.key: AODItemData(adventures_of_dreamland_base_id + 31, ItemClassification.progression),
    ItemName.glue_stick: AODItemData(adventures_of_dreamland_base_id + 32, ItemClassification.progression),
    ItemName.broom: AODItemData(adventures_of_dreamland_base_id + 33, ItemClassification.progression),
    ItemName.empty_bucket: AODItemData(adventures_of_dreamland_base_id + 34, ItemClassification.progression),
    ItemName.filled_bucket: AODItemData(adventures_of_dreamland_base_id + 35, ItemClassification.progression),
    ItemName.magnifying_glass: AODItemData(adventures_of_dreamland_base_id + 36, ItemClassification.progression),
    ItemName.lighter: AODItemData(adventures_of_dreamland_base_id + 37, ItemClassification.progression),
}

item_data_table: Dict[str, AODItemData] = {**puzzle_related_item_data_table, **hint_related_data_table, **other_progression_data_table}

item_data = {name: data.code for name, data in item_data_table.items() if data.code is not None}