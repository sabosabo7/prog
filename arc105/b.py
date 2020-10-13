from sys import exit, stdin
import copy
from collections import deque, Counter

# import numpy as np
from math import gcd, comb

input = stdin.readline

(N,) = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = A[0]
for i in range(1, N):
    ans = gcd(ans, A[i])
print(ans)
