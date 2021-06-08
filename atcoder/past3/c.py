import numpy as np

a, r, n = map(int, input().split())

r = float(r)
temp = a * np.power(r, n - 1)

if temp > np.power(10, 9):
    print("large")
else:
    print(int(temp))
