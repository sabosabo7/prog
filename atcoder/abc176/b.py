from sys import exit, stdin

# import copy
# from collections import deque,Counter
# import numpy as np
# input = stdin.readline


N = input()

ans = 0
for i in N:
    ans += int(i)
    ans %= 9

if ans == 0:
    print("Yes")
else:
    print("No")

