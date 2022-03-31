"""
Dana jest tablica wypełniona liczbami naturalnymi:
const int N=1000; int t[N][N];
Proszę napisać funkcję, która poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą
większą od 1, którego iloczyn 4 pól narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość
k. Funkcja powinna zwrócić informacje czy udało się znaleźć kwadrat oraz współrzędne (wiersz,
kolumna) środka kwadratu.
"""
from random import randint

def funkcja(t, k):
    z = 2
    while z < len(t):
        i = 0
        while len(t) - (i + z) > 0:
            p = 0
            while len(t) - (p + z) > 0:
                print(f"""
                                    {t[i][p]} {t[i][p + z]}
                                    {t[i + z][p]} {t[i + z][p + z]}""")
                if t[i][p] * t[i][p + z] * t[i + z][p] * t[i + z][p + z] == k:
                    # print(f"""
                    # {t[i][k]} {t[i][k + z]}
                    # {t[i + z][k]} {t[i + z][k + z]}""")
                    return True, [i + z//2, p + z//2], z, i, p

                p += 1

            i += 1

        z += 2
    return None


t = [[randint(1, 5) for _ in range(10)] for _ in range(10)]
for x in t:
    print(x)


print(funkcja(t, 24))