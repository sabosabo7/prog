from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb
import bisect

input = stdin.readline
mod = 1000000007

N,M =list(map(int, input().split()))

H=list(map(int, input().split()))
W=list(map(int, input().split()))

H_s=sorted(H)

sum=H_s[-1]-H_s[0]


ans=float("inf")
for w in W:
    idx=bisect.bisect_left(H_s,w)
    if idx%2==0:
        tmp=sum-(H_s[idx+2]-H_s[idx])+H_s[idx+1]-w
    else:
        tmp=sum-(H_s[idx+1]-H_s[idx-1])+w-H_s[idx]
    ans=min(ans,tmp)

print(ans)
