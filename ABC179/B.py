N = int(input())
L = []

for i in range(N):
    D = list(map(int, input().split()))
    L.append(D)

for i in range(len(L)-2):
    if (L[i][0] == L[i][1]) and (L[i+1][0] == L[i+1][1]) and (L[i+2][0] == L[i+2][1]):
        print('Yes')
        exit()

print('No')
