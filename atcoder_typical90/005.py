from sys import exit, stdin, setrecursionlimit

setrecursionlimit(1000000)
import copy

# from collections import deque, Counter
import numpy as np

# from math import gcd, comb

# input = stdin.readline
MOD = 1000000007

N, B, K = map(int, input().split())

C = list(map(int, input().split()))


x = np.zeros(B)
for c in C:
    x[c % B] += 1

A = np.zeros((B, B))

for i in range(B):
    for c in C:
        A[(i * 10 + c) % B, i] += 1

print(x)


def my_pow(x, n):
    if n == 0:
        return np.eye(x.shape[0])
    if n % 2 == 0:
        tmp = my_pow(x, n // 2)

        return np.dot(tmp, tmp) % MOD
    else:
        tmp = my_pow(x, n // 2)
        return np.dot(x, np.dot(tmp, tmp)) % MOD


ans = np.dot(my_pow(A, N - 1), x) % MOD

print(int(ans[0]))
