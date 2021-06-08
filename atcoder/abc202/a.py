from sys import exit, stdin, setrecursionlimit
setrecursionlimit(1000000)
# import copy
# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb
# input = stdin.readline

mod = 1000000007
a, b, c = map(int, input().split())

print(int(21 - a - b - c))
