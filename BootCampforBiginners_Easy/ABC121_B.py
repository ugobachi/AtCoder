N, M, C = map(int, input().split()) 
B = list(map(int, input().split()))
 
sumlist = []
cnt = 0
 
for i in range(N):
    A = list(map(int, input().split()))
    for j in range(M):
        sumlist.append(A[j]*B[j])
    if sum(sumlist) + C > 0:
        cnt += 1
        sumlist = []
    else:
        sumlist = []
 
print(cnt)