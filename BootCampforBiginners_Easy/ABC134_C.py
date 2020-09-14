N = int(input())
li = []
 
for i in range(N):
    A = int(input())
    li.append(A)
 
li2 = sorted(li,reverse=True)
ans = max(li)
 
for i in range(N):
    if(ans == li[i]):
        print(li2[1])
    else:
        print(ans)