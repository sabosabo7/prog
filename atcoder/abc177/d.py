from sys import exit, stdin

input = stdin.readline
import copy

# from collections import deque, Counter

# import numpy as np


class UnionFind:
    def __init__(self, N):
        # N = data size
        self.n = N
        self.parents = [-1] * N

    def find(self, x):
        # find x's root
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        # unite x and y
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False
        if -(self.parents[rx]) < -(self.parents[ry]):
            rx, ry = ry, rx
        self.parents[rx] += self.parents[ry]
        self.parents[ry] = rx
        return True

    def size(self, x):
        # size of group of x's root
        return -(self.parents[self.find(x)])

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())


N, M = list(map(int, input().split()))

if M == 0:
    print(1)
    exit()


D = UnionFind(N)

for i in range(M):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    D.union(a, b)

num = [D.size(r) for r in D.roots()]

print(max(num))
