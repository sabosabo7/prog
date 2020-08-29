from sys import exit, stdin

input = stdin.readline
import copy
from collections import deque, Counter

# import numpy as np


N, M = list(map(int, input().split()))

if M == 0:
    print(1)
    exit()


D = [-1] * N
S = [[] * N]


tmp = 0
for i in range(M):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    if D[a] == -1 and D[b] == -1:
        D[a] = tmp
        D[b] = tmp
        tmp += 1
    elif D[a] == -1 and D[b] != -1:
        D[a] = D[b]
    elif D[a] != -1 and D[b] == -1:
        D[b] = D[a]
    elif D[a] != D[b]:
        S[a].append(b)
        S[b].append(a)

        # for k in range(N):
        #     if D[k] == D[b]:
        #         D[k] = a


R = Counter(D)
ans = R.most_common(2)
if ans[0][0] == -1:
    print(ans[1][1])
else:
    print(ans[0][1])
