#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the oddNumbers function below.
def oddNumbers(l, r):
    odd = l
    arr= []
    while(odd <= r):
        if( odd%2 == 1):
            arr.append(odd)
        odd+=1
    return arr

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    res = oddNumbers(l, r)

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')

    # fptr.close()
