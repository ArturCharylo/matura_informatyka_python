# Include a dummy element at index 0 for 1-based indexing
T = [0, 6, -4, 12, 27, 26, 8]
n = 6


def d(x):
    global n  # Declare n as global to modify it
    n += 1
    if n >= len(T):  # Dynamically expand the list if needed
        T.append(0)
    T[n] = x
    s = n
    while (s // 2) >= 1 and T[s] > T[s // 2]:
        # Swap T[s] with its parent T[s // 2]
        T[s], T[s // 2] = T[s // 2], T[s]
        s = s // 2
    return T


wynik = d(6)
print(wynik)
