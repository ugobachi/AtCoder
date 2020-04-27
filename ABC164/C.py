"""[summary]
入力をリストに格納してソートする
l[i]とl[i+1]の文字列を比較して同じでなかったらカウントを増やす
"""

N = int(input())
l = []

for i in range(N):
    S = input()
    l.append(S)

l.sort()
cnt = 1

for i in range(len(l) - 1):
    if l[i] != l[i+1]:
        cnt += 1

print(cnt)