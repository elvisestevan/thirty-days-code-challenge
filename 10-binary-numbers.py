#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    b = "{0:b}".format(n)
    max_1_in_a_row = 0
    number_1_in_a_row = 0

    for i in range(len(b)):
        if b[i] == "1":
            number_1_in_a_row += 1
            if number_1_in_a_row > max_1_in_a_row:
                max_1_in_a_row = number_1_in_a_row
        else:
            number_1_in_a_row = 0
    
    print(max_1_in_a_row)

    
