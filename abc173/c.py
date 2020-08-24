from sys import exit
import copy
import numpy as np
#from collections import deque


h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]
# print(c)


def count(arr):
    cnt = 0
    for l in arr:
        for i in l:
            if i == "#":
                cnt += 1

    return cnt


ans = 0
for i in range(2 ** w):
    tmp = copy.deepcopy(c)
    for j in range(w):
        if ((i >> j) & 1):
            for s in range(h):
                tmp[s][j] = '$'

    for t in range(2 ** h):
        tmp2 = copy.deepcopy(tmp)
        for j in range(h):
            if ((t >> j) & 1):
                for s in range(w):
                    tmp2[j][s] = '$'
        # for l in tmp2:
        #     print(l)
        if count(tmp2) == k:
            ans += 1

print(ans)
