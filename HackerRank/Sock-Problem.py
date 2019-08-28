#!/bin/python3

import math
import os
import random
import re
import sys


count=0
def sockMerchant(n, a):
    count = 0
    a.sort()
    a.append('#')
    i = 0
    while i<n:
        if a[i]==a[i+1]:
            count = count+1
            i+=2
        else:
            i+=1
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
