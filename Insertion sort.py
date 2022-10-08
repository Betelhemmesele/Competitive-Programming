#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for k in range(1,n):
        key=arr[k]
        i=k-1
        while i>=0 and key < arr[i]:
            arr[i+1]=arr[i]
            i=i-1
            print(*arr)
        arr[i+1]=key
    print(*arr)
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().strip().split()))

    insertionSort1(n, arr)
