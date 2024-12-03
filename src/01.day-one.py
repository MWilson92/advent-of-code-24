# advent of code 2024
# PART 1
# match lists by lowest number first then find distance between values

import pandas as pd
import numpy  as np
from collections import Counter

# read in data
input_file = "inputs/01.day-one.txt"
df = pd.read_csv(input_file, 
                       sep='   ', 
                       header=None, 
                       names=['v1', 'v2'],
                       engine='python')

# separate columns to sort independently
v1 = df['v1'].to_numpy()
v2 = df['v2'].to_numpy()

v1_sorted = np.sort(v1)
v2_sorted = np.sort(v2)

# add vectors
diff = v1_sorted - v2_sorted

# sum the absolute differences differences
val = sum(np.abs(diff))

print('Part 1: ', val)

# PART 2
# find similarity score by multiplying values in left list by occurences in 
# right list

# after lots of googling and stack overflow reading, using `Counter()` to 
# generate list of occurencecs in list 2. Using list comprehension to match to
# list 1
v2_count = Counter(v2_sorted)
sim_scores = sum(i * v2_count[i] for i in v1_sorted)

print('Part 2: ', sim_scores)
