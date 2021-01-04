import numpy as np

N = int(input())
A = list(map(int, input().split()))

calc = 0
A.sort()

B = np.cumsum(A)
B = B.tolist()
B.insert(0, 0)

for i in range(N):
    calc += A[i]*i - B[i]

print(calc)