from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from . import Smash64World


class Smash64Location(Location):
    game = "Smash 64"

class Smash64LocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[["Smash64World"], bool] = lambda world: True
    locked_item: Optional[str] = None

location_data_table: Dict[str, Smash64Location] = {
    "Example Location": Smash64LocationData(
    region="Example Region",
    address=0x40001,
    ),
    "Example Location 2": Smash64LocationData(
    region="Example Region",
    address=0x40002,
    ),

}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}