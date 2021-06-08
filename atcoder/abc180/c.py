from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

input = stdin.readline
mod = 1000000007

N, =list(map(int, input().split()))


lim= N**0.5

a=[]
b=[]
i=1
while i < lim:
    if N%i==0:
        a.append(i)
        b.append(int(N/i))
    i+=1
    
if N==int(lim)**2:
    a.append(int(lim))

for i in a:
    print(i)

for i in b[::-1]:
    print(i)
