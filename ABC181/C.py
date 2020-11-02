import itertools
from scipy.spatial import distance


N = int(input())
L = []

for i in range(N):
    x = list(map(int, input().split()))
    L.append(x)

A = list(itertools.combinations(L,3))

for i in A:
    x1, y1 = i[0][0], i[0][1] 
    x2, y2 = i[1][0], i[1][1]
    x3, y3 = i[2][0], i[2][1]
    if (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1) == 0:
        print('Yes')
        exit()

print('No')