from sys import exit, stdin
import copy
#from collections import deque, Counter
import numpy as np
#from math import gcd, comb

input = stdin.readline

T = int(input())


for k in range(T):
    S = int(input())
    L = list(map(int, input().split()))
    n=0
    for i in range(len(L)-1):
        # print(L)
        j=np.argmin(L[i:])+i
        n+=j-i+1
        L[i:j+1]=reversed(L[i:j+1])
    print("Case #{}: {}".format(k+1,n))        
