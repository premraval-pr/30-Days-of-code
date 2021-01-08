#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    sol = ""
    for i in range(len(arr)):
        sol += str(arr[len(arr)-i-1])
        sol += " "
    print(sol)
