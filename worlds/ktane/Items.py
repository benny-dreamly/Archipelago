from BaseClasses import Item


class KTANEItem(Item):
    game: str = "Keep Talking and Nobody Explodes"

#Name classification:
#713 01 001
#713 Auth
#01 Game
#001 itemID

modules_item_table = {
    "Complicated Wires": 71301001,
    "Maze": 71301002,
    "Memory": 71301003,
    "Morse Code": 71301004,
    "Password": 71301005,
    "Simon Says": 71301006,
    "Who's on First": 71301007,
    "Wire Sequence": 71301008,
    "Capacitor": 71301009,
    "Knob": 71301010,
    "Vent Gas": 71301011
}

modules_item_nohl_table = {
    "Complicated Wires": 71301001,
    "Maze": 71301002,
    "Memory": 71301003,
    "Morse Code": 71301004,
    "Password": 71301005,
    "Simon Says": 71301006,
    "Who's on First": 71301007,
    "Wire Sequence": 71301008,
    "Knob": 71301010
}

other_progression_items = {
    "Bomb Fragment": 71301012,
    "Time++": 71301013
}

useful_items = {
    "Time+": 71301014
}

filler_item = {
    "Strike+": 71301015
}

item_table = {
    **modules_item_table, **other_progression_items, **useful_items, **filler_item
}