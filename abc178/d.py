from sys import exit, stdin

input = stdin.readline
import copy
from scipy.special import comb


# from collections import deque,Counter
# import numpy as np

(S,) = list(map(int, input().split()))
i = 0
s = S - 3
ans = 0
while s >= 0:
    ans = (ans + comb(s + i, i, exact=True)) % (10 ** 9 + 7)
    i += 1
    s -= 3


print(int(ans % (10 ** 9 + 7)))
