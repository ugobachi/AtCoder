N = int(input())
A = list(map(int, input().split()))

GCDmax = 0
res = 0

for i in range(2,max(A)+1):
    GCD = 0
    for j in range(N):
        if A[j]%i == 0:
            GCD += 1
    if GCDmax < GCD:
        res = i
        GCDmax = GCD

print(res)


