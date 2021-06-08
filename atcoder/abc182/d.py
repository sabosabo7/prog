from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

input = stdin.readline
mod = 1000000007

N,=list(map(int, input().split()))
A=list(map(int, input().split()))

dsum=[0]*N
dsum[0]=A[0]
for i in range(1,N):
    dsum[i]=dsum[i-1]+A[i]

tmp=0
ans=0
for s in dsum:
    tmp+=s
    ans=max(ans,tmp)

print(ans) 
