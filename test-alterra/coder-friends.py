#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'winner' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING erica
#  2. STRING bob
#

def winner(erica, bob):
    # Write your code here
    result_erica = 0
    result_bob = 0
    for e in range(len(erica)):
        if(erica[e] == 'E'):
            result_erica+=1
        elif(erica[e] == 'M'):
            result_erica+=3
        else:
            result_erica+=5
    
    for b in range(len(bob)):
        if(bob[b] == 'E'):
            result_bob+=1
        elif(bob[b] == 'M'):
            result_bob+=3
        else:
            result_bob+=5
    if(result_erica > result_bob):
        return "Erica"
    elif(result_bob > result_erica):
        return "Bob"
    else:
        return "Tie"
        
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    erica = input()

    bob = input()

    result = winner(erica, bob)

    # fptr.write(result + '\n')

    # fptr.close()
