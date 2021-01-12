from sys import exit, stdin
import copy
from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

# input = stdin.readline
mod = 1000000007

S=input()

C=Counter(list(S))

if len(S)==1:
    if int(S)==8:
        print("Yes")
        exit()
elif len(S)==2:
    for i in range(16,100,8):
        tmp=str(i)
        t= Counter(tmp)
        for j in t.items():
            if C[j[0]]<j[1]:
                break
        else:
            print("Yes")
            exit()

else :
    for i in range(0,1000,8):
        tmp=str(i).zfill(3)
        t= Counter(tmp)
        for j in t.items():
            if C[j[0]]<j[1]:
                break
        else:
            print("Yes")
            exit()
    
print("No")
