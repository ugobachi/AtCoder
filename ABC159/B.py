S = list(input())

reS = list(reversed(S))

cnt = 0
cntA = 0
cntB = 0

for (i, j) in zip(S, reS):
    if i == j:
        cnt += 1
    else:
        print('No')
        break
    
if cnt == len(S):
    N = len(S)
    listA = []
    listB = []

    for i in range(0, (N-1)//2):
        listA.append(S[i])
    for j in range((N+3)//2 - 1, N):
        listB.append(S[j])

    reA = list(reversed(listA))
    reB = list(reversed(listB))

    for (i, j) in zip(listA, reA):
        if i == j:
            cntA += 1
        else:
            pass

    for (i, j) in zip(listB, reB):
        if i == j:
            cntB += 1
        else:
            pass

    if cntA == len(listA) and cntB == len(listB):
        print('Yes')
    else:
        print('No')