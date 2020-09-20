from sys import exit, stdin

input = stdin.readline
import copy

# from collections import deque,Counter
# import numpy as np
mod = 10 ** 9 + 7

(N,) = list(map(int, input().split()))
ans = (pow(10, N, mod) + pow(8, N, mod) - 2 * pow(9, N, mod)) % mod

print(ans)
