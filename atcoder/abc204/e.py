from prog.abc204.c import dijkstra
from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial

N,M =map(int, input().split())
G=[[] for _ in range(N)]
for _ in range(M):
	A,B,C,D=map(int, input().split())
	A-=1
	B-=1
	G[A].append([B,(C,D)])
	G[B].append([A,(C,D)])


from heapq import heappush, heappop
def dijkstra(graph, s0=0):
	"""
	graph:隣接リスト (nextnode,weight)
	s0:start位置
	return:各頂点の距離
	"""
	dist = [float("inf")] * len(graph)
	que = [(0, s0)]
	dist[s0] = 0
	while que:
		d, now = heappop(que)
		if d<=dist[now]:
			dist[now]=d
			for next, cost in graph[now]:
				if dist[now] + cost <dist[next]:
					heappush(que, (d+cost, next))
	return dist

print(ans[N-1])