
# https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true

#code

import math
import os
import random
import re
import sys


# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    
    print(sum(arr)-max(arr),end=" ") 
    print(sum(arr)-min(arr))
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


