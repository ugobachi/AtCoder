N = int(input())
A = list(map(int, input().split()))

maxi = 0

for i in range(N):
    mini = A[i]
    for j in range(i,N):
        if mini >= A[j]:
            mini = A[j]
        calc = mini * (j-i+1)
        if calc > maxi:
            maxi = calc

print(maxi)