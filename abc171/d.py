from sys import exit
# import copy
# import numpy as np
# from collections import deque


n, = map(int, input().split())
a = list(map(int, input().split()))
q, = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(q)]

count = [0]*100000
ans = 0
for i in a:
    count[i - 1] += 1
    ans += i

for que in b:
    count[que[1] - 1] += count[que[0] - 1]
    ans += (que[1]-que[0])*count[que[0] - 1]
    count[que[0] - 1] = 0
    print(ans)
