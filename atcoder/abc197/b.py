from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

# input = stdin.readline
mod = 1000000007

H,W,X,Y = list(map(int, input().split()))

X-=1
Y-=1

S = [input() for _ in range(H)]



cnt =0

u,d,l,r =X,X,Y,Y

for li in range(Y,-1,-1):
    if S[X][li]=="#":
        break
    l=li

for ri in range(Y,W,1):
    if S[X][ri]=="#":
        break
    r=ri

for ui in range(X,-1,-1):
    if S[ui][Y]=="#":
        break
    u=ui

for di in range(X,H,1):
    if S[di][Y]=="#":
        break
    d=di

ans = (r-l)+(d-u)+1

print(int(ans))