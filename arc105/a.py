from sys import exit, stdin
import copy

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb

input = stdin.readline
mod = 1000000007

A = list(map(int, input().split()))
A = A[::-1]
a = sum(A)


for i in range(2 ** 4):
    eat = 0
    for j in range(4):
        if (i >> j) & 1:
            eat += A[j]
    if eat * 2 == a:
        print("Yes")
        exit()

print("No")
