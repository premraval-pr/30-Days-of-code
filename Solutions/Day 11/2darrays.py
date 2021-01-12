#!/bin/python3

import math
import os
import random
import re
import sys

arr = []
def get_hourglass_sum(i,j):
    return arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

if __name__ == '__main__':

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    total = None
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            if i < (len(arr)-2) and j < (len(arr[0])-2):
                hourglass = get_hourglass_sum(i,j)
                if total is None:
                    total = hourglass
                else:
                    total = total if total > hourglass else hourglass
    
    print(total)
