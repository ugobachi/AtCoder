S = list(input())

S.append('end')

print(S)

cnt = 0
res = 0

for i in range(len(S)-1):
    print(S[i])

    if S[i+1] == 'end':
        cnt += 1
        res += cnt
    if S[i] == S[i+1] == '<' or (S[i] == '>' and S[i+1] == '<'):
        cnt += 1
    elif S[i] == S[i+1] == '>' or (S[i] == '<' and S[i+1] == '>'):
        cnt -= 1
        cnt = max(0, cnt)
    print(cnt)
    res += cnt

print(res)