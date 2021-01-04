N = int(input())
L = []
aoki = 0
takahashi = 0
cnt = 0

for i in range(N):
    AB = list(map(int, input().split()))
    aoki += AB[0]
    L.append(AB)

li = sorted(L, reverse=True, key=lambda x: (x[0]+x[0]+x[1]))

for i in range(N):
    cnt += 1
    aoki -= li[i][0]
    takahashi += sum(li[i])
    if takahashi > aoki:
        print(cnt)
        exit()