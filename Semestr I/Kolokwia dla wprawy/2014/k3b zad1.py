"""
Dana jest tablica wypełniona liczbami naturalnymi:
const int N=1000;
int t[N][N];
Proszę napisać funkcję, która w poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku
prawo-dół, liczącego co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić
informacje czy udało się znaleźć taki ciąg oraz długość tego ciągu
"""
from random import randint

def funkcja(t):
    if len(t) < 3:
        return "Nie da się"

    else:
        p = len(t) - 1
        k = p  - 2
        biggest = 2
        while k != 0:
            kol = 0
            k_copy = k
            first_q = t[k_copy + 1][kol + 1] / t[k_copy][kol]
            geo_count = 1
            while k_copy < p:
                if t[k_copy + 1][kol + 1] / t[k_copy][kol] == first_q:
                    geo_count += 1
                    if geo_count > biggest:
                        biggest = geo_count
                        print(k_copy, kol, "Dolna strona")

                else:
                    geo_count = 1

                k_copy += 1
                kol += 1

            kol = k
            k_copy = 0
            first_q = t[k_copy + 1][kol + 1] / t[k_copy][kol]
            geo_count = 1
            while kol < p:
                if t[k_copy + 1][kol + 1] / t[k_copy][kol] == first_q:
                    geo_count += 1
                    if geo_count > biggest:
                        biggest = geo_count
                        print(k_copy, kol, "Górna strona")

                else:
                    geo_count = 1

                k_copy += 1
                kol += 1

            k -= 1

        return biggest


t = [[randint(1, 3) for _ in range(10)] for _ in range(10)]
for x in t:
    print(x)


print(funkcja(t))