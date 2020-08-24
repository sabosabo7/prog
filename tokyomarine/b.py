import numpy as np
import sys
# import copy


def xnxn(n=0, flag="v"):
    """
    args:
        int n: a number of lows to read
    example:
        input   1
        retrun  1

        input   1 2 3
        return  [1,2,3]
        input   1 2 3
                4
        return  [[1,2,3],
                [4]]
    """
    if n == 0:
        temp = list(map(int, input().split()))
        if len(temp) == 1:
            if flag == "l":
                return temp
            else:
                return temp[0]
        elif len(temp) > 1:
            return temp
    else:
        temp = [list(map(int, input().split())) for _ in range(n)]
        return temp


a, v = xnxn()
b, w = xnxn()
t = xnxn()


# for i in range(t):
#     if b - a > 0:
#         b = min(b + w, 10 ** 9)
#         a = min(a + v, 10 ** 9)
#         if b == a:
#             print("YES")
#             sys.exit()
#     elif b - a < 0:
#         b = max(b - w, 10 ** 9)
#         a = max(a - v, 10 ** 9)
#         if b == a:
#             print("YES")
#             sys.exit()

# print("NO")

if b - a > 0:
    b_f = b+t*w
    a_f = a+t*v
    if b_f > a_f:
        print("NO")
    else:
        print("YES")


else:
    b_f = b-t*w
    a_f = a-t*v

    if b_f < a_f:
        print("NO")
    else:
        print("YES")
