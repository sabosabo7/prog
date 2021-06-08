from sys import exit, stdin, setrecursionlimit

setrecursionlimit(1000000)
import copy

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb

# input = stdin.readline
mod = 1000000007


N, K = map(int, input().split())

for _ in range(K):
    if N % 200 == 0:
        N /= 200
    else:
        N = N * 1000 + 200

print(int(N))
