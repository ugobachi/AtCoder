"""[solution]
aとbのgcdが１だった場合cがどの値であってもgcdは１なので
1*(cがとりうる値の数)だけ足す
1以外の場合はfor文でa, b, cのgcdを求める
"""

import math

N = int(input())

result = 0

for a in range(1, N+1):
    for b in range(1, N+1):
        if math.gcd(a,b) == 1:
            result += 1*N
        else:
            for c in range(1, N+1):
                result += math.gcd(math.gcd(a,b),c)

print(result)