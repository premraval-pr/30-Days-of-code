#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    strBin = str(bin(n)[2:])
    result = 0
    consecOnes = []
    for ch in strBin:
        if ch == '1':
            result += 1
        else:
            consecOnes.append(result)
            result = 0
    consecOnes.append(result)
    print(max(consecOnes))
