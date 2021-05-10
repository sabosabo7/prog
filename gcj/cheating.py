from operator import inv
from sys import exit, stdin
import copy
#from collections import deque, Counter
import numpy as np
#from math import gcd, comb
# import matplotlib.pyplot as plt 
input = stdin.readline
# mod = 1000000007

def sigmoid(x):
    return 1/(1+np.exp(-x))

def inv_sig(x):
    return -1*np.log((1-x)/x)

def px(x):
    return (x<0)*(1/36*x+1/6)+(x>=0)*(-1/36*x+1/6)

x=np.linspace(-6,6,1201)
plt.plot(x,px(x))
plt.show()

plt.plot(sigmoid(x),px(x))
plt.show()

plt.plot(sigmoid(x),px(x))
plt.plot(sigmoid(x)*0.5+0.5,px(x)*2)
plt.show()

x1=np.linspace(0.5,1,1000)
y_norm = px(inv_sig(x1))
y_cheat = px(inv_sig((x1-0.5)*2))*2
rate = y_cheat/(y_norm+y_cheat)
plt.ylim([0,1])
plt.plot(x1,rate)




T = int(input())
for t in range(T):
    P = int(input())
    rate=np.zeros(100) 
    for i in range(100):
        buf=list(map(int,list(input())[:-1]))
        rate[i]=sum(buf)/10000
    ans = np.argmin(np.abs(rate-2/3))+1    
    print("Case #{}: {}".format(t+1,ans))
