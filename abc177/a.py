#%%
from sys import exit, stdin

input = stdin.readline
import copy

# from collections import deque,Counter
# import numpy as np


D, T, S = list(map(int, input().split()))

if T * S >= D:
    print("Yes")
else:
    print("No")
