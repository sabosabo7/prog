import numpy as np
import sys
# import copy


def xnxn(n=0):
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
            return temp[0]
        elif len(temp) > 1:
            return temp
    else:
        temp = [list(map(int, input().split())) for _ in range(n)]
        return temp


def sp_xnxn(n=0):
    """
    args:
        int n: a number of lows to read
    example
        input   1
        retrun  [1]

        input   123
        return  [1,2,3]

        input   123
                4
        return  [[1,2,3],
                [4]]
    """
    if n == 0:
        return [int(k) for k in xsxs()]
    else:
        return [[int(k) for k in xsxs()] for _ in range(n)]


def xsxs(n=0):
    """
    args:
        int n: a number of lows to read
    example:
        input   AA
        retrun  AA

        input   A BBB CC
        return  ["A","BBB","CC"]

        input   A BB CCC
                D
        return  [["A","BBB","CC"],
                ["D"]]
    """
    if n == 0:
        temp = list(input().split())
        if len(temp) == 1:
            return temp[0]
        elif len(temp) > 1:
            return temp
    else:
        return [list(input().split()) for _ in range(n)]


def sp_xsxs(n=0):
    """
    args:
        int n: a number of lows to read
        example:
            input   A
            retrun  ["A"]

            input   ABC
            return  ["A","B","C"]

            input   ABC
                    D
            return  [["A","B","C"],
                    ["D"]]
    """
    if n == 0:
        return [s for s in xsxs()]
    else:
        return [[s for s in xsxs()] for _ in range(n)]


def dt(arr):
    return [-arr[1]+201, arr[0]+201]


n, x, y = xnxn()
d = xnxn(n)


grid = np.zeros((403, 403))

for a in d:
    i, j = dt(a)
    grid[i, j] = -1

i_goal, j_goal = dt([x, y])
# print(grid[i_goal:201+1, 201:j_goal+1])

que = []
d_now = [0, 0]
while True:
    x_now, y_now = d_now
    i_now, j_now = dt(d_now)
    for d_next in [[x_now + 1, y_now + 1], [x_now, y_now + 1], [x_now - 1, y_now + 1], [x_now + 1, y_now], [x_now - 1, y_now], [x_now, y_now - 1]]:
        i_next, j_next = dt(d_next)
        if d_next == [0, 0] or d_next[0] > 201 or d_next[0] < -201 or d_next[1] > 201 or d_next[1] < -201:
            continue
        elif grid[i_next, j_next] == 0.0:
            que.append(d_next)
            grid[i_next, j_next] = grid[i_now, j_now]+1
            if d_next == [x, y]:
                print(int(grid[i_next, j_next]))
                # print(grid[i_goal:201+1, 201:j_goal+1])
                sys.exit()
    if que == []:
        print(-1)
        sys.exit()
    d_now = que.pop(0)
