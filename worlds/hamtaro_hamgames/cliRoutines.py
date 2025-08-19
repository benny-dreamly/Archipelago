def get_area_move(passes_have):
    # IDX	AREA		BTN 1 SA DA		BTN 2 SA DA		BTN 3 SA DA		BTN 4 SA DA

    # 0A	Studio:		40 00 0A 0B		10 00 0A 0C		80 00 0A 11 
    # 0B	Beach:		10 00 0B 0C		80 00 0B 0C		20 00 0B 0A 
    # 0C	Tennis:		40 00 0C 0B		80 00 0C 11		20 00 0C 0A		10 00 0C 0D
    # 0D	Village:	80 00 0D 10		20 00 0D 0C		10 00 0D 0E
    # 0E	Pool:		80 00 0E 0F		20 00 0E 0D 
    # 0F	Clubhouse:	40 00 0F 0E		80 00 0F 10		20 00 0F 11 
    # 10	Lawn:		40 00 10 0F		20 00 10 11		10 00 10 0F 
    # 11	Stadium:	40 00 11 0C		20 00 11 0A		10 00 11 10

    # 10 Right    20 Left    40 Up  80  Down
    #area_coords = {
    #        0x0A: [21,85],
    #        0x0B: [71,43],
    #        0x0C: [119,44],
    #        0x0D: [166,52],
    #        0x0E: [224,53],
    #        0x0F: [240,160],
    #        0x10: [184,122],
    #        0x11: [95,108],
    #}

    area_sets = {
		0x0A: [ # Studio
				[0x0B,0x0E], # Up
				[0x0C,0x0D,0x0F], # Right
				[0x11,0x10] # Down
				],         
		0x0B: [# Beach
				[0x0D,0x0E,0x0F], # Right
				[0x0C,0x11,0x10], # Down
				[0x0A], # Left
				],
		0x0C: [ # Tennis
				[0x0B], # Up
				[0x11,0x10], # Down
				[0x0A,0x0B], # Left
				[0x0D,0x0E,0x0F], # Right
				],
		0x0D: [ # Village
				[0x10, 0x11,0x0F,0x0E], # Down
				[0x0C, 0x0B,0x0A,], # Left
				[0x0E, 0x0F], # Right
				],
		0x0E: [ # Pool
				[0x0F,0x10,0x11], # Down
				[0x0D,0x0C,0x0A,0x0B], # Left
				],
		0x0F: [ # Clubhouse
				[0x0E,0x0D,0x0B], # Up
				[0x10], # Down
				[0x11,0x0C,0x0A], # Left
				],
		0x10: [ # Lawn
				[0x0D,0x0E,0x0C,0x0F], # Up
				[0x11,0x0A,0x0B], # Left
				[0x0F,0x0E], # Right
				],
		0x11: [ # Stadium
				[0x0C,0x0D,0x0B,0x0A], # Up
				[0x0A,0x0B], # Left
				[0x10,0x0F,0x0E], # Right
				]
    }

    move_bytes = [
        0x40,0x00,0x0A,0x0A, 0x10,0x00,0x0A,0x0A, 0x80,0x00,0x0A,0x0A, 0x10,0x00,0x0B,0x0B,
        0x80,0x00,0x0B,0x0B, 0x20,0x00,0x0B,0x0B, 0x40,0x00,0x0C,0x0C, 0x80,0x00,0x0C,0x0C,
        0x20,0x00,0x0C,0x0C, 0x10,0x00,0x0C,0x0C, 0x80,0x00,0x0D,0x0D, 0x20,0x00,0x0D,0x0D,
        0x10,0x00,0x0D,0x0D, 0x80,0x00,0x0E,0x0E, 0x20,0x00,0x0E,0x0E, 0x40,0x00,0x0F,0x0F,
        0x80,0x00,0x0F,0x0F, 0x20,0x00,0x0F,0x0F, 0x40,0x00,0x10,0x10, 0x20,0x00,0x10,0x10,
        0x10,0x00,0x10,0x10, 0x40,0x00,0x11,0x11, 0x20,0x00,0x11,0x11, 0x10,0x00,0x11,0x11,
    ]

    writeoffset = 0x03
    for sourceArea, moveSets in area_sets.items():
        for moveset in moveSets:
            for area in moveset:
                if area in passes_have:
                    move_bytes[writeoffset] = area
                    break
                move_bytes[writeoffset] = sourceArea
            writeoffset += 4
        #writeoffset += 4

    return move_bytes


def tournyevent(medal_array,placement:int):
	medal_array[placement] += 1
	if placement == 0:
		rainbow_place = 1
		seaham_place = 2
		djungle_place = 3
	elif placement == 1:  
		rainbow_place = 0
		seaham_place = 2
		djungle_place = 3
	elif placement == 2:  
		rainbow_place = 3
		seaham_place = 0
		djungle_place = 1
	elif placement == 3:  
		rainbow_place = 2
		seaham_place = 0
		djungle_place = 1
	medal_array[4 + rainbow_place] += 1
	medal_array[8 + seaham_place] += 1
	medal_array[12 + djungle_place] += 1
	return medal_array

def rainbowWin(medal_array,placement:int,seahamwin:bool):
	if placement == 0:
		rainbow_place = 1
		seaham_place = 2
		djungle_place = 3
	elif placement == 1:  
		rainbow_place = 0
		seaham_place = 2
		djungle_place = 3
	elif placement == 2:  
		rainbow_place = 0
		seaham_place = 1
		djungle_place = 3
	elif placement == 3:  
		rainbow_place = 0
		seaham_place = 1
		djungle_place = 2
	if seahamwin and placement ==1:
		rainbow_place += 2
		seaham_place -= 2
	elif seahamwin:
		rainbow_place += 1
		seaham_place -= 1
	medal_array[placement] += 1
	medal_array[4 + rainbow_place] += 1
	medal_array[8 + seaham_place] += 1
	medal_array[12 + djungle_place] += 1
	return medal_array


def recalculateMedals(place_dict):
	#"tennisprelim":tennis_prelim_flag,
	#"tennis finals":tennis_finals_place,
	#"volleyballprelim":volleyball_prelim_flag,
	#"volleyball finals": volleyball_finals_place,
	#"100hmdash":hamdash_place,
	#"hurdles":hurdles_place,
	#"sailing":sailing_place,
	#"swimming":swim_place,
	#"hammer":hammer_place,
	#"polevault":polevault_place,
	#"triple jump":triple_jump_place,
	#"diving":diving_place,
	#"carrot":carrot_place,
	#"archery":archery_place,
	#"bird back":birdback_place,
	#"sync swim":sync_swim_place,
					#hamham #rainbow #seaham  #djungle
	medal_array = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]
	exclude_list = ["tennisprelim","tennis finals","volleyballprelim","volleyball finals"]
	for event, placement in place_dict.items():
		seahamwin = False
		if event in exclude_list:
			continue
		if event =="swimming" or event =="sailing":
			seahamwin = True
		if placement == 4:
			continue
		medal_array = rainbowWin(medal_array,placement,seahamwin)
	
	if place_dict["tennis finals"] != 4:
		medal_array = tournyevent(medal_array,place_dict["tennis finals"])

	if place_dict["volleyball finals"] != 4:
		medal_array = tournyevent(medal_array,place_dict["volleyball finals"])
	
	for x in range(4):
		medal_array[(x*4)+3] = 0
	return medal_array