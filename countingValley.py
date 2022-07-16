
import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    height = 0
    valley = 0
    isSeaLevel = True
    for letter in path:
        if isSeaLevel:
            isSeaLevel =False 
            if letter =='D':
                height -=1
                valley +=1
            else:
                height +=1
            continue
        if letter =='D':
            height -=1
        if letter =='U':
            height +=1
        if (height == 0):
            isSeaLevel = True
    return valley
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
