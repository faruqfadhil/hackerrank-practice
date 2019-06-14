#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'investment' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER_ARRAY e
#

def investment(s, e):
    # Write your code here
    list_day = []
    for i in range(len(s)):
        first = s[i]
        last = e[i]
        print("awal")
        while(first<=last):
            if(first not in list_day):
                list_day.append(first)
                print("break")
                break
            first+=1
            
    print(list_day)
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s_count = int(input().strip())

    s = []

    for _ in range(s_count):
        s_item = int(input().strip())
        s.append(s_item)

    e_count = int(input().strip())

    e = []

    for _ in range(e_count):
        e_item = int(input().strip())
        e.append(e_item)

    result = investment(s, e)

    # fptr.write(str(result) + '\n')

    # fptr.close()
