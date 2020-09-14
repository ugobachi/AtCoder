N = int(input())
cnt = 1
 
datalist =[ list(map(str, input().split())) for i in range(N) ]
 
for i in range(0,N):
    datalist[i].append(cnt)
    cnt += 1
 
datalist2 = sorted(datalist, key=lambda x:(x[0], -int(x[1])))
 
for i in range(0,N):
    print(datalist2[i][2])