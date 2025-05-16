def zadanie3_1():
    with open("liczby.txt", 'r') as file:
        kw_calk = 0
        for line in file:
            liczba = int(line.strip())
            if czy_kwadrat(liczba):
                print(liczba)
                kw_calk += 1
        return kw_calk


def czy_kwadrat(liczba):
    i = 1
    while i * i <= liczba:
        if i * i == liczba:
            return True
        i += 1
    return False


def zadannie3_2():
    with open("liczby.txt", 'r') as file:
        ilosc_dzielnikow = 0
        ilosc_liczb = 0
        for line in file:
            liczba = int(line.strip())
            ilosc_dzielnikow = ile_dzielnikow(liczba)
            if ilosc_dzielnikow >= 5:
                ilosc_liczb += 1
                print(liczba)
        return ilosc_liczb


def ile_dzielnikow(liczba):
    i = 1
    ilosc_dzielnikow = 0
    while i <= liczba:
        if czy_pierwsza(i) and liczba % i == 0:
            ilosc_dzielnikow += 1
        i += 1
    return ilosc_dzielnikow


def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # dzielniki tylko do pierwiastka z n
        if n % i == 0:
            return False
    return True


def procedura(liczba):
    # Zapewniamy, że liczba ma 4 cyfry (np. 0023)
    cyfry = list(str(liczba).zfill(4))
    najwieksza = int("".join(sorted(cyfry, reverse=True)))
    najmniejsza = int("".join(sorted(cyfry)))
    return najwieksza - najmniejsza


def zadanie3_3():
    mniejsze = wieksze = rowne = 0
    rowne_liczby = []

    with open("liczby.txt", "r") as file:
        for line in file:
            liczba = int(line.strip())
            roznica = procedura(liczba)

            if roznica < liczba:
                mniejsze += 1
            elif roznica > liczba:
                wieksze += 1
            else:
                rowne += 1
                rowne_liczby.append(liczba)

    print(f"Liczb, dla których różnica jest mniejsza niż liczba: {mniejsze}")
    print(f"Liczb, dla których różnica jest większa niż liczba: {wieksze}")
    print(f"Liczb, dla których różnica jest równa liczbie: {rowne}")
    for l in rowne_liczby:
        print(l)


zadanie3_3()
