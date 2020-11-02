"""[solution]
A ~ BまででNで割り切れる数があればOK, なければNGを出力
"""

K = int(input())
A, B = map(int, input().split())

fl = False

for i in range(A, B+1):
    if i % K == 0:
        fl = True
        break

if fl:
    print('OK')
else:
    print('NG')