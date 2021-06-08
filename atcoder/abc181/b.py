from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

input = stdin.readline
mod = 1000000007


N, =list(map(int, input().split()))
A=[list(map(int, input().split())) for _ in range(N)]

tmp=0

for i in A:
    tmp+=0.5*(i[0]+i[1])*(i[1]-i[0]+1)

print(int(tmp))