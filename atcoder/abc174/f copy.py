# import numpy as np
from sys import exit, stdin
import copy
from collections import deque, Counter

input = stdin.readline


class BIT:
    def __init__(self, a=0):
        self.n = a
        self.d = [0] * (a + 1)

    def add(self, i, x=1):
        i += 1
        while i <= self.n:
            self.d[i] += x
            i += i & (-i)

    def sum(self, *i):
        if len(i) == 1:
            x = 0
            tmp = i[0] + 1
            while tmp:
                x += self.d[tmp]
                tmp -= tmp & (-tmp)
            return x
        else:
            return sum(self, i[1] - 1) - sum(self, i[0] - 1)


N, Q = map(int, input().split())
C = list(map(int, input().split()))

app = [-1] * (N + 1)
ps = [[] for _ in range(N)]
for i in range(N):
    tmp = app[C[i]]
    if tmp != -1:
        ps[tmp].append(i)
    app[C[i]] = i

qs = [[] for _ in range(N)]
for i in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    qs[l].append(copy.deepcopy([r, i]))

ans = [0] * Q
d = BIT(N)
for x in range(N - 1, -1, -1):
    for y in ps[x]:
        d.add(y, 1)
    for p in qs[x]:
        r = p[0]
        i = p[1]
        ans[i] = (r - x + 1) - d.sum(r)

for re in ans:
    print(re)
