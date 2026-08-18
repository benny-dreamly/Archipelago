from worlds.AutoWorld import World
from . import Items as taylor_swift_items
from .Options import TaylorSwiftOptions

class TaylorSwiftWorld(World):
    """Taylor Swift's discography as an archipelago integration where you get checks by listening to music"""

    game = "Taylor Swift Discography"

    base_id = 1989

    options_dataclass = TaylorSwiftOptions
    options: TaylorSwiftOptions

    item_name_to_id = taylor_swift_items.ITEM_NAME_TO_ID

    def create_item(self, name: str) -> taylor_swift_items.TaylorSwiftItem:
        return taylor_swift_items.create_item_with_correct_classification(self, name)

    def create_items(self) -> None:
        taylor_swift_items.create_all_items(self)

    def get_filler_item_name(self) -> str:
        return taylor_swift_items.get_random_filler_item_name(self)
