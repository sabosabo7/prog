from sys import exit, stdin, setrecursionlimit

setrecursionlimit(1000000)
import copy

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb

# input = stdin.readline
mod = 1000000007

N = int(input())

if N % 2 == 1:
    pass
else:

    for i in range(2 ** N - 1):
        s = ""
        for j in range(N - 1, -1, -1):
            if i & (1 << j):
                s += ")"
            else:
                s += "("

        l = 0
        r = 0
        for k in s:
            if k == "(":
                l += 1
            else:
                r += 1
            if l < r:
                break
        else:
            if l == r:
                print(s)
