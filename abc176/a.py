from sys import exit, stdin

# import copy
# from collections import deque,Counter
# import numpy as np
input = stdin.readline

N, X, T = map(int, input().split())

if N % X == 0:
    ans = (N // X) * T
else:
    ans = (N // X + 1) * T

print(ans)
