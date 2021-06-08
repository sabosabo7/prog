#import numpy as np
#import sys
#import copy


def xnxn(n=0, flag="v"):
    """
    args:
        int n: a number of lows to read
    example:
        input   1
        retrun  1

        input   1 2 3
        return  [1,2,3]
        input   1 2 3
                4 
        return  [[1,2,3],
                [4]]
    """
    if n == 0:
        temp = list(map(int, input().split()))
        if len(temp) == 1:
            if flag == "1":
                return temp
            else:
                return temp[0]
        elif len(temp) > 1:
            return temp
    else:
        temp = [list(map(int, input().split())) for _ in range(n)]
        return temp


n, m, q = xnxn()
u = [list(map(int, input().split())) for _ in range(m)]
c = list(map(int, input().split()))
s = xnxn(q)

graph = [[] for _ in range(n)]

for i in range(m):
    graph[u[i][0]-1].append(u[i][1]-1)
    graph[u[i][1]-1].append(u[i][0]-1)

for que in s:
    if que[0] == 1:
        print(c[que[1] - 1])
        for idx in graph[que[1] - 1]:
            c[idx] = c[que[1] - 1]
    elif que[0] == 2:
        print(c[que[1] - 1])
        c[que[1] - 1] = que[2]
