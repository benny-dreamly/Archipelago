import typing

if typing.TYPE_CHECKING:
    from .Client import SimsContext

desired_traits = [
        "Consumable", "Food", "Drink", "Buff",
        "Seed", "Cure", "Resource", "Meat",
        "Vegetable", "Fruit", "Egg", "Currency",
        "Furniture", "Clothing"
    ]

sims4_gifting_options = {
    "accepts_any_gift": True,
    "desired_traits": desired_traits,
    "minimum_gift_version": 3,
}