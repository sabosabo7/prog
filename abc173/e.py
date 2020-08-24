from sys import exit
# import copy
# import numpy as np
# from collections import deque
import random


def mymod(n):
    if abs(n) > 1**9+7:
        if n > 0:
            return n % (1**9+7)
        else:
            return n % (1**9+7) - (1**9+7)
    else:
        return n


N, K = map(int, input().split())
# A = list(map(int, input().split()))

A = [random.randrange(1, 100)*1e4*(-1)**random.randrange(0, 2) for _ in range(N)]

A = sorted(A, key=abs)

print(A)

A.extend([float("inf"), 0])

ans = 1
if N == K:
    for n in A[:-2]:
        ans *= n
        ans = mymod(ans)
    ans %= 1**9+7
    print(int(ans))
    exit()
elif K % 2 == 1 and max(A[:-2]) < 0:
    for i in range(K):
        ans *= A[i]
        ans = mymod(ans)
    ans %= 1**9+7
    print(int(ans))
    exit()
else:
    min_minu = -2
    min_plus = -2
    for i in range(N-K, N):
        ans *= A[i]
        ans = mymod(ans)
        if min_minu == -2 and A[i] < 0:
            min_minu = i
        if min_plus == -2 and A[i] > 0:
            min_plus = i

    if ans >= 0:
        print(int(ans))
        exit()
    else:
        max_minu = -1
        max_plus = -1
        for i in range(N-K-1, -1, -1):
            if max_minu == -1 and A[i] < 0:
                max_minu = i
            if max_plus == -1 and A[i] > 0:
                max_plus = i
            if max_minu != -1 and max_plus != -1:
                break

        if abs(A[max_minu] / A[min_plus]) >= abs(A[max_plus] / A[min_minu]):
            ans = 1
            A[min_plus] = A[max_minu]
            for i in range(N-K, N):
                ans *= A[i]
                ans = mymod(ans)
            ans %= 1**9+7
            print(int(ans))
            exit()
        else:
            ans = 1
            A[min_minu] = A[max_plus]
            for i in range(N-K, N):
                ans *= A[i]
                ans = mymod(ans)
            ans %= 1**9+7
            print(int(ans))
            exit()
