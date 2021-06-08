from sys import exit, stdin, setrecursionlimit

setrecursionlimit(1000000)
import copy

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb

# input = stdin.readline
mod = 1000000007


N = int(input())
A = list(map(int, input().split()))


M = [0] * 200

for a in A:
    M[a % 200] += 1

ans = 0
for m in M:
    if m >= 2:
        ans += m * (m - 1) / 2

print(int(ans))
