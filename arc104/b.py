from sys import exit, stdin

input = stdin.readline

import copy

# from collections import deque,Counter
# import numpy as np

L, S = input().split()
L = int(L)

c = [[0, 0, 0, 0] for i in range(L + 1)]


for i in range(1, L + 1):
    c[i] = copy.deepcopy(c[i - 1])

    if S[i - 1] == "A":
        c[i][0] += 1
    elif S[i - 1] == "T":
        c[i][1] += 1
    elif S[i - 1] == "C":
        c[i][2] += 1
    else:
        c[i][3] += 1

num = [0, 0, 0, 0]
ans = 0

for i in range(1, L):
    k = i + 1
    while k <= L:
        for t in range(4):
            num[t] = c[k][t] - c[i - 1][t]
        if num[0] == num[1] and num[2] == num[3]:
            ans += 1
            k += 1
        else:
            k += abs(num[0] - num[1]) + abs(num[2] - num[3])

print(ans)
