N, K = map(int, input().split())
p = list(input().split())

p = [int(n) for n in p]

p.sort()

res = 0

for i in range(K):
    res += p[i]

print(res)