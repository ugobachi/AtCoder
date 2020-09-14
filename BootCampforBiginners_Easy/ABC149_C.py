X = int(input())

def isPrime(n):
    """[summary]
    素数判定の関数
    Args:
        n ([int]): 判定に用いる値

    Returns:
        [bool]: 引数nが素数ならTrue, そうでないならFalseを返す
    """    
    if n < 2:
        return False
    if n == 2:
        return True
    for p in range(2, n):
        if n % p == 0:
            return False
    return True


for i in range(X, 1000000):
    if isPrime(i) == True:
        print(i)
        exit()