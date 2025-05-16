liczba_wywolan = 0


def F(x, p):
    global liczba_wywolan
    liczba_wywolan += 1
    if x == 0:
        return 0
    else:
        c = x % p
        if c % 2 == 1:
            return F(x // p, p) + c
        else:
            return F(x // p, p) - c


print(F(96, 3))
