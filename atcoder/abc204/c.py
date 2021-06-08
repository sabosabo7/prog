from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

# from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial

from heapq import heappush, heappop
def dijkstra(graph, s0=0):

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

# def bfs(graf, i0=0, w=[]):
# 	"""
# 	graf:隣接リスト (nextnode,wieght)
# 	i0:start位置
# 	return:各頂点の距離
# 	"""
# 	if w == []:
# 		w = 1
# 	dist = [-1] * len(graf)
# 	q = deque()
# 	q.append(i0)
# 	dist[i0] = 0

# 	while q:
# 		now = q.popleft()
# 		for next in graf[now]:
# 			if dist[next] == -1 or dist[next] > dist[now] + w:
# 				dist[next] = dist[now] + w
# 				q.append(next)
# 	return dist


N,M = map(int, input().split())

G=[[] for _ in range(N)]
for _ in range(M):
	a,b = map(int, input().split())
	a-=1
	b-=1
	G[a].append((b,1))

ans=0
for i in range(N):
	# dist=bfs(G,i0=i)
	dist=dijkstra(G,s0=i)
	for d in dist:
		if d!=float('inf'):
			ans+=1
		

print(ans)
