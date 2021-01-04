N = int(input())

L = []
L_ex = []

for i in range(N):
    S = input()
    if S[0] == '!':
        L_ex.append(S[1:])
    else:
        L.append(S)

L_Lex_and = list(set(L) & set(L_ex))

if len(L_Lex_and) == 0:
    print('satisfiable')
else:
    print(L_Lex_and[0])