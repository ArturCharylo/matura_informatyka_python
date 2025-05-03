n = 4999
d = 0
waga = 1
while n > 0:
    cyfra = n % 10
    dopelnienie = 9 - cyfra
    d += dopelnienie * waga
    waga *= 10
    n //= 10
print(d)
