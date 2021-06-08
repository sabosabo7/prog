from sys import exit, stdin,setrecursionlimit
# setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
# import numpy as np
#from math import gcd, comb, factorial

N,K=map(int, input().split())
A =[list(map(int, input().split())) for _ in range(N)]

def check(l,r):
	mid= (l+r)//2
	S=[[0]*(N+1) for _ in range(N+1)]
	for i in range(N):
		for j in range(N):
			a=(A[i][j]>mid)*1
			S[i+1][j+1]=S[i][j+1]+S[i+1][j]-S[i][j]+a

	for i in range(N-K+1):
		for j in range(N-K+1):
			tmp= S[i+K][j+K]-S[i][j+K]-S[i+K][j]+S[i][j]
			if tmp<(K**2//2+1):
				return [l,mid]

	return [mid,r]

ok_r=10**9+1
ng_l=-1
while ok_r-ng_l!=1:
	ng_l,ok_r=check(ng_l,ok_r)

print(ok_r)
