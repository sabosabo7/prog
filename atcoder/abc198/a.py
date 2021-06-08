from sys import exit, stdin
import copy

# from collections import deque, Counter
# import numpy as np
from math import gcd, comb

# input = stdin.readline
mod = 1000000007

N = int(input())

ans = 0
if N == 1:
    ans = 0
elif N == 2:
    ans = 1
else:
    ans = N - 1

print(ans)
