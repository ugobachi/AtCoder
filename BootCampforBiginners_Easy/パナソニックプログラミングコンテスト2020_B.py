n,m = (int(x) for x in input().split())
 
mul = int(n*m)
 
if n == 1 or m == 1:
    print(1)
elif mul % 2 == 1:
    print(mul // 2 + 1)
elif mul % 2 == 0:
    print(mul //2)