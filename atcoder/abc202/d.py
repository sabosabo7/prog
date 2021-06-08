from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10000000)
import copy

# from collections import deque, Counter

# import numpy as np
from math import gcd, comb, factorial

# input = stdin.readline
mod = 1000000007

A, B, K = map(int, input().split())

ans = ""


def num(a, b):
    return factorial(a + b) // factorial(a) // factorial(b)


while True:
    if K <= num(A - 1, B):
        ans += "a"
        A -= 1
    else:
        ans += "b"
        K -= num(A - 1, B)
        B -= 1
    if A == 0 or B == 0:
        ans += "a" * A + "b" * B
        break

print(ans)
