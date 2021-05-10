from sys import exit, stdin, setrecursionlimit

setrecursionlimit(1000000)
import copy

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb

# input = stdin.readline
mod = 1000000007


N = int(input())
A = list(map(int, input().split()))

N = min(8, N)

D = [-1] * 200
for i in range(1, 2 ** N):
    mod = 0
    for j in range(N):
        if i & (1 << j):
            mod += A[j] % 200
    mod %= 200
    if D[int(mod)] == -1:
        D[int(mod)] = i
    else:
        print("Yes")
        ans = ""
        x = 0
        for k in range(N):
            if D[int(mod)] & (1 << k):
                ans += " " + str(k + 1)
                x += 1
        print(str(x) + ans)

        ans = ""
        y = 0
        for k in range(N):
            if i & (1 << k):
                ans += " " + str(k + 1)
                y += 1
        print(str(y) + ans)

        exit()
else:
    print("No")
