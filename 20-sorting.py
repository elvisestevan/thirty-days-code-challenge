#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

def swap(list_sort, i, j):
    aux = list_sort[i]
    list_sort[i] = list_sort[j]
    list_sort[j] = aux

numberOfSwaps = 0

for i in range(n):    
    
    for j in range(n - 1):
        if (a[j] > a[j + 1]):
            swap(a, j, j + 1)
            numberOfSwaps += 1
    
    if (numberOfSwaps == 0):
        break

print("Array is sorted in {} swaps.".format(numberOfSwaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[n - 1]))
