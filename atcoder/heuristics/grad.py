from sys import exit
import copy
import random
import time 
#import numpy as np
#from collections import deque

def calc_score(arr):
    ans=0
    l=[0 for _ in range(26)]
    for i in range(d):
        ans+=s[i][arr[i]-1]
        for k in range(26):
            ans-=c[k]*(i+1-l[k])
        l[arr[i]-1]=i+1
    return ans

def greed():
    sche=[0 for _ in range(d)]
    last=[0 for _ in range(26)]
    ans=0
    for day in range(1,d+1):
        idx=day-1
        delta=float("inf")*(-1)
        for t in range(26):    
            del_tmp=0
            l_tmp=copy.copy(last)
            del_tmp+=s[idx][t]
            l_tmp[t]=day
            for l in range(26):
                del_tmp-=c[l]*(day-l_tmp[l])
            if del_tmp>=delta:
                delta=del_tmp
                i_tmp=t
        sche[idx]=i_tmp+1
        ans+=delta
        last[i_tmp]=day
    return ans,sche



d, = map(int, input().split())
c= list(map(int, input().split()))
s=[list(map(int, input().split())) for _ in range(d)]

t0=time.time()
TL=10
score,sche=greed()
print(score)

while True:#time.time()-t0<TL:
    sche_tmp=copy.copy(sche)
    sche_tmp[random.randrange(d)]=random.randrange(1,27)
    s_tmp=calc_score(sche_tmp)
    if s_tmp>=score:
        score=s_tmp
        sche=copy.copy(sche_tmp)
        print(s_tmp)


# for i in sche:
#     print(i)
# print(score)




