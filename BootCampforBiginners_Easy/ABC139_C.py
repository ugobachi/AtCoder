N = int(input())
H = list(map(int, input().split()))
H.append(1000000000000000000000000000000)
dansa = 0
cnt = 0
 
for i in range(len(H)-1):
    if H[i] >= H[i+1]:
        cnt += 1
    else:
        if cnt > dansa:
            dansa = cnt
        cnt = 0
 
print(dansa)