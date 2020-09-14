M = [int(input()) for i in range(5)]
li = []
 
total = 0
 
for i in M:
    if i % 10 == 0:
        total += i
    else:
        total += i
        total += 10 - (i%10)
        li.append(i%10)
 
print(total - (10 - (10 if not li else min(li))))