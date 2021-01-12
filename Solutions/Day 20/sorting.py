#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numOfSwaps = 0

for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
            numOfSwaps += 1

print("Array is sorted in " + str(numOfSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[len(a)-1]))
