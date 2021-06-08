from sys import exit, stdin, setrecursionlimit

setrecursionlimit(1000000)
import copy

from collections import deque, Counter

# import numpy as np
# from math import gcd, comb

# input = stdin.readline
mod = 1000000007

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A = Counter(A)
Nb = [[] for _ in range(N + 1)]
for i, b in enumerate(B):
    Nb[b].append(i + 1)

C = Counter(C)

ans = 0

for a, ni in list(A.items()):
    nj = 0
    for b in Nb[a]:
        nj += C[b]
    ans += ni * nj

print(ans)
