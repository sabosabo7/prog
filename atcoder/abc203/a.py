from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial

a,b,c=map(int, input().split())

if a==b:
	print(c)
elif a==c:
	print(b)
elif b==c:
	print(a)
else:
	print(0)
