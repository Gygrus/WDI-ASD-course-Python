"""
Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy w tablicy istnieje wiersz, w którym każda liczba zawiera co najmniej jedną cyfrę
będącą liczbą pierwszą?
"""
from math import sqrt


def cw15(t):

    for x in t:
        k = True
        for i in x:
            czy_pierwsza = False
            for z in str(i):
                mini_k = True
                if int(z) == 1 or int(z) == 0:
                    mini_k = False

                else:
                    for p in range(2, int(sqrt(int(z))) + 1):
                        if int(z) % p == 0:
                            mini_k = False
                            break

                if mini_k:
                    czy_pierwsza = True
                    break

            if not czy_pierwsza:
                k = False
                break

        if k:
            return True, x

    return False


print(cw15([[1, 6, 34, 0, 3],
           [2, 2, 2, 2, 2],
           [0, 7, 53, 122, 0],
           [234, 4454, 78, 5125, 8697],
           [1, 0, 0, 231, 7]]))
