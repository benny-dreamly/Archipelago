from typing import Dict, List, TypedDict
from BaseClasses import ItemClassification
from .data import ItemName
from .Constants import AOD_BASE_ID

class ItemDict(TypedDict):
    id: int
    classification: ItemClassification

item_table: Dict[str, ItemDict] = {
    # Puzzles
    ItemName.pp1: {"id": AOD_BASE_ID + 1, "classification": ItemClassification.progression},
    ItemName.pp2: {"id": AOD_BASE_ID + 2, "classification": ItemClassification.progression},
    ItemName.pp3: {"id": AOD_BASE_ID + 3, "classification": ItemClassification.progression},
    ItemName.pp4: {"id": AOD_BASE_ID + 4, "classification": ItemClassification.progression},
    ItemName.p1: {"id": AOD_BASE_ID + 5, "classification": ItemClassification.progression},
    ItemName.p2: {"id": AOD_BASE_ID + 6, "classification": ItemClassification.progression},
    ItemName.p3: {"id": AOD_BASE_ID + 7, "classification": ItemClassification.progression},
    ItemName.p4: {"id": AOD_BASE_ID + 8, "classification": ItemClassification.progression},
    ItemName.finished_puzzle: {"id": AOD_BASE_ID + 9, "classification": ItemClassification.progression},

    # Hints
    ItemName.h1:   {"id": AOD_BASE_ID + 10, "classification": ItemClassification.progression_skip_balancing},
    ItemName.sh:   {"id": AOD_BASE_ID + 11, "classification": ItemClassification.useful},
    ItemName.gb:   {"id": AOD_BASE_ID + 12, "classification": ItemClassification.useful},
    ItemName.fc:   {"id": AOD_BASE_ID + 13, "classification": ItemClassification.useful},
    ItemName.h3:   {"id": AOD_BASE_ID + 14, "classification": ItemClassification.progression_skip_balancing},
    ItemName.c1:   {"id": AOD_BASE_ID + 15, "classification": ItemClassification.progression_skip_balancing},
    ItemName.c1_2: {"id": AOD_BASE_ID + 16, "classification": ItemClassification.progression_skip_balancing},
    ItemName.c3:   {"id": AOD_BASE_ID + 17, "classification": ItemClassification.progression_skip_balancing},

    # Hint Fragments
    ItemName.hf_a: {"id": AOD_BASE_ID + 18, "classification": ItemClassification.progression_skip_balancing},
    ItemName.hf_b: {"id": AOD_BASE_ID + 19, "classification": ItemClassification.progression_skip_balancing},
    ItemName.hf_c: {"id": AOD_BASE_ID + 20, "classification": ItemClassification.progression_skip_balancing},
    ItemName.hf_d: {"id": AOD_BASE_ID + 21, "classification": ItemClassification.progression_skip_balancing},
    ItemName.hf_e: {"id": AOD_BASE_ID + 22, "classification": ItemClassification.progression_skip_balancing},
    ItemName.hf_f: {"id": AOD_BASE_ID + 23, "classification": ItemClassification.progression_skip_balancing},
    ItemName.hf_g: {"id": AOD_BASE_ID + 24, "classification": ItemClassification.progression_skip_balancing},
    ItemName.hf_h: {"id": AOD_BASE_ID + 25, "classification": ItemClassification.progression_skip_balancing},
    ItemName.hf_i: {"id": AOD_BASE_ID + 26, "classification": ItemClassification.progression_skip_balancing},
    ItemName.hf_j: {"id": AOD_BASE_ID + 27, "classification": ItemClassification.progression_skip_balancing},
    ItemName.hf_k: {"id": AOD_BASE_ID + 28, "classification": ItemClassification.progression_skip_balancing},
    ItemName.hf_l: {"id": AOD_BASE_ID + 29, "classification": ItemClassification.progression_skip_balancing},
    ItemName.hf_m: {"id": AOD_BASE_ID + 30, "classification": ItemClassification.progression_skip_balancing},

    # Progression Items
    ItemName.key:              {"id": AOD_BASE_ID + 31, "classification": ItemClassification.progression},
    ItemName.glue_stick:       {"id": AOD_BASE_ID + 32, "classification": ItemClassification.progression},
    ItemName.broom:            {"id": AOD_BASE_ID + 33, "classification": ItemClassification.progression},
    ItemName.empty_bucket:     {"id": AOD_BASE_ID + 34, "classification": ItemClassification.progression},
    ItemName.filled_bucket:    {"id": AOD_BASE_ID + 35, "classification": ItemClassification.progression},
    ItemName.magnifying_glass: {"id": AOD_BASE_ID + 36, "classification": ItemClassification.progression},
    ItemName.lighter:          {"id": AOD_BASE_ID + 37, "classification": ItemClassification.progression},
}