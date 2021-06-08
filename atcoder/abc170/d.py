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


n = xnxn()
if n == 1:
    print(1)
    sys.exit()

a = xnxn()

a.sort()

a_max = max(a)

dp = [1] * (a_max+1)


if a[0] != a[1]:
    count = 1
else:
    count = 0
for k in range(1, a_max // a[0]+1):
    dp[a[0] * k] = 0

for i in range(1, n):
    if dp[a[i]] == 1:
        for k in range(1, a_max // a[i]+1):
            dp[a[i] * k] = 0
        if i+1 < n and a[i] == a[i+1]:
            continue
        count += 1

print(count)
