smpl = []
for _ in range(42):
    smpl.append(input())

print("read calc")
ans = []
for _ in range(41):
    ans.append(input())

print("diff")
for s in smpl:
    if not (s in ans):
        print(s)
