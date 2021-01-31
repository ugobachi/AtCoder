import itertools

'''
itertools.product() : リストの各要素の組み合わせの列挙, デカルト積
'''

N, M = map(int, input().split())

L1 = [tuple(map(int, input().split())) for i in range(M)]
K = int(input())
L2 = [tuple(map(int, input().split())) for i in range(K)]

ans = 0

for balls in itertools.product(*L2):
    balls = set(balls)
    cnt = sum(A in balls and B in balls for A, B in L1)
    if ans < cnt:
        ans = cnt

print(ans)