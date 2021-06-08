from sys import exit, stdin
import copy
#from collections import deque, Counter
import numpy as np
#from math import gcd, comb
import math
# input = stdin.readline
# mod = 1000000007

N = int(input())
x0,y0 = list(map(int, input().split()))
xn,yn = list(map(int, input().split()))

z0 = complex(x0,y0)
zn = complex(xn,yn)
zc= (z0 + zn)*0.5

z1 = (z0 - zc)* complex(math.cos(math.pi/N*2),math.sin(math.pi/N*2))+zc
print(z1.real,z1.imag)
