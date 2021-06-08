from sys import exit

# import copy
# import numpy as np
# from collections import deque

(N,) = map(int, input().split())

C = list(input())


na = C.count("R")

ans = na - C[0:na].count("R")

print(ans)
