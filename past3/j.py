# import copy
import bisect


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


def search(n, arr):
    max_idx = 0
    min_idx = len(arr)-1
    while min_idx-max_idx != 1:
        p_idx = int((max_idx+min_idx) / 2)
        if n > arr[p_idx]:
            min_idx = p_idx
        else:
            max_idx = p_idx
    return [max_idx, min_idx]


n, m = xnxn()
a = xnxn(flag="l")
score = [0]

for s in a:
    if s > score[0]:
        score[0] = s
        print(1)
    elif score[-1] >= s:
        if len(score) > n-1:
            print(-1)
            continue
        else:
            score.append(s)
            print(len(score))
    else:
        idx = search(s, score)
        score[idx[1]] = s
        print(idx[1]+1)
