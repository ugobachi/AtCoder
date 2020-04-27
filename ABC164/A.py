"""[summary]
W, Sの大小比較で出力を変える
"""

S, W = map(int, input().split())

if W >= S:
    print('unsafe')
else:
    print('safe')
