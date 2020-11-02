N, M, Q = map(int, input().split())

l = []
cnt = 0

for i in range(Q):
    a = list(map(int, input().split()))
    l.append(a)

l = sorted(l, reverse=True, key=lambda x: x[3])

print(l)