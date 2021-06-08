from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

input = stdin.readline
mod = 1000000007

N,=list(map(int, input().split()))
A=list(map(int, input().split()))

tmp=0
ans=2
for i in range(2,1001):
    cnt=0
    for a in A:
        if a%i ==0:
            cnt+=1
    if cnt>tmp:
        tmp=cnt
        ans=i

print(ans)