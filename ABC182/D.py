import numpy as np

N = int(input())
A = list(map(int, input().split()))

maxi = 0
current = 0
q = -1 * float('inf')
_A = np.cumsum(A)
_A = _A.tolist()

for i in range(N):
    p = _A[i]
    q = max(q, _A[i])
    maxi = max(maxi, current+q)
    current += p

print(maxi)