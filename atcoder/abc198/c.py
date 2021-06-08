from sys import exit, stdin
import copy

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb

# input = stdin.readline
mod = 1000000007

R, X, Y = list(map(int, input().split()))

dist = (X ** 2 + Y ** 2) ** 0.5

ans = dist // R


if ans == 0:
    ans = 2
elif dist % R == 0:
    pass
else:
    ans += 1

print(int(ans))
