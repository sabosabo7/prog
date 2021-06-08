from sys import exit, stdin, setrecursionlimit

setrecursionlimit(1000000)
import copy

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb

# input = stdin.readline
mod = 1000000007

S = input()

ans = ""
for s in S:
    if s == "6":
        ans += "9"
    elif s == "9":
        ans += "6"
    else:
        ans += s

print(ans[::-1])
