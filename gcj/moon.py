from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

input = stdin.readline

T = int(input())
for k in range(T):
    X,Y,S = input().split()
    X=int(X)
    Y=int(Y)
    c=0
    buf =""    
    for s in S:
        if buf=="" and s!="?":
            buf=s
        elif buf!="" and s!="?":
            if s!=buf:
                if buf=="C":
                    c+=X
                elif buf=="J":
                    c+=Y
                buf = s
    print("Case #{}: {}".format(k+1,c))
