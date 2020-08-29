from sys import exit, stdin

input = stdin.readline
import copy
from collections import deque, Counter

# import numpy as np


N, M = list(map(int, input().split()))

if M == 0:
    print(1)
    exit()


D = [[] * N]
S = [-1] * N


tmp = 0
ans = 0

for i in range(M):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    D[a].append(b)
    D[b].append(a)
