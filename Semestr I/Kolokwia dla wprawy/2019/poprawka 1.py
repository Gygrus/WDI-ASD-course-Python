"""
Tablica tab jest wypełniona liczbami naturalnymi. Na szachownicy umieszczamy dwa klocki domina tak, że jeden
klocek przykrywa dwa pola. Proszę napisać funkcję, która sprawdza czy istnie takie ustawianie klocków na
szachownicy, że:
- oba klocki są prostopadle do siebie,
- w żadnym wierszu ani w żadnej kolumnie nie leży więcej niż jeden klocek,
- największym wspólnym dzielnikiem 4 przykrytych liczb jest jeden.
"""
from random import randint

def czy_istnieje(tab):
    for x in range(len(tab)):
        for y in range(len(tab) -1):
            wsp_1 = tab[x][y]
            wsp_2 = tab[x][y+1]
            z = True
            for p in range(2, min(wsp_1, wsp_2) + 1):
                if wsp_1 % p == 0 and wsp_2 % p == 0:
                    z = False
                    break

            if z:
                for x_1 in range(len(tab) - 1):
                    if x_1 != x and x_1 + 1 != x:
                        for y_1 in range(len(tab)):
                            if y_1 != y and y_1 != y + 1:
                                sec_1 = tab[x_1][y_1]
                                sec_2 = tab[x_1 + 1][y_1]
                                z_1 = True
                                for i in range(2, min(sec_1, sec_2) + 1):
                                    if sec_1 % i == 0 and sec_2 % i == 0:
                                        z_1 = False
                                        break

                                if z_1:
                                    return True, (x, y), (x_1, y_1), (tab[x][y], tab[x][y+1]), (tab[x_1][y_1], tab[x_1 + 1][y_1])



tab = [0]*3
for x in range(len(tab)):
    tab[x] = [randint(1, 10) for _ in range(3)]
    print(tab[x])

print(czy_istnieje(tab))