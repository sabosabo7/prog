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


def sp_xnxn(n=0):
    """
    args:
        int n: a number of lows to read
    example
        input   1
        retrun  [1]

        input   123
        return  [1,2,3]

        input   123
                4 
        return  [[1,2,3],
                [4]]
    """
    if n == 0:
        return [int(k) for k in xsxs()]
    else:
        return [[int(k) for k in xsxs()] for _ in range(n)]


def xsxs(n=0):
    """
    args:
        int n: a number of lows to read 
    example:
        input   AA
        retrun  AA

        input   A BBB CC
        return  ["A","BBB","CC"]

        input   A BB CCC
                D
        return  [["A","BBB","CC"],
                ["D"]]
    """
    if n == 0:
        temp = list(input().split())
        if len(temp) == 1:
            return temp[0]
        elif len(temp) > 1:
            return temp
    else:
        return [list(input().split()) for _ in range(n)]


def sp_xsxs(n=0):
    """
    args:
        int n: a number of lows to read 
        example:
            input   A
            retrun  ["A"]

            input   ABC
            return  ["A","B","C"]

            input   ABC
                    D
            return  [["A","B","C"],
                    ["D"]]
    """
    if n == 0:
        return [s for s in xsxs()]
    else:
        return [[s for s in xsxs()] for _ in range(n)]


n = xnxn()

if n % 10 == 3:
    print("bon")
elif n % 10 == 0 or n % 10 == 1 or n % 10 == 6 or n % 10 == 8:
    print("pon")
else:
    print("hon")
