from sys import exit, stdin
import copy

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb

# input = stdin.readline
mod = 1000000007

N = input()
N = N.strip("0")

ans = "No"
if len(N) % 2 == 0:
    buf = N[int(len(N) / 2) :]
    if N[: int(len(N) / 2)] == buf[::-1]:
        ans = "Yes"
else:
    buf = N[int(len(N) / 2 + 1) :]
    if N[: int(len(N) / 2)] == buf[::-1]:
        ans = "Yes"

print(ans)