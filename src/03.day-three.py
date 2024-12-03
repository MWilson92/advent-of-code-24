# Advent of Code 2024
# Day 3 - Part 1
# find valid instructions from the string provided. Valid instructions are:
#  - wrapped in mul()
#  - are numbers 1-3 digits
#  - separated by a comma with no whitespace anywhere

input_file = 'inputs/day-three.txt'
inst_raw = open(input_file).read()

import re

# regex to find the valid instructions. need a string to pass back to findall
inst = ''.join(re.findall("mul\(\d{1,3},\d{1,3}\)", inst_raw))

# need to extract the numbers now
# inst_num = [i for ]
inst_num = re.findall('\d+,\d+', inst)

# split the numbers and convert to ints
inst_ints = [list(map(int, i.split(','))) for i in inst_num]

# multiply the 2 elements
inst_vals = [j[0] * j[1] for j in inst_ints]

print('Part 1: ', sum(inst_vals))

# Part 2
# we now need to handle do() and don't() instructions
# anything preceded by don't() is disabled until reenabled by a do()
# look behind assertions must be fixed length which makes it trickier
# capture all instructions and do(), don't(), then sort from there
inst_all = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", inst_raw)

enabled = True
inst_en_ls = []

for match in inst_all:
    if match.startswith('mul(') and enabled:
        inst_en_ls.append(match)
    elif match == 'do()':
        enabled = True
    else:
        enabled = False

# convert list to string
inst_en = ''.join(inst_en_ls)

inst_en_num = re.findall('\d+,\d+', inst_en)

# split the numbers and convert to ints
inst_en_ints = [list(map(int, k.split(','))) for k in inst_en_num]

# multiply the 2 elements
inst_en_vals = [l[0] * l[1] for l in inst_en_ints]

print('Part 2: ', sum(inst_en_vals))
