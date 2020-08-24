import numpy as np


# input N   -> return N
# input N N -> return [N, N]
# input N N -> return [[N, N],
#       N N            [N, N]]

def xnxn(n=0):
    if n == 0:
        temp = list(map(int, input().split()))
        if len(temp) == 1:
            return temp[0]
        elif len(temp) > 1:
            return temp
    else:
        temp = [xn() for _ in range(n)]
        return temp


# input str     -> return str
# input str str -> return [str, str]
# input str str -> return [[str, str],
#       str str            [str, str]]

def xsxs(n=0):
    if n == 0:
        temp = list(input().split())
        if len(temp) == 1:
            return temp[0]
        elif len(temp) > 1:
            return temp
    else:
        return [list(input().split()) for _ in range(n)]


a = xnxn()
b, c = xnxn()
s = xsxs()

print(a+b+c, s)
