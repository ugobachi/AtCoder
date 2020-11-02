N = int(input())
# 初項1, 等差1, 項数Nの等差数列の和の公式：1/2n{2a+(n-1)d}
N -= 1 
calc =  N * (N+1) // 2
print(calc)