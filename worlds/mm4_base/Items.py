from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from . import MM4World
    

class MM4Item(Item):
    game = "Mega Man 4"

class MM4ItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable[["MM4World"], bool] = lambda world: True
    fillweight: Optional[float] = None

item_data_table: Dict[str, MM4ItemData] = {
    

    "Example Item": MM4ItemData(
        code=0x40001,
        type=ItemClassification.progression,
    ),
    "Example Item 2": MM4ItemData(
        code=0x40002,
        type=ItemClassification.filler,
        num_exist= 2,
        fillweight= 0.5,
    ),


}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
item_id_to_name = {data.code: name for name, data in item_data_table.items() if data.code is not None}
item_filler = [name for name, data in item_data_table.items() if data.type == ItemClassification.filler and data.fillweight is not None]
item_filler_weight = [data.fillweight for name, data in item_data_table.items() if data.type == ItemClassification.filler and data.fillweight is not None]