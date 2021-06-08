from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial


N = int(input())
T = list(map(int, input().split()))

total=sum(T)

dp=[[0]*(total//2+1) for _ in range(N+1)]

dp[0][0]=1


for i in range(1,N+1):
	for j in range(total//2+1):
		if j-T[i-1]>=0:
			dp[i][j]=dp[i-1][j]+dp[i-1][j-T[i-1]]
		else:
			dp[i][j]=dp[i-1][j]

for i in range(total//2,-1,-1):
	if dp[N][i]!=0:
		print(total-i)
		exit()
