"""
ソートして頭の要素が0ならそのまま0出力
前から掛けて行って10^18桁をオーバーしたら-1出力
"""

N = int(input())

A = input().split()
result = 1

A.sort()
fl = True

if int(A[0]) == 0:
    print(0)
else:
    for i in A:
        result *= int(i)
        if result > 10**18:
            fl = False   
            break                
    if fl:
        print(result)
    else:
        print(-1)

