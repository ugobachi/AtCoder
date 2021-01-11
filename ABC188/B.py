N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
calc = 0

for i, j in zip(A, B):
    calc += (i*j)

if calc == 0:
    print('Yes')
else:
    print('No')