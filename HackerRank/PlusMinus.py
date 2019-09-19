#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    sm = 0
    for x in arr:
        if x > 0:
            pos+=1
        elif x<0:
            neg+=1
        else:
            zero+=1 
        sm = pos+zero+neg
    print(pos/sm)
    print(neg/sm)
    print(zero/sm)
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
