"""[solution]
500で割った時の商と5で割った商をそれぞれの嬉しさにかけて足し算
"""

X = int(input())

A = X // 500

X = X % 500

B = X // 5

calc = A*1000 + B*5

print(calc)