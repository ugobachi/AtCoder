# coding: utf-8

A, B = map(int, input().split())

x = A / 0.08

y = B / 0.1

result = max(x, y)

print(x, y)

if x < y:
    print('-1')
elif x == y:
    print(x)
elif x >= y:
    pass


