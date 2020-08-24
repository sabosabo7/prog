from sys import exit
import copy
#import numpy as np
#from collections import deque


d, = map(int, input().split())
c= list(map(int, input().split()))
s=[list(map(int, input().split())) for _ in range(d)]
#  t=[int(input()) for _ in range(d)]

sche=[0 for _ in range(d)]
s_tmp=float("inf")*(-1)
for off in range(0,13):
    last=[0 for _ in range(26)]
    sche=[0 for _ in range(d)]
    for day in range(1,d+1):
        idx=day-1
        d_tmp=float("inf")*(-1)
        i_tmp=0
        for t in range(26):    
            delta=0
            l_tmp=copy.copy(last)
            delta+=s[idx][t]
            l_tmp[t]=day
            for l in range(26):
                delta-=0.5*(off+1)*c[l]*((day-l_tmp[l])+(day+off-l_tmp[l]))
            if delta>=d_tmp:
                d_tmp=delta
                i_tmp=t
        
        sche[idx]=i_tmp+1
        # score+=d_tmp
        last[i_tmp]=day
        # print(score)
        # print(i_tmp+1)

    score=0
    last=[0 for _ in range(26)]
    for i in range(1,d+1):
        idx=i-1
        score+=s[idx][sche[idx]-1]
        for l in range(26):
            score-=c[l]*(i-last[l])
        last[sche[idx]-1]=i
    
    # print(score)
    if score>=s_tmp:
        s_tmp=score
        sche_tmp=copy.copy(sche)


for i in sche_tmp:
    print(i)
# print(s_tmp)




