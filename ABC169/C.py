from decimal import Decimal

"""
float*整数は誤差が生じることがあるのでdecimalモジュールを使ってBを定義
参考 - https://docs.python.org/ja/3/library/decimal.html

Bを100倍して(A × (B × 100))/100としても誤差が生じずに計算できる
"""

A, B = input().split()

A = int(A)
B = Decimal(B)

C = A*B
C = int(C)

print(C)