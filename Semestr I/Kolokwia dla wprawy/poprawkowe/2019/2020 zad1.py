"""
1. Dane są deklaracje reprezentujące szachownicę o boku długości N:
const int N= …
int tab[N][N];
Tablica tab jest wypełniona liczbami naturalnymi. Na szachownicy umieszczamy dwa klocki domina tak, że jeden
klocek przykrywa dwa pola. Proszę napisać funkcję, która sprawdza czy istnie takie ustawianie klocków na
szachownicy, że:
- oba klocki są prostopadle do siebie,
- w żadnym wierszu ani w żadnej kolumnie nie leży więcej niż jeden klocek,
- największym wspólnym dzielnikiem 4 przykrytych liczb jest jeden.
"""
from random import randint



def NWD(a, b):
    while True:
        print('gówno')
        if a % b == 0:
            return b
        c = a
        a = b
        b = c % b

#print(NWD(1001, 49))

def check_if_is_possible(T):
    for poziom in range(len(T)):
        for p in range(len(T)-1):
            horizontal_values = (T[poziom][p], T[poziom][p+1])
            for x in range(len(T)-1):
                if x == poziom or x+1 == poziom:
                    pass
                else:
                    for y in range(len(T)):
                        if y == p or y == p+1:
                            pass
                        else:
                            vertical_values = (T[x][y], T[x+1][y])
                            if NWD(NWD(NWD(horizontal_values[0], horizontal_values[1]), vertical_values[0]), vertical_values[1]) == 1:
                                return ((poziom, p), (poziom,p+1)), horizontal_values, ((x, y), (x+1, y)), vertical_values

        return False


T = [[randint(1, 10) for _ in range(10)] for _ in range(10)]
for x in T:
    print(x)
print(check_if_is_possible(T))


