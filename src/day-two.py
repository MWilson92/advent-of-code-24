# advent of code 2024
# day 2 - PART 1
# finding safe reports. requirements for safe report:
#       - all values in a row must be increasing or decreasing
#       - must change by between 1 and 3

import pandas as pd
import numpy  as np

# read in data
input_file = "inputs/day-two.txt"
raw = open(input_file).read().splitlines()

# create a list of lists to hold our reports and convert to intergers
ls = []
for i in range(0, len(raw)):
    ls.append(np.asarray(list(map(int, raw[i].split()))))

# create list for return objects
safe_recs = []
unsafe_recs = []
safe_recs_tol = []
safe_diff_arr= []

# loop through list and only return true if all conditions are met
for j in ls:
    diff_arr = np.diff(j)
    # check if step is within between 1, -1 and 3, -3
    step_bool = all(((0 < a < 4) or (-4 < a < 0)) for a in diff_arr) 
    # check that all values are postive or negative
    pos_bool = all(b > 0 for b in diff_arr)
    neg_bool = all(c < 0 for c in diff_arr)
    
    # if 2 checks are True then is a safe record
    if step_bool + pos_bool + neg_bool == 2:
        safe_recs.append(j)
    
    else:
        unsafe_recs.append(j)

# print('Part 1: ', len(safe_recs))

# PART 2
# there is now a tolerance for one unsafe value in each report to make it safe.
# after much pain the problem is to actually remove the bad value and test again
# do we now need to check individual values and compile a score?
# we can build off of what we have done already

# need to look in each report, find first problem value, remove, then test again
# but can also just test every permutation
for k in unsafe_recs:
    # create list to hold outcomes of our tests
    test_results = []

    for idl, l in enumerate(k):
        report_copy = np.delete(k, idl)
        diff_arr_us = np.diff(report_copy)

        # check if step is within between 1, -1 and 3, -3
        step_bool = all(((0 < a < 4) or (-4 < a < 0)) for a in diff_arr_us) 
        # check that all values are postive or negative
        pos_bool = all(b > 0 for b in diff_arr_us)
        neg_bool = all(c < 0 for c in diff_arr_us)
    
        # if 2 checks are True then is a safe record
        if step_bool + pos_bool + neg_bool == 2:
            test_results.append(True)
        else:
            test_results.append(False)
    # if a single permutation passed then record is safe
    if any(test_results):
        safe_recs.append(k)

print('Part 2: ', len(safe_recs))
