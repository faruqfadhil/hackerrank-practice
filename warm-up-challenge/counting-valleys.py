#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    UP="U"
    DOWN="D"
    up_count = 0
    down_count = 0
    posisi_permukaan_laut = 0
    jumlah_lembah = 0
    langkah = list(s)
    log=[]
    for i in range(len(langkah)):
        if(langkah[i] == UP):
            up_count+=1
            posisi_permukaan_laut+=1
        else:
            down_count+=1
            posisi_permukaan_laut-=1
        
        if(posisi_permukaan_laut == 0):
            if (langkah[i] == UP ):
                awal = DOWN
            else:
                awal = UP
            log.append(awal)
    for i in range(len(log)):
        if(log[i]==DOWN):
            jumlah_lembah+=1
    return jumlah_lembah
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    # langkah medan
    s = input()

    result = countingValleys(n, s)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
