from sys import exit, stdin, setrecursionlimit

setrecursionlimit(1000000)
import copy

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb

# input = stdin.readline
mod = 1000000007

N, K = map(int, input().split())


dp = [[0] * (3 * N + 2) for _ in range(4)]

dp[0][0] = 1
for i in range(3):
    for j in range(N * i + 1):
        dp[i + 1][j + 1] += dp[i][j]
        dp[i + 1][j + N + 1] -= dp[i][j]
    for j in range(1, N * (i + 1) + 2):
        dp[i + 1][j] += dp[i + 1][j - 1]


for i in range(1, 3 * N + 1):
    if K <= dp[3][i]:
        score = i
        break
    else:
        K -= dp[3][i]


for i in range(1, score - 1):
    jmin = max(1, score - i - N)
    jmax = min(N, score - i - 1)
    if jmin > N or jmax < 1:
        continue
    if K <= jmax - jmin + 1:
        break
    else:
        K -= jmax - jmin + 1

j = jmin + K - 1
k = score - i - j

print(i, j, k)
