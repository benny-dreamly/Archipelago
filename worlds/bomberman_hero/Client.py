import typing
from typing import TYPE_CHECKING, Set, Optional, Dict, Any
import logging
from NetUtils import ClientStatus
#from .Items import id_to_string
from base64 import b64encode
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

import time
import random

logger = logging.getLogger("Client")

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

STAGE_HINT = {
    0x134808: "Planet Bomber Area 1",
    0x134809: "Planet Bomber Area 1",
    0x13480A: "Planet Bomber Area 1",
    0x13480B: "Planet Bomber Area 1",
    0x13480C: "Planet Bomber Area 1",

    0x13480F: "Planet Bomber Area 2",
    0x134810: "Planet Bomber Area 2",
    0x134811: "Planet Bomber Area 2",
    0x134812: "Planet Bomber Area 2",
    0x134813: "Planet Bomber Area 2",
    0x134814: "Planet Bomber Area 2",
    0x134815: "Planet Bomber Area 2",

    0x134816: "Planet Bomber Area 3",
    0x134817: "Planet Bomber Area 3",
    0x134818: "Planet Bomber Area 3",
    0x134819: "Planet Bomber Area 3",

    0x13481D: "Primus Area 1",
    0x13481E: "Primus Area 1",
    0x13481F: "Primus Area 1",
    0x134820: "Primus Area 1",
    0x134821: "Primus Area 1",

    0x134824: "Primus Area 2",
    0x134825: "Primus Area 2",
    0x134826: "Primus Area 2",
    0x134827: "Primus Area 2",
    0x134828: "Primus Area 2",
    0x134829: "Primus Area 2",

    0x13482B: "Primus Area 3",
    0x13482C: "Primus Area 3",
    0x13482D: "Primus Area 3",
    0x13482E: "Primus Area 3",

    0x134832: "Kanatia Area 1",
    0x134833: "Kanatia Area 1",
    0x134834: "Kanatia Area 1",
    0x134835: "Kanatia Area 1",
    0x134836: "Kanatia Area 1",

    0x134839: "Kanatia Area 2",
    0x13483A: "Kanatia Area 2",
    0x13483B: "Kanatia Area 2",
    0x13483C: "Kanatia Area 2",
    0x13483D: "Kanatia Area 2",
    0x13483E: "Kanatia Area 2",
    0x13483F: "Kanatia Area 2",

    0x134840: "Kanatia Area 3",
    0x134841: "Kanatia Area 3",
    0x134842: "Kanatia Area 3",
    0x134843: "Kanatia Area 3",
    0x134844: "Kanatia Area 3",

    0x134847: "Mazone Area 1",
    0x134848: "Mazone Area 1",
    0x134849: "Mazone Area 1",
    0x13484A: "Mazone Area 1",

    0x13484E: "Mazone Area 2",
    0x13484F: "Mazone Area 2",
    0x134850: "Mazone Area 2",
    0x134851: "Mazone Area 2",
    0x134852: "Mazone Area 2",

    0x134855: "Mazone Area 3",
    0x134856: "Mazone Area 3",
    0x134857: "Mazone Area 3",
    0x134858: "Mazone Area 3",
    0x134859: "Mazone Area 3",

    0x13485C: "Garaden",
    0x13485D: "Garaden",
    0x13485E: "Garaden",
    0x13485F: "Garaden",
    0x134860: "Garaden",
    0x134861: "Garaden",
    0x134862: "Garaden",

    #0x134871: "Gossick",
    #0x134872: "Gossick",
    #0x134873: "Gossick",
}

ITEM_INDEX = {
    0x16523F:  0x01, # Bombup
    0x165240:  0x02, # Fireup
    0x165268:  0x03, # Glove
    0x165258:  0x04, # Vest
    0x165250:  0x05, # Salt
    0x1779F8:  0x06, # HUD
    0x165244:  0x07, # Gold Heart
    0x165243:  0x08, # 1UP
    0x165248:   0x09, # Adok Bomb

    0x134808: 0x10,#Battle Room
    0x134809: 0x11,#Hyper Room
    0x13480A: 0x12,#Secret Room
    0x13480B: 0x13,#Heavy Room
    0x13480C: 0x14,#Sky Room
    0x13480F: 0x15,#Blue Cave
    0x134810: 0x16,#Hole Lake
    0x134811: 0x17,#Red Cave
    0x134812: 0x18,#Big Cannon
    0x134813: 0x19,#Dark Wood
    0x134814: 0x1A,#Dragon Road
    0x134815: 0x1B,#Vs Nitros Planet Bomber
    0x134816: 0x1C,#Clown Valley
    0x134817: 0x1D,#Great Rock
    0x134818: 0x1E,#Fog Route
    0x134819: 0x1F,#Vs Endol

    0x13481D: 0x20,#Groog Hills
    0x13481E: 0x21,#Bubble Hole
    0x13481F: 0x22,#Erars Lake
    0x134820: 0x23,#Waterway
    0x134821: 0x24,#Water Slider
    0x134824: 0x25,#Rockn Road
    0x134825: 0x26,#Water Pool
    0x134826: 0x27,#Millian Road
    0x134827: 0x28,#Warp Room
    0x134828: 0x29,#Dark Prison
    0x134829: 0x2A,#Vs Nitros Primus
    0x13482B: 0x2B,#Killer Gate
    0x13482C: 0x2C,#Spiral Tower
    0x13482D: 0x2D,#Snake Route
    0x13482E: 0x2E,#Vs Baruda

    0x134832: 0x2F,#Hades Crater
    0x134833: 0x30,#Magma Lake
    0x134834: 0x31,#Magma Dam
    0x134835: 0x32,#Crysta Hole
    0x134836: 0x33,#Emerald Tube
    0x134839: 0x34,#Death Temple
    0x13483A: 0x35,#Death Road
    0x13483B: 0x36,#Death Garden
    0x13483C: 0x37,#Float Zone
    0x13483D: 0x38,#Aqua Tank
    0x13483E: 0x39,#Aqua Way
    0x13483F: 0x3A,#Vs Nitros Kanatia
    0x134840: 0x3B,#Hard Coaster
    0x134841: 0x3C,#Dark Maze
    0x134842: 0x3D,#Mad Coaster
    0x134843: 0x3E,#Move Stone
    0x134844: 0x3F,#Vs Bolban

    0x134847: 0x40,#Hoppy Land
    0x134848: 0x41,#Junfalls
    0x134849: 0x42,#Freeze Lake
    0x13484A: 0x43,#Cool Cave
    0x13484E: 0x44,#Snowland
    0x13484F: 0x45,#Storm Valley
    0x134850: 0x46,#Snow Circuit
    0x134851: 0x47,#Heaven Sky
    0x134852: 0x48,#Eye Snake
    0x134855: 0x49,#Vs Nitros Mazone
    0x134856: 0x4A,#Air Room
    0x134857: 0x4B,#Zero G Room
    0x134858: 0x4C,#Mirror Room
    0x134859: 0x4D,#Vs Natia

    0x13485C: 0x4E,#Boss Room 1
    0x13485D: 0x4F,#Boss Room 2
    0x13485E: 0x50,#Boss Room 3
    0x13485F: 0x51,#Boss Room 4
    0x134860: 0x52,#Boss Room 5
    0x134861: 0x53,#Boss Room 6
    0x134862: 0x54,#Vs Bagular

    #0x134871: 0x55,#Outter Road
    #0x134872: 0x56,#Inner Road
    #0x134873: 0x57,#Vs Evil Bomber
}

RADIO_DUPE = {
    0x80105D08: {0x02000000:0x134808B, 0x02000102:0x134811A}, #Battle Room Raising Platform/#Red Cave Lower Path
    0x80105D6C: {0x02000001:0x134809B, 0x02000004:0x13480CA}, #Hyper Room Door/Sky Room Entrance
    0x80106914: {0x02010104:0x134828A, 0x02020200:0x134840A}, #Dark Prison Entrance/Hard Coaster Green Warp
}

RADIO_INDEX = {
    0x80105F80: 0x134808A, #Battle Room Entrance
    #-- 0x80105D08: 0x134808B, #Battle Room Raising Platform
    0x80106234: 0x134808C, #Battle Room Switch
    0x80105DE4: 0x134809A, #Hyper Room Entrance
    #--0x80105D6C: 0x134809B, #Hyper Room Door
    0x80105EF8: 0x13480AA, #Secret Room Entrance
    0x80105E5C: 0x13480BA, #Heavy Room Entrance
    0x8010608C: 0x13480BB, #Heavy Room Barrier Tower
    #--0x80105D6C: 0x13480CA, #Sky Room Entrance
    #-- 0x80105D08: 0x134811A, #Red Cave Lower Path
    0x80105FF8: 0x134813A, #Dark Wood Entrance
    0x801065A8: 0x13481DA, #Groog Hills Entrance
    0x801064FC: 0x13481DB, #Groog Hills Right Big Tree
    0x80106B10: 0x13481DC, #Groog Hills Frost Blossom
    0x80106A14: 0x13481EA, #Bubble Hole Entrance
    0x80106BDC: 0x13481FA, #Erars Lake Upper Left Warp
    #0x80106914: 0x134828A, Dark Prison Entrance
    0x80106A84: 0x13482BA, #Killer Gate Entrance
    0x80106628: 0x134832A, #Hades Crater Entrance
    0x80106874: 0x134833A, #Magma Dam Entrance
    0x80106818: 0x134833B, # Magma Dam Radio Left Dam
    0x80106488: 0x13483CA, #Float Zone Entrance
    0x801066A8: 0x13483DA, #Aqua Tank Entrance
    # 0x80106914: 0x134840A, #Hard Coaster Green Warp
    0x80106C68: 0x134843A, #Move Stone Entrance
    0x80106410: 0x134847A, #Hopper Land Entrance
    0x80106714: 0x13484FA, #Storm Valley Entrance
    0x80106B78: 0x134857A, #Zero G Room Red Switch
    0x801067B8: 0x134858A, #Mirror Room Entrance
    0x80106990: 0x134858B, #Mirror Room Right Ramp
}

RECV_INDEX = 0x57498

def ramdomize_table(tbl,entrysize):
    split_table = split_into_xbit_chunks(tbl,entrysize)
    random.shuffle(split_table)
    result = b''.join(split_table)
    return result

def ramdomize_table_with_exclude(tbl,entrysize,excepts):
    split_table = split_into_xbit_chunks(tbl,entrysize)
    idxshuffle = []
    new_table = []
    for x in range(len(split_table)):
        idxshuffle.append(x)
        new_table.append(b'/x00/x00/x00/x00')
    random.shuffle(idxshuffle)
    for idx in range(len(split_table)):
        if idx in excepts:
            new_table[idx] = split_table[idx]
            continue
        randidx = idxshuffle.pop(0)
        while randidx in excepts:
            randidx = idxshuffle.pop(0)
        new_table[idx] = split_table[randidx]
    result = b''.join(new_table)
    return result

def split_into_xbit_chunks(byte_array,size):
   #Splits a byte array into chunks of 32 bits (4 bytes).

    chunks = []
    for i in range(0, len(byte_array), size):
        chunk = byte_array[i:i + size]
        # If the last chunk is less than 4 bytes, pad it with zeros
        if len(chunk) < size:
            chunk += b'\x00' * (size - len(chunk)) 
        chunks.append(chunk)
    return chunks

def resync_game_prog(locs):

    return

class BombHClient(BizHawkClient):
    game = "Bomberman Hero"
    system = "N64"
    patch_suffix = ".apbombh"
    #rom: typing.Optional[bytes] = None
    local_checked_locations: Set[int]
    rom_slot_name: Optional[str]

    death_link: bool = False
    sending_death_link: bool = True
    pending_death_link: bool = False

    adok_required = 24
    salt_timer = 0
    point_require = 5
    item_powerup = 0
    item_health = 0
    sound_rando =  False
    sky_rando = False
    music_rando = False
    radio = False

    def __init__(self) -> None:
        super().__init__()
        self.local_checked_locations = set()
        self.rom_slot_name = None

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        # Borrowed some authentication code from Kirby 64's apworld
        from CommonClient import logger
        rom_data = await bizhawk.read(
            ctx.bizhawk_ctx,
            [
            (0x20, 0xE, "ROM"), # 0 Rom Name
            (0xB864D0, 0x10,  "ROM"), # 1 Game Options
            (0xB86500, 0x32, "ROM"), # 2 Slot name
            (0xB864E0, 0x20, "ROM"), # 3 Slot Data
            (0xC,0x4, "EEPROM"), # 4 Save File

            (0x1B80BC,0x200,"RDRAM"), # 5 Sound Table
            (0x1051E0, 0xF0, "RDRAM"), # 6 Skybox Table
            (0x1A738C, 0x100, "RDRAM"), # 7  Music Table
            ]
        )
        #game_name = ((await bizhawk.read(ctx.bizhawk_ctx, [(0x1FFF200, 21, "ROM")]))[0])
        try:
            # Check ROM name/patch version
            rom_name = rom_data[0].decode("ascii")
            if rom_name != "BOMBERMAN HERO":
                return False  # Not a Bomberman Hero ROM
            try:
                #slot_name_bytes = (await bizhawk.read(ctx.bizhawk_ctx, [(0xB86500, 32, "ROM")]))[0]
                slot_name_bytes = rom_data[2]
                self.rom_slot_name = bytes([byte for byte in slot_name_bytes if byte != 0]).decode("utf-8")
            except UnicodeDecodeError:
                logger.info("Could not read slot name from ROM. Are you sure this ROM matches this client version?")
                return False
        except bizhawk.RequestFailedError:
            return False  # Not able to get a response, say no for now

        # This is a Bomberman Hero ROM
        
        ctx.game = self.game
        ctx.items_handling = 0b111
        game_options = rom_data[1]
        #deathlink = (await bizhawk.read(ctx.bizhawk_ctx, [(0xB864D2, 1, "ROM")]))[0][0]
        deathlink = rom_data[1][2]
        if deathlink:
            self.death_link = True
        
        #self.adok_required = (await bizhawk.read(ctx.bizhawk_ctx, [(0xB864D0, 1, "ROM")]))[0][0]
        self.adok_required = game_options[0]
        self.game_goal = game_options[1]
        self.point_require = game_options[6]
        self.item_powerup = (game_options[7] & 0x1)
        self.item_health = (game_options[7] & 0x2)
        self.radio = (game_options[8])
        self.stage_total = (game_options[9])
        # Randomize Sounds
        if rom_data[1][3]:
            self.sound_rando = True
            await bizhawk.write(ctx.bizhawk_ctx, [(0x1B80BC, ramdomize_table(rom_data[5],4), "RDRAM")])

        # Randomize Skybox
        if rom_data[1][4]:
            self.sky_rando = True
            await bizhawk.write(ctx.bizhawk_ctx, [(0x1051E0, ramdomize_table(rom_data[6],4), "RDRAM")])

        # Randomize Music
        if rom_data[1][5]:
            self.music_rando = True
            await bizhawk.write(ctx.bizhawk_ctx, [(0x1A738C, ramdomize_table_with_exclude(rom_data[7],8,[0x00,0x12,0x18,0x1A,0x1D,0x1E,0x1F]), "RDRAM")])


        #self.rom = game_name
        ctx.want_slot_data = True
        logger.info("Start a game file to connect")
        #bizhawk.set_message_interval(ctx.bizhawk_ctx,5)

        return True
        

    def on_package(self, ctx: "BizHawkClientContext", cmd: str, args: Dict[str, Any]) -> None:
        if cmd == "Bounced":
            if "tags" in args:
                assert ctx.slot is not None
                if "DeathLink" in args["tags"] and args["data"]["source"] != ctx.slot_info[ctx.slot].name:
                    self.on_deathlink(ctx)
    
    #async def deathlink_kill_player(self, ctx) -> None:
    #    from worlds._bizhawk import write
    #    await write(ctx.bizhawk_ctx, [(0x154259, bytearray([0x00]), "RDRAM")])

    async def send_deathlink(self, ctx: "BizHawkClientContext") -> None:
        self.sending_death_link = True
        ctx.last_death_link = time.time()
        await ctx.send_death("Bomberman is dead.")

    def on_deathlink(self, ctx: "BizHawkClientContext") -> None:
        ctx.last_death_link = time.time()
        self.pending_death_link = True

    async def set_auth(self, ctx: "BizHawkClientContext") -> None:
        ctx.auth = self.rom_slot_name

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        from CommonClient import logger



        try:
            ram_data = await bizhawk.read(
                ctx.bizhawk_ctx,
                [
                (0x134808, 0x70, "RDRAM"), # 0 Stages
                (0x57495,  0x03, "RDRAM"), # 1 Adok Bombs
                (0x165240,  0x20, "RDRAM"), # 2 Bomber Stats
                (0x154259, 0x01, "RDRAM"), # 3 Death
                (0x1B80BC,0x200,"RDRAM"), # 4 Sound Table
                (0x1051E0, 0xF0, "RDRAM"), # 5 Skybox Table
                (0x1A738C, 0x100, "RDRAM"), # 6 Music Table
                (RECV_INDEX,  0x03, "RDRAM"), # 7 Treasure Free Space
                (0x16523F,  0x1, "RDRAM"), # 8 Firepower, I know I should extend bomber stats for it
                (0x177924,0x4, "RDRAM"), # 9 Radio check
                (0x134800, 0x4, "RDRAM"), #A Current Stage
                (0x410000, 0x4, "RDRAM"), #B Expansion Memory
                ]
            )#0x16523F
            outbound_writes = []
            exp_data = ram_data[0xB]
            adok_bombs = ram_data[1]
            stage_data = ram_data[0]
            bomber_stats = ram_data[2]
            death_read = ram_data[3][0]
            health_cur = bomber_stats[4]
            health_max = bomber_stats[5]
            lives = bomber_stats[3]
            heath_max = bomber_stats[5]
            bomb_type = bomber_stats[0x10]
            gem_checks = exp_data[0]
            #game_start = ram_data[7]
            bagular_clear = stage_data[0x5A]
            recv_index = ram_data[7][0]
            cur_bombs = bomber_stats[0]
            cur_fire = ram_data[8][0]
            cur_stage = int.from_bytes(ram_data[0x0A], byteorder='big')
            radio_check = int.from_bytes(ram_data[9], byteorder='big')
            goal_clear = False
            #dead = ram_data[7]
            #needed_cards = ram_data[6][0]
            #goal_type = ram_data[6][1]

            # Check if game file is loaded
            if stage_data[0] == 0 or stage_data[0] > 6:
                
                return
            
            # Deathlink
            if self.death_link:
                await ctx.update_death_link(self.death_link)
            if self.pending_death_link:
                outbound_writes.append((0x154259, bytearray([0x00]), "RDRAM"))
                self.pending_death_link = False
                self.sending_death_link = True
            if "DeathLink" in ctx.tags  and ctx.last_death_link + 1 < time.time():
                if health_cur == 0 and not self.sending_death_link:
                #if death_read == 0 and not self.sending_death_link:
                    await self.send_deathlink(ctx)
                elif health_cur  != 0:
                    self.sending_death_link = False

            
            # Check Locations
            locs_to_send = set()

             # Adok Bombs
            # Stupid fix to a stupid problem
            if (adok_bombs[0] == 0xAA and adok_bombs[1] == 0x00 and adok_bombs[2] == 0x10):
                pass
            else:
                offset = 0
                for val in adok_bombs:
                    for bit in range(8):
                        loc_id = 0x574950 + (offset *0x10) + bit
                        mask = 1 << bit
                        flag = val & mask
                        if flag and loc_id in ctx.server_locations:
                            locs_to_send.add(loc_id)
                    offset += 1

            # Stage Clears
            offset = 0
            stage_clear_count = 0
            for val in stage_data:
                loc_base = (offset * 0x10) + 0x1348080
                loc_id = loc_base + 8
                if val > 0 and val < 6 and loc_id in ctx.server_locations:
                    locs_to_send.add(loc_id)
                    stage_clear_count += 1
                    if val >= self.point_require:
                        loc_id += 1
                        locs_to_send.add(loc_id)
                offset += 1

            # Gem Checks
            #if self.item_health:
            #logger.warning(f"{ctx.server_locations}")
            for x in range(1,10,1):
                if gem_checks == x:
                    loc_id = 0x1348060 + x
                    
                    if loc_id in ctx.server_locations:
                        locs_to_send.add(loc_id)
            # Radiosanity
            if self.radio:
                loc_id = 0
                if radio_check in RADIO_DUPE:
                    if cur_stage in RADIO_DUPE[radio_check]:
                        loc_id = RADIO_DUPE[radio_check][cur_stage]
                elif radio_check in RADIO_INDEX:
                    loc_id = RADIO_INDEX[radio_check]
                if loc_id in ctx.server_locations:
                    locs_to_send.add(loc_id)

            if locs_to_send != self.local_checked_locations:
                self.local_checked_locations = locs_to_send
                if locs_to_send is not None:
                    await ctx.send_msgs([{"cmd": "LocationChecks", "locations": list(locs_to_send)}])
            #logger.info(stage_code)

            # Handle Items
            # Permanent Items
            bombup = 0
            fireup = 0
            adok = 0
            max_hp = 4
            for item in range(len(ctx.items_received)):
                raw_item = ctx.items_received[item].item
                match raw_item:
                    case 0x16523F: # Bombup
                        bombup += 1
                    case 0x165240: #Fireup
                        fireup += 1
                    case 0x165258: # Vest
                        if self.item_powerup:
                            outbound_writes.append(( 0x165258, (0x01).to_bytes(1, "little"), "RDRAM"))
                    case 0x165245: # Max Health
                        max_hp += 1
                    case 0x165248: # Adok Bomb
                        adok += 1
                        # Used for the lua tracker
                        outbound_writes.append((0x57499,bytearray([adok]), "RDRAM"))
                        # Unlock Bagular
                        if adok >= self.adok_required and stage_data[0x5A] == 0:
                            outbound_writes.append((0x134862,bytearray([0x06]), "RDRAM"))
                    case _: # Stage unlocks
                        if raw_item > 0x134807 and raw_item < 0x134862:
                            if stage_data[raw_item - 0x134808] == 0x00:
                                outbound_writes.append((raw_item, (0x06).to_bytes(1, "little") , "RDRAM"))
                                if raw_item in STAGE_HINT:
                                    logger.info(STAGE_HINT[raw_item])


            if self.item_powerup:
                outbound_writes.append(( 0x16523F,bytearray([bombup]), "RDRAM"))
            if self.item_powerup:
                outbound_writes.append(( 0x165240,bytearray([fireup]), "RDRAM"))
            outbound_writes.append(( 0x51DF0,bytearray([adok]), "RDRAM"))
            #if self.item_health:
            outbound_writes.append(( 0x165245,bytearray([max_hp]), "RDRAM"))

            if len(ctx.items_received) > recv_index:
                raw_item = ctx.items_received[recv_index].item
                match raw_item:
                    case 0x165240: # Bombup
                        if not self.item_powerup:
                            outbound_writes.append(( 0x165240,bytearray([cur_bombs +1]), "RDRAM"))
                    case 0x16523F: #Fireup
                        if not self.item_powerup:
                            outbound_writes.append(( 0x16523F,bytearray([cur_fire + 1]), "RDRAM"))
                    case 0x165244: # Heart
                        outbound_writes.append((raw_item, (heath_max).to_bytes(1, "little") , "RDRAM"))
                    case 0x165243: # 1 UP
                        outbound_writes.append((raw_item, (lives +1).to_bytes(1, "little") , "RDRAM"))
                    case 0x165268: # Power Glove
                        outbound_writes.append((raw_item, (0x01).to_bytes(1, "little") , "RDRAM"))
                    case 0x165250: # Salt Bombs
                        outbound_writes.append((raw_item, (0x01).to_bytes(1, "little") , "RDRAM"))
                        #self.salt_timer = 180
                    case 0x1779F8: # Disabled HUD
                        outbound_writes.append((raw_item, (0x00).to_bytes(1, "little") , "RDRAM"))
                    #case _: # Stage unlocks
                    #    if raw_item > 0x134807 and raw_item < 0x134862:
                    #        if stage_data[raw_item - 0x134808] == 0x00:
                    #            outbound_writes.append((raw_item, (0x06).to_bytes(1, "little") , "RDRAM"))
                    #            if raw_item in STAGE_HINT:
                    #                logger.info(STAGE_HINT[raw_item])
                if raw_item in ITEM_INDEX:
                    # Used for the lua tracker
                    outbound_writes.append((0x5749A, bytearray([ITEM_INDEX[raw_item]]) , "RDRAM"))
                    
                outbound_writes.append((RECV_INDEX, (recv_index +1).to_bytes(1, "little") , "RDRAM"))

            # Handle Trap timers
           # if self.salt_timer > 0:
                #self.salt_timer -= 1
               # if self.salt_timer == 1:
                    #await bizhawk.write(
                            #ctx.bizhawk_ctx,[(0x165250, (0x00).to_bytes(1, "little") , "RDRAM")],)
            # Send Game Clear
            if self.game_goal == 0:
                if  bagular_clear != 0 and bagular_clear != 6:
                    goal_clear = True
                else:
                    goal_clear = False
            elif self.game_goal == 1:
                if adok >= self.adok_required:
                    goal_clear = True
                else:
                    goal_clear = False
            elif self.game_goal == 2:
                if stage_clear_count >= self.stage_total:
                    goal_clear = True
                else:
                    goal_clear = False



            if not ctx.finished_game and goal_clear:
                await ctx.send_msgs([{
                    "cmd": "StatusUpdate",
                    "status": ClientStatus.CLIENT_GOAL
                }])

            # Randomize Sounds
            if self.sound_rando and ram_data[4][3] == 0xB8:
                outbound_writes.append((0x1B80BC, ramdomize_table(ram_data[4],4), "RDRAM"))

            # Randomize Skybox
            if self.sky_rando and ram_data[5][2] == 0x2D:
                outbound_writes.append((0x1051E0, ramdomize_table(ram_data[5],8), "RDRAM"))

            # Randomize Music
            if self.music_rando and ram_data[6][7] == 0xB0:
                outbound_writes.append((0x1A738C, ramdomize_table_with_exclude(ram_data[6],8,[0x00,0x12,0x18,0x1A,0x1D,0x1E,0x1F]), "RDRAM"))

            #if stage_data[0] == 0x06:
            #    resync_game_prog(self.local_checked_locations)
            # Do all writes
            await bizhawk.write(ctx.bizhawk_ctx, outbound_writes)

        except bizhawk.RequestFailedError:
            # The connector didn't respond. Exit handler and return to main loop to reconnect
            pass