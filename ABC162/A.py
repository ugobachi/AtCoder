"""[solution]
入力をリスト化して、フラグを用意
リスト内でfor文を回し、7が含まれていたらフラグをTrueにする
フラグによって出力を変える
"""

N = list(input())

flag = False

for i in N:
    if i == '7':
        flag = True

if flag == True:
    print('Yes')
else:
    print('No')