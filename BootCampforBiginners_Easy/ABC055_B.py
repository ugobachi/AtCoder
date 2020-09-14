# でかい数の計算には時間がかかるので、10^9+7のあまりを求めながら更新していく

N = int(input())
calc = 1
for i in range(1, N+1):
    calc = (i*calc) % (10**9+7)

print(calc)
