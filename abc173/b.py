from sys import exit
# import copy
# import numpy as np
# from collections import deque


n, = map(int, input().split())

cnt = [0, 0, 0, 0]
for _ in range(n):
    tmp = input()
    if tmp == "AC":
        cnt[0] += 1
    elif tmp == "WA":
        cnt[1] += 1
    elif tmp == "TLE":
        cnt[2] += 1
    elif tmp == "RE":
        cnt[3] += 1

print("AC x", cnt[0])
print("WA x", cnt[1])
print("TLE x", cnt[2])
print("RE x", cnt[3])
