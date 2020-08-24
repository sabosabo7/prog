N, M = map(int, input().split())


S = []
C = []


for i in range(0, M):
    a, b = input().split()
    S.append(a)
    C.append(int(b))

# print(S)

# print(C)

d = [10 ** 13 for i in range(0, 2 ** N)]

d[0] = 0


def yn2num(s):
    k = 0
    idx = 0
    for t in s:
        if t == "Y":
            idx = idx + 2 ** k
        k = k + 1
    return idx


for i in range(0, M):
    s_idx = yn2num(S[i])

    for k in range(0, 2 ** N):
        tp_idx = k | s_idx
        if d[k] + C[i] < d[tp_idx]:
            d[tp_idx] = d[k] + C[i]


if d[2 ** N - 1] == 10 ** 13:
    print(-1)

else:
    print(d[2 ** N - 1])
