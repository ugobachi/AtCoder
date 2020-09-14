s = int(input())
li = []
li.append(s)
fl = True

while fl:
    # 要素の追加
    if li[-1] % 2 == 0:
        n = int(li[-1] / 2)
        li.append(n)
    elif li[-1] % 2 == 1:
        n = li[-1]*3 + 1
        li.append(n)
 
    # 一致を調べる
    for j in range(0,len(li)-1):
        if li[j] == n:
            fl = False
 
print(len(li))