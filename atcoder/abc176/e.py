from sys import exit, stdin

# import copy
from collections import deque, Counter

# import numpy as np
input = stdin.readline

H, W, M = map(int, input().split())

col = Counter()
row = Counter()
D = Counter()
for i in range(M):
    h, w = input().split()
    row.update([h])
    col.update([w])
    D.update([h + w])

rtop = row.most_common(1)[0]
ctop = col.most_common(1)[0]


for c in col.most_common():
    if c[1] < ctop[1]:
        break
    else:
        if D[rtop[0] + c[0]] == 0:
            ans = rtop[1] + c[1]
            break
        else:
            ans = rtop[1] + c[1] - 1

for r in row.most_common():
    if r[1] < rtop[1]:
        break
    else:
        if D[r[0] + ctop[0]] == 0:
            ans2 = r[1] + ctop[1]
            break
        else:
            ans2 = r[1] + c[1] - 1

print(max(ans, ans2))

