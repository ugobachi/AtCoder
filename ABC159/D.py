
N = int(input())
A = list(map(int, input().split()))


for i in range(N):
    cnt = 1
    calclist = []
    Blist = A
    Blist.remove(Blist[i])
    Blist.sort()
    for j in range(0, N-2):
        if Blist[j] == Blist[j+1]:
            cnt += 1
        else:
            calc = (cnt*(cnt-1)) // 2
            calclist.append(calc)
    result = sum(calclist)
    print(result)


    
    