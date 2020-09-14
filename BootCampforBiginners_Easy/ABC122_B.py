def main():
    s = str(input())
    slist = list(s)
    stk = []
    c = []
    lenmax = 0

    for i in range(len(slist)):
        if slist[i] == 'A' or slist[i] =='C' or slist[i] =='G' or slist[i] =='T':
            stk.append(slist[i])
            if i == len(slist) - 1:
                c.append(stk)
        else:
            c.append(stk)
            if len(stk) > 0:
                stk = []
                c.append(stk)
            stk = []

    for j in range(len(c)):
        if len(c[j]) > lenmax:
            lenmax = len(c[j])
 
    print(lenmax)


if __name__ == "__main__":
    main()