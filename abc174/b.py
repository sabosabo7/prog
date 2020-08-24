from sys import exit

# import copy
# import numpy as np
# from collections import deque

N, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for a in A:
    if a[0] ** 2 + a[1] ** 2 <= D ** 2:
        cnt += 1

print(cnt)
