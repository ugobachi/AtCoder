"""[solution]
3でも5でも割り切れない数字のみ配列に入れる
配列内の要素をsumして出力
"""

N = int(input())

l = []

for i in range(1, N+1):
    if i % 3 != 0 and i % 5 != 0:
        l.append(i)

result = sum(l)

print(result)