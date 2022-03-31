"""
 Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać funkcję, która
sprawdza czy z każdej z tablic można wyciąć po jednym kawałku, tak aby suma elementów w obu kawałkach była:
co najmniej drugą potęgą dowolnej liczby naturalnej. Łączna długości obu kawałków powinna wynosić 24.
"""
from random import randint


def f(t1, t2):
    dlugosc_1 = 1
    dlugosc_2 = 23
    while dlugosc_1 <= 23:
        for x in range(len(t1) - dlugosc_1):
            new_1 = t1[x:x + dlugosc_1]
            for i in range(len(t2) - dlugosc_2):
                new_2 = t2[i:i + dlugosc_2]

            suma = 0
            wszystkie = new_1 + new_2
            for k in wszystkie:
                suma += k
            if suma == 1:
                return "Jest, to potęga 1"
            else:
                podstawa = 2
                potega = 2
                while podstawa ** potega <= suma:
                    potega = 2
                    while podstawa ** potega <= suma:
                        if suma == podstawa ** potega:
                            return f"jest, jest to {potega} potęga liczby {podstawa}"

                        potega += 1
                    podstawa += 1

        dlugosc_1 += 1
        dlugosc_2 -= 1

    return "Nie ma"




t1 = [randint(1, 100) for _ in range(100)]
t2 = [randint(1, 100) for _ in range(100)]

print(f(t1, t2))