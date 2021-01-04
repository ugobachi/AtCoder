import itertools

N = list(input())

N_int = [int(s) for s in N]

maxi = sum(N_int)

if maxi%3 == 0:
    print(0)
    exit()
else:
    for i in range(1,len(N_int)):
        for comb in itertools.combinations(N_int, i):
            if (maxi - sum(comb))%3 == 0:
                print(i)
                exit()

print(-1)