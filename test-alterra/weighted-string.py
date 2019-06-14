#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'smallestString' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER weight as parameter.
#

def smallestString(weight):
    # Write your code here
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    value_each_alphabet=[]
    A = 1
    iterator = 1
    value_each_alphabet.append(A)
    while(iterator < len(alphabet)):
        result = ((iterator+1)*value_each_alphabet[iterator-1])+value_each_alphabet[iterator-1]
        iterator+=1
        value_each_alphabet.append(result)
    
    length_value_arr = len(value_each_alphabet)
    # initial variabel
    result_alphabet=[]
    result_in_str=""
    # binary search alghoritm
    target = weight
    L = 0
    R = length_value_arr-1
    ketemu = False
    while(L<=R):
        # search mid point
        m = int((L+R)/2)
        if(value_each_alphabet[m] == target):
            ketemu = True
            L = R
            break
        
        if(target < value_each_alphabet[m]):
            R = m - 1
            
        
        if(target > value_each_alphabet[m]):
            L = m + 1

    index_last = R+1
    while(index_last >=0):
        lanjut = True
        while(lanjut):
            if(value_each_alphabet[index_last]<=weight):
                weight-=value_each_alphabet[index_last]
                result_alphabet.append(alphabet[index_last])
            else:
                lanjut = False
        index_last-=1

    for z in reversed(result_alphabet):
        result_in_str +=str(z)

    print(result_in_str) 

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    weight = int(input().strip())

    result = smallestString(weight)

    # fptr.write(result + '\n')

    # fptr.close()
