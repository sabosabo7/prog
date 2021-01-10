from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

mod = 1000000007


N=input()
N=list(map(int,list(N)))

S=[0]*(len(N)+1)
S[0]=0
for i in range(1,len(N)+1):
    S[i]=(S[i-1]+N[i-1])%3
if S[len(N)]==0:
    print(0)
    exit()
ans=-1
for i in range(1,len(N)):
    for k in range(0,len(N)-i+1):
        tmp=(S[len(N)]-(S[k+i]-S[k]))%3
        if tmp==0:
            ans=i
            print(ans)
            exit()

print(ans)
