from sys import exit, stdin
import copy
from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

input = stdin.readline
mod = 1000000007

S=input().split()[0]
T= deque()



r=False
for s in S:
    if s=="R":
        r = not r
    else:
        if len(T)==0:
            T.append(s)
            continue
        if r:
            if s==T[0]:
                T.popleft()
            else: 
                T.appendleft(s)
        else:
            if s==T[-1]:
                T.pop()
            else:
                T.append(s)

if r:
    T.reverse()
    print("".join(T))
else:
    print("".join(T))
