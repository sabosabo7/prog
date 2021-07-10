from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial
import math

A,B,C,D= map(int, input().split())

if C*D-B>0:
	ans = math.ceil(A/(C*D-B))
else:
	ans=-1

print(ans)