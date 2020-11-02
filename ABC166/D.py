X = int(input())
l = []
k = []


for i in range(-100, 101):
    l.append(i**5)

for i in range(len(l)):
    for j in range(len(l)):
        if l[i] == l[j] + X:
            k.append(l[i])
            k.append(l[j])

A = pow(k[2], 0.2)
B = pow(k[3], 0.2)

print(A, B)