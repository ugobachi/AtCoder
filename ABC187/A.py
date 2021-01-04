A, B = map(int, input().split())

def digitSum(n):
    s = str(n)
    array = list(map(int, list(s)))
    return sum(array)

print(max(digitSum(A), digitSum(B)))