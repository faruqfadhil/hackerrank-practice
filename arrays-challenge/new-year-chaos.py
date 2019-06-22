#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
# keyword bubble sort

def minimumBribes(q):
    # bubble sort
    did_swap = True
    chaotic = False
    pos_akhir = len(q)-2
    count_swap = 0
    count_each_swap = 0
    arr_swapped = []
    swapped_count = []
    while(pos_akhir >= 0 or did_swap):
        index = 0
        did_swap = False
        while(index <= pos_akhir):
            if(q[index] > q[index+1]):
                if(q[index] not in arr_swapped):
                    arr_swapped.append(q[index])
                    swapped_count.append(1)
                else:
                    swapped_index = arr_swapped.index(q[index])
                    swapped_count[swapped_index]+=1

                count_swap+=1
                temp = q[index]
                q[index] = q[index+1]
                q[index+1] = temp
                did_swap = True
            index+=1
        pos_akhir-=1        

    for i in range(len(swapped_count)):
        if(swapped_count[i] >2):
            chaotic = True
            break
    if(chaotic):
        print("Too chaotic")
    else:
        print(count_swap)

    # print(q)
    # print(count_swap)
    # print(arr_swapped)
    # print(swapped_count)

    # array_short = q[:]
    # array_short.sort()
    # last_index = len(q)-1
    # total_bribes = 0
    # i = last_index
    # chaotic = False
    # while(i>=0):
    #     print("se = "+str(array_short[i]))
    #     dynamic_array = q[0:last_index+1]
    #     print("dynamic array")
    #     print(dynamic_array)
    #     print("=============")
    #     bribes_count = 0
    #     if(array_short[i] in dynamic_array):
    #         bribes_count = abs(q.index(array_short[i]) - i)
    #         last_index = q.index(array_short[i])
    #     i-=1
    #     print("count = "+str(bribes_count))
    #     if(bribes_count > 2):
    #         chaotic = True
    #         print("Too chaotic")
    #         break
    #     else:
    #         total_bribes+=bribes_count
    
    # if(chaotic == False):
    #     print(total_bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
