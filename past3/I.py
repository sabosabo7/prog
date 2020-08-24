import numpy as np
import copy

n = int(input())
q = int(input())

p = [list(map(int, input().split())) for _ in range(q)]

# print(p)
row_idx = np.array([i for i in range(n)])  # 行
col_idx = np.array([j for j in range(n)])  # 列


def value(i, j, n):
    return n * i + j


# print([[value(i, j, n) for j in col_idx] for i in row_idx])

trans = 0
for que in p:
    if que[0] == 3:
        temp = row_idx
        row_idx = col_idx
        col_idx = temp
        trans += 1
    else:
        a = que[1]-1
        b = que[2]-1
        if que[0] == 1:
            temp = row_idx[a]
            row_idx[a] = row_idx[b]
            row_idx[b] = temp

        elif que[0] == 2:
            temp = col_idx[a]
            col_idx[a] = col_idx[b]
            col_idx[b] = temp

        elif que[0] == 4:
            if trans % 2 == 0:
                i = row_idx[a]
                j = col_idx[b]
            else:
                i = col_idx[b]
                j = row_idx[a]
            print(value(i, j, n))
