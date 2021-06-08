from sys import exit

# import copy
# import numpy as np
from collections import deque, Counter


(K,) = map(int, input().split())

q = Counter([])
tmp = K

if K % 2 == 0 or K % 5 == 0:
    print(-1)
    exit()


if K % 7 == 0:
    L = 9 * K / 7
else:
    L = 9 * K

tmp = 10

for i in range(1, 10 ** 9):
    if tmp > L:
        tmp = tmp % L
    if tmp % L == 1:
        print(i)
        exit()
    tmp *= 10

