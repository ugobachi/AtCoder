H = int(input())
cnt, res = 0, 0

while H > 1:
    H = H //2
    cnt += 1
    res += 2**cnt

print(res+1)