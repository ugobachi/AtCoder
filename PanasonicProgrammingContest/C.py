# coding: utf-8

"""[solution]
√a + √b < √cかどうかを判定するプログラム
a, b, cの整数の変数
srqtを使うと小数になってしまうため、小数を使わないアプローチを採用
大小比較は両辺を二乗しても可能
a + 2√ab + b < c
まだ√が残っているので、式変形して二乗する
c - a - b > 2√ab
これを二乗して
(c - a - b)^2 > 4ab
また、a + bがcより大きければ絶対に√a + √b < √cを満たさないのでこの条件も追加
条件を満たすもののみをYesを出力
"""

a,b,c = (int(x) for x in input().split())

if (c - a - b)**2 > 4 * a * b and c - a - b > 0:
    print('Yes')
else:
    print('No')