from sys import exit
#import copy
#import numpy as np
#from collections import deque


W, H, M, N = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(M)]
A = [list(map(int, input().split())) for _ in range(N)]


D = [["." for _ in range(W + 1)] for _ in range(H + 1)]
for q in C:
    x = q[0]
    y = q[1]
    t = q[2]
    r = q[3]
    D[y][x] = "c"
    for yi in range(H + 1):
        for xi in range(W + 1):
            if (yi-y) ^ 2+(yi-y) ^ 2
