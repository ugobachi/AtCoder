N, S, D = map(int, input().split())
L = []
for i in range(N):
    XY = list(map(int, input().split()))
    L.append(XY)

for i in range(N):
    if (L[i][0] < S) and (L[i][1] > D):
        print('Yes')
        exit()

print('No')