n, m, q = map(int, input().split())

s = list(list(map(int, input().split())) for i in range(q))

# print(s)

point = [n for _ in range(m)]
score = [[0 for _ in range(m)] for _ in range(n)]

for i in range(q):
    idx = s[i][1]-1
    if s[i][0] == 1:
        sum_p = 0
        for k in range(m):
            sum_p = sum_p + score[idx][k]*point[k]
        print(sum_p)
    elif s[i][0] == 2:
        point[s[i][2]-1] = point[s[i][2]-1]-1
        score[idx][s[i][2]-1] = 1
