N = int(input())
H = list(map(int, input().split()))
fl = True
 
for i in range(0, len(H)-1):
    if H[i] > H[i+1] + 1:
        fl = False
        break
 
    if H[i-1] == H[i]:
        if H[i] > H[i+1]:
            fl = False
            break
 
    if H[i-1] < H[i]:
        if H[i] == H[i+1] + 1 or H[i] == H[i+1]:
            H[i] = H[i] - 1
 
if fl == True:
    print('Yes')
elif fl == False:
    print('No')