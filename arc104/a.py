from sys import exit, stdin

input = stdin.readline
import copy

# from collections import deque,Counter
# import numpy as np


A, B = list(map(int, input().split()))

x = int((A + B) / 2)
y = int((A - B) / 2)

print(x, y)
