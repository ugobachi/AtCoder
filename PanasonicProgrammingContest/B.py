# coding:utf-8

"""[solution]
縦横を指定する整数の変数n, m
例えば、2×2の4マスの盤面であれば半分の2マス分が駒の移動できる範囲なので
縦×横が偶数の場合はその半分を出力、奇数であれば半分+1マスを出力
縦もしくは横が1マスしか無かった場合、それ以上移動はできないので、1を出力
"""

n,m = (int(x) for x in input().split())

mul = int(n*m)

if n == 1 or m == 1:
    print(1)
elif mul % 2 == 1:
    print(mul // 2 + 1)
elif mul % 2 == 0:
    print(mul //2)
