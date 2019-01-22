#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []
    soma = 0
    max_soma = float("-inf")

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(4):
        for j in range(4):
            soma = arr[i][j]
            soma += arr[i][j + 1]
            soma += arr[i][j + 2]
            soma += arr[i + 1][j + 1]
            soma += arr[i + 2][j]
            soma += arr[i + 2][j + 1]
            soma += arr[i + 2][j + 2]
            if soma > max_soma:
                max_soma = soma

    print(max_soma)
