N, X = map(int, input().split())
L = []

alchol = 0
ans = 0

for i in range(N):
    VP = list(map(int, input().split()))
    L.append(VP)

for i in range(N):
    ans += 1
    alchol += L[i][0] * L[i][1]
    if X*100 < alchol:
        print(ans)
        exit()

print(-1)