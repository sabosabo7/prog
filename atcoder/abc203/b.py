from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial


N,K =map(int, input().split())

ans=(N+1)*N//2*K*100+(1+K)*K//2*N
print(ans)