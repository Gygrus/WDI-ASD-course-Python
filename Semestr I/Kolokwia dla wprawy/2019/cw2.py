"""
 Dana jest tablica int t[N][N] zawierająca liczby naturalne. Proszę napisać funkcję, która sprawdza czy z tablicy
można usunąć jeden wiersz i dwie kolumny, tak aby każdy z pozostałych elementów tablicy w zapisie dwójkowym
posiadał nieparzystą liczbę jedynek.
"""
from random import randint


def f(t):
    # x = 0
    # while x != len(t):
    #     print('x', x)
    #
    #     y = 0
    #     while y != len(t) - 1:
    #         print('y', y)
    #         z = y + 1
    #         while z != len(t):
    #             print('z', z)
    #
    #             pom = True
    #             for k in range(len(t)):
    #                 if not pom:
    #                     break
    #                 for p in range(len(t)):
    #                     if k != x and p != z and p != y:
    #                         count = 0
    #                         supp = t[k][p]
    #                         while supp != 0:
    #                             if supp % 2 == 1:
    #                                 count += 1
    #                             supp //= 2
    #
    #                         if count % 2 == 0:
    #                             print(x, y, z, k, p, t[k][p])
    #                             pom = False
    #                             break
    #
    #             if pom:
    #                 return "Da się, trzeba wykreślić wiersz", x, 'kolumny', y, z
    #
    #             z += 1
    #
    #         y += 1
    #
    #     x += 1
    #
    # return "Nie da się"
    def licznik(k):
        count = 0
        while k != 0:
            if k % 2 == 1:
                count += 1
            k = k // 2
        if count % 2 == 1:
            return True
        else:
            return False

    for x in range(len(t)):
        for y in range(len(t) - 1):
            for z in range(y+1, len(t)):
                check = True
                for p in range(len(t)):
                    if p != x and check:
                        for l in range(len(t)):
                            if l != y and l != z and check:
                                check = licznik(t[p][l])

                if check:
                    return "można, jest to wiersz", x, 'oraz kolumny', y, 'i', z

    return "nie można :("




t = [0]*4
for x in range(len(t)):
    t[x] = [randint(1, 10) for _ in range(4)]

for x in t:
    print(x)


print(f(t))