from sys import exit, stdin, setrecursionlimit

setrecursionlimit(1000000)
import copy

# from collections import deque, Counter
# import numpy as np

# from math import gcd, comb

input = stdin.readline
mod = 1000000007

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
sum_row = [0] * H
sum_col = [0] * W
for i in range(H):
    for j in range(W):
        sum_row[i] += A[i][j]
        sum_col[j] += A[i][j]

B = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        B[i][j] = sum_row[i] + sum_col[j] - A[i][j]

for l in B:
    print(*l)
