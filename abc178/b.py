from sys import exit, stdin

input = stdin.readline
import copy

# from collections import deque,Counter
# import numpy as np
a, b, c, d = list(map(int, input().split()))


ans = max([a * c, a * d, b * c, b * d])

print(ans)
