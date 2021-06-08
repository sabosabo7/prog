from sys import exit
#import copy
#import numpy as np
#from collections import deque

n, = map(int, input().split())

tmp = n

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
         "m", "n", "o", "p", " q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

ans = []
gun = 0
for l in range(1, 13):
    if gun < tmp <= gun+26 ** l:
        kou = tmp - gun-1
        for k in range(l):
            ans.append(kou % 26)
            kou = kou // 26
        break
    else:
        gun += 26 ** l


s = ""
for i in ans[::-1]:
    s += alpha[i]

print(s)
