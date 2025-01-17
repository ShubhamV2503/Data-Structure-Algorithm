# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true



import math
import os
import random
import re
import sys



def divisibleSumPairs(n, k, a):

    counter = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if i < j:
                if (a[i] + a[j]) %k == 0:
                    counter = counter + 1
    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
