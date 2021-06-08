from sys import exit
import numpy as np

# import copy
# from collections import deque


N, M, X = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]

tmp = float("inf")

for i in range(2 ** N):
    s = np.zeros(M + 1)
    for j in range(N):
        if (i >> j) & 1:
            s += C[j]
    if min(s[1:]) >= X:
        tmp = min(s[0], tmp)

if tmp == float("inf"):
    tmp = -1
print(int(tmp))

