"""[solution]
入力をリストで扱う
for文でRGBの数を数える
その後等間隔で３文字が違うものを例外ケースとして数えておく
(Rの数)*(Gの数)*(Bの数) - (例外)

※なんとPython3で提出するとTLEし、PyPyで提出すると通ってしまう
"""

N = int(input())
S = list(input())

Rcnt = 0
Gcnt = 0

excep = 0

for i in range(len(S)):
    if S[i] == 'R':
        Rcnt += 1
    elif S[i] == 'G':
        Gcnt += 1
    for j in range(1, len(S)):
        if i+j+j < len(S) and S[i] != S[i+j]:
            if S[i] != S[i+j+j] and S[i+j] != S[i+j+j]:
                excep += 1
        elif i+j+j >= len(S):
            break

RGBcalc = Rcnt * Gcnt * (N - Rcnt - Gcnt)

print(RGBcalc - excep)