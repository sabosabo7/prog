from sys import exit, stdin

# import copy
# from collections import deque,Counter
# import numpy as np
input = stdin.readline

H, W = map(int, input().split())
C = list(map(int, input().split()))
D = list(map(int, input().split()))
S = [list(input().split()) for _ in range(H)]
