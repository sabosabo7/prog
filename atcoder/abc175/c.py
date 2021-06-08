from sys import exit, stdin

# import copy
# from collections import deque,Counter
# import numpy as np
input = stdin.readline

X, K, D = map(int, input().split())

if abs(X) >= K * D:
    print((abs(X) - K * D))
else:
    A1 = abs(X) % D
    A2 = abs(A1 - D)
    n = abs(X) // D
    if (K - n) % 2 == 0:
        print(A1)
    else:
        print(A2)

