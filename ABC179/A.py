S = list(input())

if S[-1] == 's':
    S.append('es')
else:
    S.append('s')

print(''.join(S))