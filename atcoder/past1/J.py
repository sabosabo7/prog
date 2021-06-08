import copy

h, w = map(int, input().split())


A = [list(map(int, input().split())) for i in range(h)]

# print(A)


def mkidx(n):
    if n == 0:
        return [[0, 0]]
    temp = [[-n, -n + i] for i in range(0, 2 * n)] \
        + [[-n + i,  n] for i in range(0, 2 * n)] \
        + [[n, n - i] for i in range(0, 2 * n)]\
        + [[n - i, -n] for i in range(0, 2 * n)]\

    return mkidx(n-1)+temp


def around(x, y, a, h, w):
    if x == 0:
        l = 10 ** 6
        r = a[y][x+1]
    elif x == w - 1:
        l = a[y][x - 1]
        r = 10 ** 6
    else:
        l = a[y][x - 1]
        r = a[y][x+1]

    if y == 0:
        u = 10 ** 6
        d = a[y+1][x]
    elif y == h - 1:
        u = a[y-1][x]
        d = 10 ** 6
    else:
        u = a[y-1][x]
        d = a[y+1][x]

    return l, r, u, d


ans = 10**6
for i in range(0, h):
    for j in range(0, w):
        D = [[10**6 for _ in range(w)] for _ in range(h)]
        D[i][j] = 0
        D_t = [[0 for _ in range(w)] for _ in range(h)]
        while D_t != D:
            D_t = copy.deepcopy(D)
            for p, q in mkidx(int(max(h, w))):
                y = p + i
                x = q + j
                if (0 <= x < w) and (0 <= y < h):
                    l, r, u, d = around(x, y, D, h, w)
                    if y == i and x == j:
                        continue
                    elif l == 10**6 and r == 10**6 and u == 10**6 and d == 10**6:
                        continue

                    D[y][x] = min([l, r, u, d]) + A[y][x]
        temp = D[0][w-1]+D[h-1][0]+D[h-1][w-1]+A[i][j]
        # print("##############")
        # print("i,j=", i, j)
        # print("ans=", temp)
        # for s in D:
        # print(s)

        ans = min(ans, temp)


# print("final_min=", ans)
print(ans)
