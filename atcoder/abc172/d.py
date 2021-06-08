from sys import exit
#import copy
import numpy as np
#from collections import deque


def p_num(n):
    tmp = n
    ans = []
    for i in range(2, int(np.sqrt(n)) + 1):
        cnt = 0
        while tmp % i == 0:
            cnt += 1
            tmp = int(tmp / i)
        if cnt > 0:
            ans.append([i, cnt])
    if tmp != 1:
        ans.append([tmp, 1])
    if ans == []:
        ans.append([n, 1])
    a = 1
    for k in ans:
        a *= (k[1]+1)
    return a


n, = map(int, input().split())

ans = 1
for i in range(2, n + 1):
    ans += p_num(i) * i

print(ans)
