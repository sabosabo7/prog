from sys import exit, stdin

# import copy
# from collections import deque,Counter
# import numpy as np
input = stdin.readline


(N,) = map(int, input().split())

A = list(map(int, input().split()))

ans = 0
lmax = 0
for n in A:
    if n < lmax:
        ans += lmax - n
    else:
        lmax = n

print(ans)
