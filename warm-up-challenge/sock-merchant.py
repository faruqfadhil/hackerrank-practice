# import numpy as np
# n = input()
# ar = input().split()
# x = np.array(ar)
# distinct = np.unique(x)
# pairs = 0
# indicator = 0
# for i in range(len(distinct)):
#     # cek = indicator%2
#     a = int(indicator/2)
#     pairs+=a
#     indicator = 0
#     for j in range(len(x)):
#         if(distinct[i] == x[j]):
#             indicator+=1
# print(pairs)
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    unique_list = []
    pairs=0
    indicator=0
    for x in ar:
        if x not in unique_list:
            unique_list.append(x)

    for i in range(len(unique_list)):
        for j in range(len(ar)):
            if(int(unique_list[i]) == int(ar[j])):
                indicator+=1
        print("unik ke-"+str(unique_list[i]))
        print("indicator = "+str(indicator))
        a = int(indicator/2)
        print("nilai a = "+str(a))
        pairs+=a
        print("pairs saat ini= "+str(pairs))
        indicator = 0
        
    return pairs
    # return len(unique_list)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
