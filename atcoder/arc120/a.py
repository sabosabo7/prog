from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
# import copy
# input = stdin.readline

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb, factorial

N = int(input())
A = list(map(int, input().split()))

add = 0
sum = 0
a_max = 0

for i, a in enumerate(A):
    a_max = max(a_max, a)
    add += a
    sum += add
    print(sum + a_max * (i + 1))
