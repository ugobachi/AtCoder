from collections import Counter

S = list(input())

if len(S) >= 3:
    cnt = Counter(S)
    for i in range(112, 1000, 8):
        if not Counter(str(i)) - cnt:
            print('Yes')
            exit()

elif len(S) == 2:
    if (int(S[0])*10 + int(S[1])) % 8 == 0 or ((int(S[1])*10 + int(S[0])) % 8) == 0:
        print('Yes')
        exit()
else:
    if int(S[0]) == 8:
        print('Yes')
        exit()


print('No')