def zadanie1_2(n):
    zapis_dwojkowy = 0  # Liczba całkowita reprezentująca zapis dwójkowy
    miejsca_jedynek = 0  # Liczba całkowita reprezentująca pozycje jedynek
    pozycja = 1  # Pozycja bitu (liczona od 1)
    potega = 1  # Potęga 10 do budowy liczby zapis_dwojkowy
    potega_miejsca = 1  # Potęga 10 do budowy liczby miejsca_jedynek

    while n > 0:
        reszta = n % 2
        zapis_dwojkowy += reszta * potega
        if reszta == 1:
            miejsca_jedynek += pozycja * potega_miejsca
            potega_miejsca *= 10
        n //= 2
        potega *= 10
        pozycja += 1

    return zapis_dwojkowy, miejsca_jedynek


print(zadanie1_2(42))  # (101010, 153)
