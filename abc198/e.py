from sys import exit, stdin, setrecursionlimit

setrecursionlimit(1000000)
import copy

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb
# input = stdin.readline
mod = 1000000007

N = int(input())
C = list(map(int, input().split()))
D = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = list(map(int, input().split()))
    A -= 1
    B -= 1
    D[A].append(B)
    D[B].append(A)

cnt = {}
ans = {}


def dfs(k, i):
    if cnt.get(C[i], 0) == 0:
        ans[i] = True
    cnt[C[i]] = cnt.get(C[i], 0) + 1
    for d in D[i]:
        if d != k:
            dfs(i, d)
    cnt[C[i]] -= 1


dfs(-1, 0)

for i in range(N):
    if ans.get(i, False):
        print(i + 1)
