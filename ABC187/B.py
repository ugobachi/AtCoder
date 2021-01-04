N = int(input())
L = []
cnt = 0

for i in range(N):
    xy = list(map(int, input().split()))
    L.append(xy)


for i in range(N):
    for j in range(i+1,N):
        x = L[j][0] - L[i][0]
        y = L[j][1] - L[i][1]
        a = y / x
        if (a >= -1) and (a <= 1):
            cnt += 1 

print(cnt)