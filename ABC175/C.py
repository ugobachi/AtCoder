import math
X, K, D = map(int, input().split())

if abs(X) >= K*D:
    print(abs(X) - K*D)
else:
    quo = X // D
    rem = X % D
    opp = D - rem
    if (K - quo) % 2 == 0:
        print(rem)
    else:
        print(opp)
