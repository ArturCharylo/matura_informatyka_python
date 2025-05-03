def suma_kw_cyfr(n):
    # Znajdź największe miejsce dziesiętne
    digit_place = 1
    while n // digit_place >= 10:
        digit_place *= 10

    suma = 0  # Zmienna do przechowywania sumy kwadratów cyfr

    # Iteruj po cyfrach liczby
    while digit_place > 0:
        digit = n // digit_place  # Wyciągnij najbardziej znaczącą cyfrę
        suma += digit * digit  # Dodaj kwadrat cyfry do sumy
        n %= digit_place  # Usuń najbardziej znaczącą cyfrę z liczby
        digit_place //= 10  # Przejdź do kolejnego miejsca dziesiętnego

    return suma


def czy_nudna(n):
    digit_place = 1
    while n // digit_place >= 10:
        digit_place *= 10
    suma = 0

    while digit_place > 0:
        digit = n // digit_place
        if digit == 1:
            return False
        suma += digit * digit
        n %= digit_place
        digit_place //= 10
    return True


n = 123
print(suma_kw_cyfr(n))
print(czy_nudna(n))
