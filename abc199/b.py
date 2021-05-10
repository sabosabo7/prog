from sys import exit, stdin, setrecursionlimit

setrecursionlimit(1000000)
import copy

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb

# input = stdin.readline
mod = 1000000007

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = max(min(B) - max(A) + 1, 0)

print(int(ans))