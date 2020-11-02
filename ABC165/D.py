A, B, N = map(int, input().split())


if N >= B:
    X = (A*(B-1)) // B
    Y = A * ((B-1)//B)
    print(X-Y)
else:
    X = (A*N) // B
    Y = A * (N//B)
    print(X-Y)

