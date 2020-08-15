N, D = map(int, input().split())

cnt = 0
D = D**2

for i in range(N):
    X, Y = map(int, input().split())
    XY = X**2 + Y**2
    if D >= XY:
        cnt += 1

print(cnt)




