N = int(input())

c = list(input())

cnt = 0
headcnt = 0
tailcnt = -1

Noflag = 0

while True:
    if c[tailcnt] == 'R' and Noflag == 0:
        while True:
            if c[headcnt] == 'W':
                c[headcnt], c[tailcnt] = c[tailcnt], c[headcnt]
                cnt += 1
                break
            else:
                headcnt += 1
                if headcnt + abs(tailcnt) >= len(c):
                    Noflag += 1
                    break
    elif c[tailcnt] == 'W' or Noflag == 1:
        tailcnt -= 1
        if headcnt + abs(tailcnt) >= len(c):
            print(cnt)
            break
