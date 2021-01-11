N = int(input())
A = list(map(int, input().split()))

A_head = A[0:(2**N)//2]
A_tail = A[(2**N)//2:2**N]

res = min(max(A_head), max(A_tail))

print(A.index(res)+1)