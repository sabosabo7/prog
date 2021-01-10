from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

input = stdin.readline
mod = 1000000007

N,X =list(map(int, input().split()))
S, = input().split()

for a in S:
    if a=="o":
        X+=1
    else:
        X=max(0,X-1)


print(X)
