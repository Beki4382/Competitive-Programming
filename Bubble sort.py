
import math
import os
import random
import re
import sys


def countSwaps(a):
    count = 0
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j+1]:
                count = count + 1
                a[j], a[j+1] = a[j+1], a[j]
    txt = "Array is sorted in {} swaps."
    print(txt.format(count))
    firstElement = "First Element: {}"
    print (firstElement.format(a[0]))
    lastElement = "Last Element: {}"
    print (lastElement.format(a[-1]))
    
    return 
            

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
