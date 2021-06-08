from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb
from math import factorial as fact

input = stdin.readline
mod = 1000000007

D=list(map(int, input().split()))
D.sort()


ans=0

if D[0]==0:
    if D[1]==0:
        ans= 100-D[2]
    else:
        for a in range(D[1],100):
           ans+=(a+100-D[1]-D[2])* fact(a)/fact(D[1])*fact(100)/fact(D[2])/(fact(a+100)/fact(D[1]+D[2]))
        for b in range(D[2],100):
           ans+=(b+100-D[1]-D[2])* fact(100)/fact(D[1])*fact(b)/fact(D[2])/(fact(b+100)/fact(D[1]+D[2]))
elif D[0]!=0 and D[1]!=0 and D[2]!=0:
    for a in range(D[0],100):
        for b in range(D[1],100):
           ans+=(a+b+100-D[0]-D[1]-D[2])* fact(a)/fact(D[0])*fact(b)/fact(D[1])*fact(100)/fact(D[2])/(fact(a+b+100)/fact(D[0]+D[1]+D[2]))
    
    for a in range(D[0],100):
        for c in range(D[2],100):
           ans+=(a+100+c-D[0]-D[1]-D[2])* fact(a)/fact(D[0])*fact(100)/fact(D[1])*fact(c)/fact(D[2])/(fact(a+c+100)/fact(D[0]+D[1]+D[2]))
    for b in range(D[1],100):
        for c in range(D[2],100):
           ans+=(c+b+100-D[0]-D[1]-D[2])* fact(100)/fact(D[0])*fact(b)/fact(D[1])*fact(c)/fact(D[2])/(fact(c+b+100)/fact(D[0]+D[1]+D[2]))

print(ans)