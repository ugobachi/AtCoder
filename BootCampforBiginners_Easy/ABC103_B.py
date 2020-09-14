S = input()
T = input()

def rolling(str , n):
    """[summary]
    文字列を回転させる関数
    Args:
        str ([type]): 元の文字列
        n ([type]): 何文字分回転させるか

    Returns:
        [str]: 回転後の文字列
    """    
    return str[n:len(str)] + str[:n]

for i in range(len(S)):
    if T == rolling(S, i):
        print('Yes')
        exit()

print('No')