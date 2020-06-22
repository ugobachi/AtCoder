N = int(input())
 
amalist = []

while True:
    N -= 1
    num = N % 26
    amalist.append(num)
    N = N // 26
    if N == 0:
        break

amalist.reverse()

alphalist = [chr(i) for i in range(97,97+26)]

result = []
for i in amalist:
    result.append(alphalist[i])

print(''.join(result))