#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt


def block_reader(file):
    entries = []
    
    line = file.readline()
    while line != "\n" and line !="":
        if "HEX" in line:
            line = line.split(":")[0]
            line = line.replace(" ","").replace("HEX","") #remove prefix
            entries.append(line)
        line = file.readline()
    return entries

def pack_blocks(key_array,offset):
    block_dir = []
    for key in key_array: 
        block_dir.append((key,offset))
    return block_dir

def write_to_file(output_file,pack_array):
    for pack in pack_array:
        output_file.write(pack[0]+","+pack[1]+"\n")

DUMP_FILE_NAME = "000025_dump_ksnappy.txt"

OUT_PUT_FILE_NAME = "key_distribution.csv"

f = open(DUMP_FILE_NAME)
of = open(OUT_PUT_FILE_NAME,"w")

line = f.readline()

# counter = 5

offset_array = []

while line: # and counter >= 0:
    if "Data Block #" in line:
        block_position = line.split("@")[1].replace(" ","").replace("\n","")
        block = block_reader(f)
        # offset_array.extend(pack_blocks(block,block_position))
        pack_array = pack_blocks(block,block_position)
        write_to_file(of,pack_array)
    line = f.readline()

of.close()



# print block_reader(f)