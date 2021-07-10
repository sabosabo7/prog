from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial
N=int(input())
S = [list(map(int, input().split())) for _ in range(N)]

S.sort(key= lambda x:x[1])
cnt=0
for i in range(N-1):
	i_t,i_l,i_r =S[i]
	for j in range(i+1,N):
		j_t,j_l,j_r =S[j]
		if i_r<j_l:
			break
		if i_t==1 or i_t==3:
			if j_t==1 or j_t==2:
				if j_l<=i_r:
					cnt+=1
			else:
				if j_l<i_r:
					cnt+=1
		else:
			if j_l<i_r:
				cnt+=1

print(cnt)
