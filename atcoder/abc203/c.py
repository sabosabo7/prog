from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial


N,K =map(int, input().split())
# C=[[0,0] for _ in range(N)]
C=[list(map(int, input().split())) for _ in range(N)]
C.sort()
tmp=K
for a,b in C:
	if a>tmp:
		print(tmp)
		exit()
	tmp+=b

print(tmp)
