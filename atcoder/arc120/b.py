from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
# import copy
# input = stdin.readline

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb, factorial

H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())

# print(S)
ans = 1
if S[0][0] == ".":
    ans *= 2
if S[H - 1][W - 1] == ".":
    ans *= 2

for d in range(1, H + W - 2):
    cnt = [1, 1]
    for i in range(0, H):
        j = d - i
        if i >= 0 and 0 <= j <= W - 1:
            if S[i][j] == "R":
                cnt[0] = 0
            elif S[i][j] == "B":
                cnt[1] = 0
    ans *= sum(cnt)
    if ans == 0:
        break
    else:
        ans %= 998244353
print(int(ans))
