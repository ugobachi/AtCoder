N, M = map(int, input().split())
NL = []
summoney = []
min = 1000000000
 
for i in range(N):
    *A, B = map(int, input().split())
    A.append(B)
    NL.append(A)
 
NL = sorted(NL)
 
for j in range(N):
    if M - NL[j][1] >= 0:
        summoney.append(NL[j][0]*NL[j][1])
        M =  M - NL[j][1]
    elif  M - NL[j][1] < 0:
        summoney.append(M*NL[j][0])
        break
 
print(sum(summoney))