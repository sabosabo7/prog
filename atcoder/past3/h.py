import numpy as np
import sys


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


n, l = xnxn()
x = xnxn(flag="l")
t = xnxn()

time = 0

hurdle = [0 for _ in range(l+1)]
for i in x:
    hurdle[i] = 1

dp = [float("inf") for _ in range(l+1)]
dp[0] = 0

for i in range(1, l+1):
    if i > 0:
        dp[i] = min(dp[i-1]+t[0] + t[2]*hurdle[i-1], dp[i])
    if i > 1:
        dp[i] = min(dp[i - 2] + t[0] + t[1] +
                    t[2] * (hurdle[i - 2]), dp[i])
    if i > 3:
        dp[i] = min(dp[i - 4] + t[0] + t[1]*3 +
                    t[2] * (hurdle[i - 4]), dp[i])


for i in range(1, 4):
    dp[l] = min(dp[l - i] + 0.5 * t[0] + (0.5 + i - 1)
                * t[1] + t[2] * (hurdle[l - i]), dp[l])

print(int(dp[l]))
