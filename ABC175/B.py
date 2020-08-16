N = int(input())
cnt = 0

L = input().split()
L = [int(s) for s in L]

L.sort(reverse=True)

for i in range(len(L)-2):
    for j in range(i, len(L)-1):
        for k in range(j, len(L)):
            if L[i] < L[j] + L[k] and (L[i] != L[j] and L[i] != L[k] and L[j] != L[k]):
                cnt += 1

print(cnt)