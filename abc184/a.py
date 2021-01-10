from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

input = stdin.readline
mod = 1000000007

a,b=list(map(int, input().split()))
c,d=list(map(int, input().split()))

print(int(a*d-b*c))