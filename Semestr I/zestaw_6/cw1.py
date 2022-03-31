"""
Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
cyfry.
"""
from math import sqrt

def pomoc(n):
    tab = set()
    k = 0
    def wypisz_pierwsze(n,tab, k):
        if len(str(n)) > 1:
            czy_pierwsza = True
            for x in range(2, int(sqrt(n)) + 1):
                if n % x == 0:
                    czy_pierwsza = False
                    break

            if czy_pierwsza and n not in tab:
                tab.add(n)

            else:
                for p in range(len(str(n))):
                    i = 0
                    c = n
                    result = 0
                    while c != 0:
                        if i == p:
                            c //= 10
                            i += 1
                        else:
                            result = result*10 + c%10
                            c //= 10
                            i += 1
                    odwrotna = 0
                    while result != 0:
                        odwrotna = odwrotna*10 + result%10
                        result //= 10
                    wypisz_pierwsze(odwrotna, tab, k)

    wypisz_pierwsze(n, tab, k)
    return tab

print(pomoc(123465678))