from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

input = stdin.readline
mod = 1000000007


r1,c1=list(map(int, input().split()))
r2,c2=list(map(int, input().split()))

x=r2-r1
y=c2-c1

if x==0 and y==0:
    ans=0
elif x+y==0 or x-y==0 or abs(x)+abs(y)<=3:
    ans=1
elif (x+y)%2==1:
    if x<=-6 and y<=-x-5 and y>=x+5:
        ans=3
    elif x>=6 and y<=x-5 and y>=-x+5:
        ans=3
    elif y<=-6 and y<=-x-5 and y<=x-5:
        ans=3
    elif y>=6 and y>=x+5 and y>=-x+5:
        ans=3
    else:
        ans=2
else:
    ans=2

print(ans)