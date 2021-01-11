N, C = map(int, input().split())
L = []
res, calc, days  = 0, 0, 0

for i in range(N):
    a, b, c = map(int, input().split())
    L.append((a-1, c))
    L.append((b, -c))

L.sort()

for i, j in L:
    if i != days:
        res += min(calc, C) * (i - days)
        days = i
    calc += j

print(res)