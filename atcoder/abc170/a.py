#import numpy as np
import sys
#from collections import deque
#import copy


def xnxn(n=0, flag="v"):
    """
    args:
        int n: a number of lows to read
    example:
        input   1
        retrun  1

        input   1 2 3
        return  [1,2,3]
        input   1 2 3
                4 
        return  [[1,2,3],
                [4]]
    """
    if n == 0:
        temp = list(map(int, input().split()))
        if len(temp) == 1:
            if flag == "l":
                return temp
            else:
                return temp[0]
        elif len(temp) > 1:
            return temp
    else:
        temp = [list(map(int, input().split())) for _ in range(n)]
        return temp


x = xnxn()

for i in range(5):
    if x[i] == 0:
        print(i+1)
