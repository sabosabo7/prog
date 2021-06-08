from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

input = stdin.readline
mod = 1000000007

N, = list(map(int, input().split()))
D=[list(map(int, input().split())) for _ in range(N)]

def cost(s,g):
    return abs(g[0]-s[0])+abs(g[1]-s[1])+max([0,g[2]-s[2]])

dp=[[float("inf")]]