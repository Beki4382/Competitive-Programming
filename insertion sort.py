import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    for i in range(1, n):
        key = arr[-1 * (i)]
        j = -1 * (i + 1)
        while j<=0 and key < arr[j]:
            arr[j+1] = arr [j] 
            print(*arr, sep = " ")
            j = j-1
        arr[j+1] = key
    print (*arr, sep = " ")
          
   

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
