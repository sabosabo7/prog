from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
import numpy as np
#from math import gcd, comb, factorial

N=int(input())

S=np.array([list(map(int, input().split())) for _ in range(N)])
T=np.array([list(map(int, input().split())) for _ in range(N)])

Gs=np.sum(S)/N
Gt=np.sum(T)/N

S-=Gs
T-=Gt

for i in range()
