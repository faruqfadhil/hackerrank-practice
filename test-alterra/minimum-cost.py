#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minimizeCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY p
#  2. INTEGER_ARRAY x
#  3. INTEGER_ARRAY y
#

def minimizeCost(p, x, y):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p_count = int(input().strip())

    p = []

    for _ in range(p_count):
        p_item = int(input().strip())
        p.append(p_item)

    x_count = int(input().strip())

    x = []

    for _ in range(x_count):
        x_item = int(input().strip())
        x.append(x_item)

    y_count = int(input().strip())

    y = []

    for _ in range(y_count):
        y_item = int(input().strip())
        y.append(y_item)

    result = minimizeCost(p, x, y)

    fptr.write(str(result) + '\n')

    fptr.close()
