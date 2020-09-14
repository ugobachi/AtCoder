N = int(input())
v = list(map(int, input().split()))
 
for i in range(N-1):
    v.sort()
    v.append((v[0]+v[1]) / 2)
    v.remove(v[0])
    v.remove(v[0])
 
print(v[0])