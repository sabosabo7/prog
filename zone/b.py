from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

input = stdin.readline
mod = 1000000007

N,D,H = list(map(int, input().split()))

ans=0
for i in range(N):
    d,h= list(map(int, input().split()))
    a = (H-h)/(D-d)
    b= H-a*D
    ans = max(ans,b)

print(ans)