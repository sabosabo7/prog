#import copy
from collections import deque


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
            if flag == "l":
                return temp
            else:
                return temp[0]
        elif len(temp) > 1:
            return temp
    else:
        temp = [list(map(int, input().split())) for _ in range(n)]
        return temp


n, m = xnxn()
a = xnxn(m)

graph = [[] for _ in range(n+1)]
for g in a:
    graph[g[0]].append(g[1])
    graph[g[1]].append(g[0])

# print(graph)

d = deque([1])
rout = [0]*(n+1)
while d != deque([]):
    pos = d.popleft()
    for i in graph[pos]:
        if rout[i] == 0:
            rout[i] = pos
            d.append(i)


if rout != [0]*(n+1):
    print("Yes")
    for i in rout[2:]:
        print(i)
else:
    print("No")
