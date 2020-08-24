from sys import exit
#import copy
#import numpy as np
#from collections import deque

n, = map(int, input().split())


while n > 1000:
    n -= 1000

print(1000-n)
