N = int(input())
 
A = list(map(int, input().split()))
B = list(map(int, input().split()))
 
cnt = 0
 
for i in range(len(A)-1):
    if A[i] >= B[i]:
        cnt += B[i]
    else:
        cnt += A[i]
        B[i] -= A[i] 
        if A[i+1] >= B[i]:
            cnt += B[i]
            A[i+1] -= B[i]
        else:
            cnt += A[i+1]
            A[i+1] = 0
 
print(cnt)