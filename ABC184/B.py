N, X = map(int, input().split())
S = list(input())
cnt = X

for i in S:
    if i == 'o':
        cnt += 1
    elif cnt > 0 and (i == 'x'):
        cnt -= 1

print(cnt)