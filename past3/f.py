import sys
import itertools
import copy

n = int(input())

s = [[c for c in input()] for _ in range(n)]

# print(s)

if n == 1:
    print("".join(s[0]))
    sys.exit()

elif n % 2 == 0:
    ans = []

    for i in range(0, int(n / 2)):

        p = 0
        for k in range(n):
            if s[i][k] in s[n - 1 - i]:
                t_p = copy.copy(s[i][k])
                ans.append(t_p)
                p = 1
                break
        if p == 0:
            print(-1)
            sys.exit()
    temp = "".join(ans) + "".join(ans[::-1])
    print(temp)

else:
    ans = []

    for i in range(0, int(n / 2)):
        p = 0
        for k in range(n):
            if s[i][k] in s[n - 1 - i]:
                t_p = copy.copy(s[i][k])
                ans.append(t_p)
                p = 1
                break
        if p == 0:
            print(-1)
            sys.exit()

    temp = "".join(ans) + s[int(n/2)][0] + "".join(ans[::-1])
    print(temp)
