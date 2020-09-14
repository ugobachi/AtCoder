K, N = map(int, input().split())
A = list(map(int, input().split()))
 
A.insert(0, 0)
A.append(K)
 
start = A[1] - A[0]
goal = A[-1] - A[-2]
 
mixi = 0
sum_len = 0
 
SorG = start + goal
 
for i in range(len(A) - 1):
    if A[i+1] - A[i] > mixi:
        mixi = A[i+1] - A[i]
    sum_len += A[i+1] - A[i]
 
if max(SorG, mixi) == SorG or SorG == mixi:
    result = sum_len - (start + goal)
elif max(SorG, mixi) == mixi:
    result = sum_len - mixi
 
print(result)