from sys import exit, stdin

input = stdin.readline
import copy

# from collections import deque,Counter
import numpy as np

nmod = 1000000007

(N,) = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0
tsum = 0
for i in range(N - 1, 0, -1):
    tsum += A[i]
    tsum %= nmod
    tmp = (A[i - 1] * tsum) % nmod
    ans += tmp
    ans %= nmod

print(int(ans))
