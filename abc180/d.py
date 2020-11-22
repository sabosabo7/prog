from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

input = stdin.readline
mod = 1000000007


X,Y,A,B = list(map(int, input().split()))
exp=0

k=B/(A-1)

while X<k:
    X*=A
    if X>=Y:
        print(0)
        exit()
    exp+=1


if (Y-X)%B ==0:
    exp+= (Y-X)//B-1
else:
    exp+= (Y-X)//B

print(exp)
