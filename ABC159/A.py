N, M = map(int, input().split())

if N == 1 and M == 1:
    print('0')
elif N == 1:
    calc = (M * (M-1)) // 2
    print(calc)
elif M == 1:
    calc = (N * (N-1)) // 2
    print(calc)
else:
    calc = (M * (M-1)) // 2 + (N * (N-1)) // 2
    print(calc)