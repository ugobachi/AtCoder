a, b = map(int, input().split())

c = int(str(a)+str(b))

l = []

# 10 ~ 100100までの平方数をリストに入れる
for i in range(10, 100100):
    if (i ** .5).is_integer():
        l.append(i)

for i in l:
    if c == i:
        print('Yes')
        exit()

print('No')