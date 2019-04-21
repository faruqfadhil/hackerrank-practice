#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    cumulus = 0
    cumulus_index = []
    hasil = 0 
    for i in range(len(c)):
        if(c[i]==cumulus):
            cumulus_index.append(i)

    next_index = 0
    while next_index < len(cumulus_index)-1:
        if(cumulus_index[next_index]+2 in cumulus_index):
            # get index
            hasil+=1 
            idx = cumulus_index[next_index]+2
            for j in range(len(cumulus_index)):
                if(idx == cumulus_index[j]):
                    next_index = j

        elif(cumulus_index[next_index]+1 in cumulus_index):
            hasil+=1
            idx = cumulus_index[next_index]+1
            for j in range(len(cumulus_index)):
                if(idx == cumulus_index[j]):
                    next_index = j
            
    return hasil
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)