import sys

def solve(s,i,N):
    l = 0
    r = len(s)-1
    x = [s[l],s[r],i]
    print(*x)
    sys.stdout.flush()
    m = int(input())
    if m==s[l]:
        s.insert(0,i)
    elif m==s[r]:
        s.append(i)
    else:
        while True:
            if r-l ==1:
                s.insert(r,i)
                break 
            c = int((l+r)/2)
            x = [s[l],s[c],i]
            print(*x)
            sys.stdout.flush()
            m = int(input())   
            if m == s[c]:
                l=c
            elif m == i:
                r=c
    if i==N: 
        print(*s)
        sys.stdout.flush()
        ans = input()
        return
    solve (s,i+1,N)

T,N,Q = list(map(int, input().split()))

for t in range(T):
    s=[1,2]
    solve(s,3,N)
