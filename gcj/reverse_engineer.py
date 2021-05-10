from sys import exit, stdin
import copy
#from collections import deque, Counter
import numpy as np
#from math import gcd, comb
import itertools
input = stdin.readline

def f(N,C):
        S=[]
        c = C-(N-1)
        for i in range(1,N):
            s=min(i,c)
            S.append(s+1)
            c-=s
        # print(S)
        return S 

def mk_l(N,S):
    l=list(range(1,N+1))
    for k in range(N-1):
        i = N-2-k
        j = i+S[k]-1
        l[i:j+1]=reversed(l[i:j+1])
    return l 

def cnt(arr):
    buf = list(arr)
    n=0
    for i in range(len(buf)-1):
        j=np.argmin(buf[i:])+i
        n+=j-i+1
        buf[i:j+1]=reversed(buf[i:j+1])
    return n

T = int(input())
for k in range(T):
    N,C= list(map(int, input().split()))
    if C<N-1 or C>(N+2)*(N-1)/2:
        print("Case #{}: IMPOSSIBLE".format(k+1))
    else:
        l= mk_l(N,f(N,C))
        print("Case #{}: ".format(k+1),end="")
        print(*l)
        # print("c=",cnt(l))  
