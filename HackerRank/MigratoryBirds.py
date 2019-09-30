#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    frequencies = [0] * 6
 
    for ele in arr:
        frequencies[ele] += 1
 
    max_val = 0
    max_idx = 5
     
    for idx in range(5, 0, -1):
        if frequencies[idx] >= max_val:
            max_idx = idx
            max_val = frequencies[idx]
 
    return max_idx
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
