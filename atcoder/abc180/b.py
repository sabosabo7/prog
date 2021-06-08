from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

input = stdin.readline
mod = 1000000007


N,=list(map(int, input().split()))
X=list(map(int, input().split()))

a,b,c=0,0,0
for x in X:
    a+=abs(x)
    b+=abs(x)**2
    c= max(c,abs(x))
print(a)
print(b**0.5)
print(c)
