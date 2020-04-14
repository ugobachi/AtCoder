"""[solution]
スタートとゴールの位置及びそれぞれの家の位置を配列に入れる
スタートとゴールの合計と家の距離の最大を求める
どっちが大きいかによって通るルートが決まる
距離の合計 - 距離が大きい方
"""

K, N = map(int, input().split())
A = list(map(int, input().split()))

A.insert(0, 0)
A.append(K)

# print(A)

start = A[1] - A[0]
goal = A[-1] - A[-2]

mixi = 0
sum_len = 0

SandG = start + goal

for i in range(len(A) - 1):
    if A[i+1] - A[i] > mixi:
        mixi = A[i+1] - A[i]
    sum_len += A[i+1] - A[i]

if max(SandG, mixi) == SandG or SandG == mixi:
    result = sum_len - (start + goal)
elif max(SandG, mixi) == mixi:
    result = sum_len - mixi

print(result)
    
