# coding: utf-8
"""[solution]
DFS
"""

N = int(input())
alphabets = 'abcdefghij'

def dfs(s, mx):
    if len(s) == N:
        print("".join(s))
    else:
        t = min(len(set(s))+1,len(s)+1)
        for c in range(t):
            dfs(s + [alphabets[c]], c)

if __name__ == "__main__":
    dfs([], 0)
