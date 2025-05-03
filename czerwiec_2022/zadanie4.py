def zadanie4_1():
    with open("liczby.txt", 'r') as liczby:
        global odbicia
        odbicia = []
        for liczba in liczby:
            odbita = liczba.strip()[::-1]
            odbicia.append(odbita)


def zadanie4_2():
    with open("liczby.txt", 'r') as liczby:
        global max_liczba, max_roznica
        max_liczba = None
        max_roznica = 0
        for liczba in liczby:
            liczba = liczba.strip()
            odbita = int(liczba[::-1])
            roznica = abs(int(liczba) - odbita)
            if roznica > max_roznica:
                max_roznica = roznica
                max_liczba = liczba


zadanie4_1()
zadanie4_2()
with open("wyniki4.txt", 'w') as wyniki:
    wyniki.write("wyniki4.1\n")
    for odbita in odbicia:
        if int(odbita) % 17 == 0:
            wyniki.write(str(odbita) + "\n")
            print(odbita)
    wyniki.write("wyniki4.2\n")
    wyniki.write(f"Liczba: {max_liczba}, Różnica: {max_roznica}\n")
    print(f"Liczba: {max_liczba}, Różnica: {max_roznica}")
