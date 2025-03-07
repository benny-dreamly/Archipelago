local stagetable = {
	-- [Stage index]{World,Area,Stage}

	--Bomber
	[0x1] = {1,1,1},
	[0x2] = {1,1,2},
	[0x3] = {1,1,3},
	[0x4] = {1,1,4},
	[0x5] = {1,1,5},

	[0x8] = {1,2,1},
	[0x9] = {1,2,2},
	[0xA] = {1,2,3},
	[0xB] = {1,2,4},
	[0xC] = {1,2,5},
	[0xD] = {1,2,6},
	[0xE] = {1,2,7},

	[0xF] =  {1,3,1},
	[0x10] = {1,3,2},
	[0x11] = {1,3,3},
	[0x12] = {1,3,4},

	--Primus
	[0x16] = {2,1,1},
	[0x17] = {2,1,2},
	[0x18] = {2,1,3},
	[0x19] = {2,1,4},
	[0x1A] = {2,1,5},

	[0x1D] = {2,2,1},
	[0x1E] = {2,2,2},
	[0x1F] = {2,2,3},
	[0x20] = {2,2,4},
	[0x21] = {2,2,5},
	[0x22] = {2,2,6},

	[0x23] = {2,3,1},
	[0x24] = {2,3,2},
	[0x25] = {2,3,3},
	[0x26] = {2,3,4},

	--Kanatia
	[0x2B] = {3,1,1},
	[0x2C] = {3,1,2},
	[0x2D] = {3,1,3},
	[0x2E] = {3,1,4},
	[0x2F] = {3,1,5},

	[0x32] = {3,2,1},
	[0x33] = {3,2,2},
	[0x34] = {3,2,3},
	[0x35] = {3,2,4},
	[0x36] = {3,2,5},
	[0x37] = {3,2,6},
	[0x38] = {3,2,7},

	[0x39] = {3,3,1},
	[0x3A] = {3,3,2},
	[0x3B] = {3,3,3},
	[0x3C] = {3,3,4},
	[0x3D] = {3,3,5},

	--Mazone
	[0x40] = {4,1,1},
	[0x41] = {4,1,2},
	[0x42] = {4,1,3},
	[0x43] = {4,1,4},

	[0x47] = {4,2,1},
	[0x48] = {4,2,2},
	[0x49] = {4,2,3},
	[0x4A] = {4,2,4},
	[0x4B] = {4,2,5},

	[0x4E] = {4,3,1},
	[0x4F] = {4,3,2},
	[0x50] = {4,3,3},
	[0x51] = {4,3,4},
	[0x52] = {4,3,5},

	--Garaden
	[0x55] = {5,1,1},
	[0x56] = {5,1,2},
	[0x57] = {5,1,3},
	[0x58] = {5,1,4},
	[0x59] = {5,1,5},
	[0x5A] = {5,1,6},
	[0x5B] = {5,1,7},

    --Gossick
    --[0x6A] = {5,3,1},
    --[0x6B] = {5,3,2},
    --[0x6C] = {5,3,3},

}

ITEM_TEXT = {
	[0x01] = "I can carry more bombs!",
	[0x02] = "Bombs have been Powered up!",
	[0x03] = "I feel stronger!",
	[0x04] = "My Bombs can't hurt me now!",
	[0x05] = "My Boms are harmless now..",
	[0x06] = "My head hurts.",
	[0x07] = "I feel healthier!",
	[0x08] = "I have more lives!",
	[0x09] = "I found an Adok Bomb!",

	[0x10] = "I can train at Battle Room!",
	[0x11] = "I can train at Hyper Room!",
	[0x12] = "I can train at Secret Room!",
	[0x13] = "I can train at Heavy Room!",
	[0x14] = "I cantrain at Sky Room!",
	[0x15] = "I can go to Blue Cave!",
	[0x16] = "I can go to Hole Lake!",
	[0x17] = "I can go to Red Cave!",
	[0x18] = "I can go to Big Cannon!",
	[0x19] = "It's spooky at Dark Wood!",
	[0x1A] = "I can go to Dragon Road!",
	[0x1B] = "Nitros is at Planet Bomber!",
	[0x1C] = "I can go to Clown Valley!",
	[0x1D] = "I can go to Great Rock!",
	[0x1E] = "I can go to Fog Route!",
	[0x1F] = "I will fight you Endol! ",

	[0x20] = "I can go to Groog Hills!",
	[0x21] = "I can go to Bubble Hole!",
	[0x22] = "I can go to Erars Lake!",
	[0x23] = "I can go to Waterway!",
	[0x24] = "I can go to Water Slider!",
	[0x25] = "I can go to Rockn Road!",
	[0x26] = "I can go to Water Pool!",
	[0x27] = "I can go to Millian Road!",
	[0x28] = "I can go to Warp Room!",
	[0x29] = "I can go to Dark Prison!",
	[0x2A] = "Nitros is waiting for me at Primus!",
	[0x2B] = "I can go to Killer Gate!",
	[0x2C] = "I can go to Spiral Tower!",
	[0x2D] = "I can go to Snake Route!",
	[0x2E] = "Baruda give back the Princess!",

	[0x2F] = "I can go to Hades Crater!",
	[0x30] = "I can go to Magma Lake!",
	[0x31] = "I can go to Magma Dam!",
	[0x32] = "I can go to Crystal Hole!",
	[0x33] = "I can go to Emerald Tube!",
	[0x34] = "I can go to Death Temple!",
	[0x35] = "I can go to Death Road!",
	[0x36] = "I can go to Death Garden!",
	[0x37] = "I can go to Float Zone!",
	[0x38] = "I can go to Aqua Tank!",
	[0x39] = "I can go to Aqua Way!",
	[0x3A] = "Nitros is waiting for me at Kanatia!",
	[0x3B] = "I don't want to go to Hard Coaster..",
	[0x3C] = "I can go to Dark Maze!",
	[0x3D] = "I can go to Mad Coaster!",
	[0x3E] = "I can go to Move Stone!",
	[0x3F] = "I can fight Bolban!",

	[0x40] = "I can go to Hopper Land!",
	[0x41] = "I can go to Junfalls!",
	[0x42] = "I can go to Freeze Lake!",
	[0x43] = "I can go to Cool Cave!",
	[0x44] = "I can go to Snowland!",
	[0x45] = "I can go to Storm Valley!",
	[0x46] = "I can go to Snow Circuit!",
	[0x47] = "I can go to Heaven Sky!",
	[0x48] = "I can go to Eye Snake!",
	[0x49] = "Nitros is waiting for me at Mazone!",
	[0x4A] = "I can go to Air Room!",
	[0x4B] = "I can go to Zero G Room!",
	[0x4C] = "I can go to Mirror Room!",
	[0x4D] = "Time to pay back Natia!",

	[0x4E] = "Time to finish Endol at Garaden!",
	[0x4F] = "Time to finish Baruda at Garaden!",
	[0x50] = "Time to finish Cronus at Garaden!",
	[0x51] = "This is it Nitros, our final battle!",
	[0x52] = "Time to finish Bolban at Garaden!",
	[0x53] = "Time to finish Natia at Garaden!",
	[0x54] = "Time to end this Bagular!",

    --[0x55] = "I can go to Outter Road!",
    --[0x56] = "I can go to Inner Road!",
    --[0x57] = "I can Fight Evil Bomber!",

}

local adokTotal = 0
local item_timer = 0

local function startup()
	memory.usememorydomain("ROM")
	adokTotal = memory.read_u8(0xB864D0)
	memory.usememorydomain("RDRAM")

end

local function print_stages(stage_clears)
	gui.drawText(10,0,"Bomber","#FFFFFF","#000000")
	gui.drawText(10,40,"Primus","#FFFFFF","#000000")
	gui.drawText(10,80,"Kanatia","#FFFFFF","#000000")
	gui.drawText(10,120,"Mazone","#FFFFFF","#000000")
	gui.drawText(10,160,"Garaden","#FFFFFF","#000000")
    --gui.drawText(10,180,"Gossick","#FFFFFF","#000000")
	local adokHave = memory.read_u8(0x57499)
	local adokstr = tostring("Adok Bomb: "..adokHave.."/"..adokTotal)
	gui.drawText(180,0,adokstr,"#FFFFFF","#000000")
	for k, v in pairs(stagetable) do
		local x = v[3] * 10
		local y = ((v[1] * 40)-40) + (v[2] * 10)
		local color = "#FFFFFF"
		if stage_clears[k] == 0 then
			color = "#505050"
		elseif stage_clears[k] == 6 then
			color = "#FFFFFF"
		elseif stage_clears[k] == 5 then
			color = "#FFD700"
		end
		local printval = tostring(stage_clears[k])
		if printval == "6" then
			printval = "0"
		end
		gui.drawText(x,y,printval,color,"#000000")
	end
end

startup()
-- This template lives at `.../Lua/.template.lua`.
while true do
	gui.cleartext()
	gui.clearGraphics()
	-- Code here will run once when the script is loaded, then after each emulated frame.
	--console.log(memory.getcurrentmemorydomain())
	local stage_clears = memory.read_bytes_as_array(0x134808,0x5B)
	--console.log(joypad.get(1)["DPad D"])
	local item_in = memory.read_u8(0x5749A)
	if item_in ~= 0 and item_timer == 0 then
		item_timer = 180
	end
	if item_timer > 0 then
		gui.drawText(10,220,ITEM_TEXT[item_in],"#FFFFFF","#000000")
		item_timer = item_timer - 1
		if item_timer == 1 then
			memory.write_u8(0x5749A, 0x00)
		end
	end
	if joypad.get(1)["DPad D"] == true then
		print_stages(stage_clears)
	end
	emu.frameadvance();
end
