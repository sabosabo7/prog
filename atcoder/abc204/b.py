from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial


N= int(input())
A = list(map(int, input().split()))

ans = 0


for a in A:
	ans+= max(0,a-10)

print(ans)