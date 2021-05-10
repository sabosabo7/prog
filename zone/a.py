from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

input = stdin.readline
mod = 1000000007


S = input()


ans=0
for i in range(len(S)):
    if S[i]=="Z":
        if S[i:i+4]=="ZONe":
            ans+=1

print(ans)