from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial

N,X =map(int, input().split())

A = list(map(int, input().split()))

total = sum(A)-len(A)//2

if total <= X:
	print("Yes")
else:
	print("No")