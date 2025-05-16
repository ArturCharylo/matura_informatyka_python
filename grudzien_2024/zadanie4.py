def zadanie4_1():
    max_pole = 0
    min_pole = 999999
    with open('prostokaty.txt', 'r') as file:
        for line in file:
            line = line.strip()
            h, y = line.split()
            h = int(h)
            y = int(y)
            if h * y > max_pole:
                max_pole = h * y
            if h * y < min_pole:
                min_pole = h * y
        return max_pole, min_pole


def zadanie4_2():
    with open('prostokaty.txt', 'r') as file:
        wymiary = []
        for line in file:
            line = line.strip()
            h, y = line.split()
            h = int(h)
            y = int(y)
            wymiary.append((h, y))

        ile_max = 0
        szer = 0
        wys = 0
        ile = 1
        for i in range(len(wymiary) - 1):
            h1 = wymiary[i][0]
            y1 = wymiary[i][1]
            h2 = wymiary[i + 1][0]
            y2 = wymiary[i + 1][1]
            if h2 <= h1 and y2 <= y1:
                ile += 1
                if ile > ile_max:
                    ile_max = ile
                    szer = y2
                    wys = h2
            else:
                ile = 1
        return ile_max, wys, szer


def zadanie4_3():
    with open("prostokaty.txt", 'r') as file:
        wysokosci = {}
        for line in file:
            line = line.strip()
            h, y = line.split()
            h = int(h)
            y = int(y)
            if h not in wysokosci:
                wysokosci[h] = [y]
            else:
                wysokosci[h].append(y)
        for wysokosc in wysokosci:
            wysokosci[wysokosc].sort(reverse=True)
    return wysokosci


def wynik4_3(ilosc, wysokosci):
    max_szer = 0
    for dane in wysokosci:
        if len(wysokosci[dane]) < ilosc:
            continue
        else:
            szer_sum = sum(wysokosci[dane][:ilosc])
            if szer_sum > max_szer:
                max_szer = szer_sum
    return max_szer


wysokosci = zadanie4_3()
print(wynik4_3(2, wysokosci))
print(wynik4_3(3, wysokosci))
print(wynik4_3(5, wysokosci))
