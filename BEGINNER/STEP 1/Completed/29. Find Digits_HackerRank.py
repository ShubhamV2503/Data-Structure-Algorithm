# https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true


import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):

    res = 0

    temp = str(n)

    for i in temp:
        if int(i) !=0 and  n % int(i) == 0:
            res = res + 1

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
