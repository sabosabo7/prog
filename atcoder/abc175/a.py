from sys import exit, stdin

# import copy
# from collections import deque,Counter
# import numpy as np
# input = stdin.readline

S = input()

cnt = 0
for s in S:
    if s == "R":
        cnt += 1
    elif cnt>0 and s=="S":
        break
print(cnt)

