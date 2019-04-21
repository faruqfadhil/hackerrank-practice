#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    constan = 'a'
    index_constan = []
    karakter = list(s)
    panjang = len(karakter)
    for i in range(panjang):
        if(karakter[i]==constan):
            index_constan.append(i)
    banyaknya_constan = len(index_constan)
    pembagi = int(n/panjang)
    sisa = n%panjang
    jumlah_constan = pembagi*banyaknya_constan
    for j in range(0,sisa):
        if(karakter[j]==constan):
            jumlah_constan+=1
    return jumlah_constan
    # print(index_constan)
    # print(int(10/3))
    # for i in range(0,n):
        
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
