N = int(input())

cnt = 0

for i in range(1, N+1):
    if ('7' in list(str(i))) or ('7' in list(str(oct(i)))):
        cnt += 1

print(N - cnt)