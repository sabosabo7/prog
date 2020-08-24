# import numpy as np
import sys
# import copy


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


n, k = xnxn()
a = xnxn(flag="l")
for _ in range(k):
    tmp = [0]*(n+1)
    for i in range(0, n):
        l = max(0, i - a[i])
        r = min(n, i + a[i]+1)
        tmp[l] += 1
        tmp[r] -= 1
    for i in range(1, n):
        tmp[i] += tmp[i - 1]
    if a == tmp:
        break
    a = tmp

for i in a[:n]:
    print(i, end=" ")
