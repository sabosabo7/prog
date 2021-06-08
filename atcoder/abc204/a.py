from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial

x,y = map(int, input().split())


if x==y:
	print(x)
	exit()

ans=[0,0,0]

ans[x]=1
ans[y]=1

for i in range(3):
	if ans[i]==0:
		print(i)
