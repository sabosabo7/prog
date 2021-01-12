from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

input = stdin.readline
mod = 1000000007



N, =list(map(int, input().split()))
D=[list(map(int, input().split())) for _ in range(N)]

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if (D[j][1]-D[i][1])*(D[k][0]-D[i][0])==(D[k][1]-D[i][1])*(D[j][0]-D[i][0]):
                print("Yes")
                exit()

print("No")
