from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial

N = int(input())
C = list(map(int, input().split()))

ans = 1
tmp=0
f=0
C.sort()

for c in C:
	if c!=tmp:
		f+=c-tmp
	ans*=f
	ans %= MOD 
	f-=1
	tmp=c


print(ans)
