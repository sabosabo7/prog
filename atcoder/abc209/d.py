from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial

from collections import deque
def bfs(graph, s0=0):
	"""
	graph:隣接リスト (nextnode)
	s0:start位置
	return:各頂点の距離
	"""
	dist = [-1] * len(graph)
	que = deque()
	que.append(s0)
	dist[s0] = 0
	
	while que:
		now = que.popleft()
		for next in graph[now]:
			if dist[next] == -1:
				dist[next] = (dist[now] + 1)%2
				que.append(next)
	return dist
	
N,Q=map(int, input().split())


D = [[] for _ in range(N)]
for _ in range(N-1):
	A, B = map(int, input().split())
	A -= 1
	B -= 1
	D[A].append(B)
	D[B].append(A)


G=bfs(D)
for _ in range(Q):
	c,d = map(int, input().split())
	c-=1
	d-=1
	if G[c]==G[d]:
		print("Town")
	else:
		print("Road")
