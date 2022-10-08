import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    no=0
    new=0

    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                new=a[j]
                a[j]=a[j+1]
                a[j+1]=new
                no=no+1
    print(f"Array is sorted in {no} swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])
if __name__ == '__main__':
    n = int(input())
    
    #a = [int(i) for i in input().strip().split(' ')]
    a = list(map(int, input().strip().split()))

    countSwaps(a)
