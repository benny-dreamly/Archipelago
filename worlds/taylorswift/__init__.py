from worlds.AutoWorld import World
from Utils import visualize_regions
from . import Items as taylor_swift_items
from . import Locations as taylor_swift_locations
from . import Regions as taylor_swift_regions
from . import Rules as taylor_swift_rules
from .Options import TaylorSwiftOptions

class TaylorSwiftWorld(World):
    """Taylor Swift's discography as an archipelago integration where you get checks by listening to music"""

    game = "Taylor Swift Discography"

    base_id = 1989

    options_dataclass = TaylorSwiftOptions
    options: TaylorSwiftOptions

    item_name_to_id = taylor_swift_items.ITEM_NAME_TO_ID
    location_name_to_id = taylor_swift_locations.LOCATION_NAME_TO_ID

    def create_regions(self) -> None:
        taylor_swift_regions.create_and_connect_regions(self)
        taylor_swift_locations.create_all_locations(self)
        # visualize_regions(
        #     self.get_region("Menu"),
        #     "taylorswift.puml",
        #     show_entrance_names=True,
        #     show_entrance_rules=True,
        # )

    def set_rules(self) -> None:
        taylor_swift_rules.set_all_rules(self)
        taylor_swift_rules.set_completion_condition(self)

    def create_item(self, name: str) -> taylor_swift_items.TaylorSwiftItem:
        return taylor_swift_items.create_item_with_correct_classification(self, name)

    def create_items(self) -> None:
        taylor_swift_items.create_all_items(self)

    def get_filler_item_name(self) -> str:
        return taylor_swift_items.get_random_filler_item_name(self)
