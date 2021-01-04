import itertools

H, W = map(int, input().split())

L = []

for i in range(H):
    block = list(map(int, input().split()))
    L.append(block)

L = list(itertools.chain.from_iterable(L))
L.sort()
calc = 0

for i in range(1, len(L)):
    calc += L[i] - L[0]

print(calc)