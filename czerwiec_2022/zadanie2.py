liczba_wywolan = 0


def koduj(n):
    global liczba_wywolan
    liczba_wywolan += 1
    if n == 1:
        return ''
    else:
        k = n // 2
        if k % 2 == 0:
            return koduj(k) + 'A'
        else:
            return 'B' + koduj(k)


n = 118
print(koduj(n) + "\n" + str(liczba_wywolan))
# odpowiedź dla 2.3: 122, 118
