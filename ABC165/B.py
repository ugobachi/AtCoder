"""[solution]

"""

X = int(input())

cnt = 0
first = 100

while True:
    first += int(first*0.01)
    cnt += 1
    if X <= first:
        break

print(cnt)
