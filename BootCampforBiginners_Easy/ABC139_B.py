A, B = map(int, input().split())

cnt = 0
if B == 1:
    print('0')
 
if B > 1:
    B -= A
    cnt += 1
    while B > 0:
        cnt += 1
        B -= A-1
    print(cnt)