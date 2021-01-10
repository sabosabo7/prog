from sys import exit, stdin
import copy
#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb

input = stdin.readline
mod = 1000000007

N, =list(map(int, input().split()))


if N%2==1:
    print("Black")
else:
    print("White")