"""[solution]
入力を配列で扱って2番目と3番目、4番目と5番目の要素が一致しているものをYes
それ以外はNoを出力
"""

S = list(input())

if S[2] == S[3] and S[4] == S[5]:
    print('Yes')
else:
    print('No')