import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    for x in range(10):
        result = (n) * (x+1);
        print(str(n) + " x " + str(x+1) + " = " + str(result))
