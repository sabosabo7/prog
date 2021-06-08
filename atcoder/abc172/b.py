from sys import exit
#import copy
#import numpy as np
#from collections import deque


s = input()
t = input()

cnt = 0
for i in range(len(s)):
    if s[i] != t[i]:
        cnt += 1

print(cnt)
