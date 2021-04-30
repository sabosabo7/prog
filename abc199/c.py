from sys import exit, stdin, setrecursionlimit

setrecursionlimit(1000000)
import copy

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb

# input = stdin.readline
mod = 1000000007

N = int(input())
S = list(input())
Q = int(input())


flip = False

for _ in range(Q):
    T, A, B = map(int, input().split())
    A -= 1
    B -= 1
    if T == 1:
        if flip:
            A = (A < N) * (A + N) + (A >= N) * (A - N)
            B = (B < N) * (B + N) + (B >= N) * (B - N)
        S[A], S[B] = S[B], S[A]
    else:
        flip = not flip

if flip:
    ans = "".join(S[N:]) + "".join(S[:N])
else:
    ans = "".join(S)

print(ans)
