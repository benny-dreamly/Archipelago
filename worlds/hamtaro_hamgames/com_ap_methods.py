import random

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

def shuffle_dict(in_dict):
    value_list = list(in_dict.values())
    random.shuffle(value_list)
    shuffled_dict = {}
    keys_list = list(in_dict.keys())
    for i, key in enumerate(keys_list):
        shuffled_dict[key] = value_list[i]
    return shuffled_dict

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

def randomize_multi_table(tbl,size1,tb2,size2,excepts):
    split_table1 = split_into_xbit_chunks(tbl,size1)
    split_table2 = split_into_xbit_chunks(tb2,size2)
    idxshuffle = []
    new_table1 = []
    new_table2 = []
    for x in range(len(split_table1)):
        idxshuffle.append(x)
        new_table1.append(b'/x00')
        new_table2.append(b'/x00')
    random.shuffle(idxshuffle)