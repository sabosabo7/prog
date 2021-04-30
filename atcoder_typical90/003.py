from sys import exit, stdin, setrecursionlimit

setrecursionlimit(1000000)
import copy

from collections import deque, Counter

# import numpy as np
# from math import gcd, comb

# input = stdin.readline
mod = 1000000007

N = int(input())

D = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    D[A].append(B)
    D[B].append(A)


def bfs(graf, i0=0, w=[]):
    """
    graf:隣接リスト
    w:辺の重み
    i0:start位置
    return:各頂点の距離
    """
    if w == []:
        w = [1] * len(graf)
    dist = [-1] * len(graf)
    q = deque()
    q.append(i0)
    dist[i0] = 0

    while q:
        now = q.popleft()
        for next in graf[now]:
            if dist[next] == -1 or dist[next] > dist[now] + w[next]:
                dist[next] = dist[now] + w[next]
                q.append(next)
    return dist


dist1 = bfs(D, 0)
s = dist1.index(max(dist1))
dist2 = bfs(D, s)
print(max(dist2) + 1)
