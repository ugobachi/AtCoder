num = list(str(input()))
cnt = 0

for i in range(len(num)):
    if i+3 > len(num):
        break
    else:
        for j in range(i+4, (len(num)) + 1):
            check = ''.join(num[i:j])
            if len(num)-j >= 4:
                check2 = ''.join(num[i:len(num)-j+4])
            else:
                check2 = 1
            # print(check, check2)
            if (int(check) % 2019 == 0) or (int(check2) % 2019 == 0):
                cnt += 1
                break
            

print(cnt)