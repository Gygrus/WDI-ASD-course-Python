"""
Dane s¡ deklaracje:
const int N=1000;
int tab[N];
Tablica tab jest wypeªniona liczbami naturalnymi. Prosz¦ napisa¢ funkcj¦, która zwraca dªugo±¢ najdªu»szego
spójnego podci¡gu rosn¡cego, dla którego suma jego elementów jest równa sumie indeksów tych elementów.
Do funkcji nale»y przekaza¢ tablic¦, funkcja powinna zwróci¢ dªugo±¢ znalezionego podci¡gu, lub warto±¢ 0,
je»eli taki podci¡g nie istnieje
"""
from random import randint


def f(tab):
    x = 0
    maximum = 1
    while x < len(tab):
        pom = tab[x]
        sum_of_el = pom
        sum_of_in = x
        length_count = 1
        for i in range(x + 1, len(tab)):
            if tab[i] > pom:
                length_count += 1
                pom = tab[i]
                sum_of_el += pom
                sum_of_in += i
                if sum_of_el == sum_of_in and length_count > maximum:
                    maximum = length_count

            else:
                pom = tab[i]
                length_count = 1
                sum_of_el = pom
                sum_of_in = i

        x += 1

    return maximum if maximum > 1 else 0


tab = [randint(0, 100) for _ in range(1000)]

#tab = [2, 3, 4, 0, 1, 2, 3, 4, 5, 9, 22, 23, 42, 26342, 0, 52, 23]

print(f(tab))