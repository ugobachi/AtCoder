import itertools

N, K = map(int, input().split())

l = []
k = []
for i in range(1, N+1):
    l.append(str(i))

for i in range(K):
    d = int(input())
    array = input().strip().split()
    k.append(array)
                
k = list(itertools.chain.from_iterable(k))

k = [x for x in set(k) if k.count(x) >= 1]

for i in range(len(k)):
    for j in range(len(l)):
        if k[i] == l[j]:
            l[j] = 0

cnt = 0

for i in l:
    if i == 0:
        cnt += 1

print(len(l) - cnt)