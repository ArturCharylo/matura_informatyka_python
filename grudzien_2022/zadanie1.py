def zadanie1_1():
    with open("mecz.txt", "r") as file:
        wygrane = []
        zmiany = 0
        temp = ''
        for line in file:
            for char in line.strip():
                wygrane.append(char)
        for el in wygrane:
            if el != temp and temp != '':
                zmiany += 1
            temp = el
        print(zmiany)


def zadanie1_2():
    with open("mecz.txt", "r") as file:
        zwyciestaa = 0
        zwyciestab = 0
        for line in file:
            for char in line.strip():
                if char == 'A':
                    zwyciestaa += 1
                elif char == 'B':
                    zwyciestab += 1
                if zwyciestaa == 1000 or zwyciestab == 1000:
                    break
            if zwyciestaa == 1000 or zwyciestab == 1000:
                break
        print("A:", zwyciestaa)
        print("B:", zwyciestab)


def zadanie1_3():
    with open("mecz.txt", "r") as file:
        data = file.read().strip()

    current_team = ''
    current_streak = 0

    good_streaks = 0
    longest_streak = 0
    longest_team = ''

    i = 0
    while i < len(data):
        current_team = data[i]
        current_streak = 1
        i += 1

        while i < len(data) and data[i] == current_team:
            current_streak += 1
            i += 1

        if current_streak >= 10:
            good_streaks += 1
            if current_streak > longest_streak:
                longest_streak = current_streak
                longest_team = current_team

    print("Liczba dobrych pass:", good_streaks)
    print("Najdłuższa dobra passa:", longest_streak)
    print("Drużyna z najdłuższą passą:", longest_team)


def zadanie2_1():
    def strzalka(x, y):
        print(f"Strzałka od {x} do {y}")

    def rysuj(x, N):
        if 2 * x <= N:
            strzalka(x, 2 * x)
            rysuj(2 * x, N)
        if 2 * x + 1 <= N:
            strzalka(x, 2 * x + 1)
            rysuj(2 * x + 1, N)

    N = 20
    rysuj(1, N)


def zadanie2_4():
    def czy_potomny(x, y):
        while y > 0:
            if y == x:
                return True
            y //= 2
        return False

    def sprawdz_pary(plik, N):
        with open(plik, 'r') as f:
            for line in f:
                x, y = map(int, line.strip().split())
                if czy_potomny(x, y):
                    print(f"{x} {y}")

    N = 100_000
    sprawdz_pary("pary.txt", N)


zadanie2_4()
