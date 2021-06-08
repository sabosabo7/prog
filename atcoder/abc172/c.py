from sys import exit
import copy
# import numpy as np
from collections import deque

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0


a.insert(0, 0)
b.insert(0, 0)


for i in range(1, n+1):
    a[i] += a[i-1]

for i in range(1, m+1):
    b[i] += b[i-1]

tmp = m
for i in range(n+1):
    for j in range(tmp, -1, -1):
        if a[i] + b[j] <= k:
            cnt = max(cnt, i + j)
            tmp = j
            break


print(cnt)
