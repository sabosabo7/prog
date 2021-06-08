from sys import exit, stdin

input = stdin.readline
import copy

# from collections import deque,Counter
# import numpy as np

(S,) = input().split()
(T,) = input().split()


ans = 10000
for i in range(len(S) - len(T) + 1):
    cnt = 0
    tmp = S[0 + i : len(T) + i]
    for s, t in zip(tmp, T):
        if s != t:
            cnt += 1
    if cnt == 0:
        ans = 0
        break
    else:
        if ans > cnt:
            ans = cnt


print(ans)
