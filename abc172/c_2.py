from sys import exit
from collections import deque
# import copy
# import numpy as np
# from collections import deque

n, m, k = map(int, input().split())
a = deque(list(map(int, input().split())))
b = deque(list(map(int, input().split())))

cnt = 0

while k >= a[0] or k >= b[0]:
    if a[0] < b[0]:
        k -= a.popleft()
        cnt += 1

    elif a[0] > b[0]:
        k -= b.popleft()
        cnt += 1
    else:
        for i in range(1, min(len(a), len(b))):
            if a[i] < b[i]:
                for t in range(0, i):
                    if k < a[0]:
                        break
                    k -= a.popleft()
                    cnt += 1
                break
            elif a[i] > b[i]:
                for t in range(0, i):
                    if k < b[0]:
                        break
                    k -= b.popleft()
                    cnt += 1
                break
        else:
            if len(a) > len(b):
                for i in range(len(b)):
                    if k < a[0]:
                        break
                    k -= a.popleft()
                    cnt += 1
            else:
                for i in range(len(a)):
                    if k < b[0]:
                        break
                    k -= b.popleft()
                    cnt += 1
    if a == deque([]):
        for i in range(len(b)):
            if k < b[0]:
                break
            k -= b.popleft()
            cnt += 1
        break
    if b == deque([]):
        for i in range(len(a)):
            if k < a[0]:
                break
            k -= a.popleft()
            cnt += 1
        break
print(cnt)
