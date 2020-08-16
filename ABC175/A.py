S = list(input())

if S[0] == S[1] == S[2] == 'R':
    print(3)
elif S[0] == S[1] == 'R' or S[1] == S[2] == 'R':
    print(2) 
elif (S[0] == 'R' or S[2] == 'R') and S[1] == 'S':
    print(1)
elif (S[0] == 'S' and S[2] == 'S') and S[1] == 'R':
    print(1)
elif S[0] == S[1] == S[2] == 'S':
    print(0)

