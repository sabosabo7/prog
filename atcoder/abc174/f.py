from sys import exit, stdin
import copy

# import numpy as np
from collections import deque, Counter

N, Q = map(int, stdin.readline().split())
C = list(map(int, stdin.readline().split()))
R = [list(map(int, stdin.readline().split())) for _ in range(Q)]


tmp = Counter([])

q = [copy.deepcopy(tmp)]

for c in C:
    tmp[str(c)] += 1
    q.append(copy.deepcopy(tmp))

for r in R:
    d = q[r[1]] - q[r[0] - 1]
    print(len(d))
