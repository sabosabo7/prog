from sys import exit, stdin, setrecursionlimit

setrecursionlimit(1000000)
import copy

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb

# input = stdin.readline
mod = 1000000007

A, B, C = map(int, input().split())

if A ** 2 + B ** 2 < C ** 2:
    print("Yes")
else:
    print("No")