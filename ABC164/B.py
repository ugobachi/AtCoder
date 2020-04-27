"""[summary]
C - BとA - Dを交互に行って0以下になったら出力
"""

A, B, C, D = map(int, input().split())

while True:
    C -= B
    if A <= 0:
        print('No')
        break
    A -= D
    if C <= 0:
        print('Yes')
        break