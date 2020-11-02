N = int(input())
cnt = 0
for i in range(N):
    A, B = map(int, input().split())
    S = (B-A+1)*(A+B)//2
    cnt += S

print(cnt)