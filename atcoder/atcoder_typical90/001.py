from sys import exit, stdin, setrecursionlimit

setrecursionlimit(1000000)
import copy

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb

# input = stdin.readline
mod = 1000000007

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

l = 0
r = L // (K + 1) + 1

while r - l > 1:
    p = (l + r) // 2
    tmp = 0
    cnt = 0
    sum = []
    l0 = 0
    for i in range(len(A)):
        if A[i] - l0 >= p:
            cnt += 1
            sum.append(A[i] - l0)
            l0 = A[i]
    if L - l0 >= p:
        sum.append(L - l0)
    else:
        sum[-1] += L - l0
        cnt -= 1

    if cnt >= K:
        l = p
    else:
        r = p

print(l)
