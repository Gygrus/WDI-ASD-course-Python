"""
Dany jest zbiór punktów leżących na płaszczyźnie opisany przy pomocy struktury dane =
[(x1, y1),(x2, y2),(x3, y3), ...(xN , yN )] Proszę napisać funkcję, która zwraca wartość True jeżeli zbiorze istnieją 4 punkty wyznaczające kwadrat o bokach równoległych do osi układu współrzędnych, a wewnątrz
tego kwadratu nie ma żadnych innych punktów. Do funkcji należy przekazać strukturę opisującą położenie
punktów.
"""
from random import randint

def czy_istnieje(dane):

    for x in dane:
        print(x)
        for y in dane:
            if x != y:
                if x[0] == y[0]:
                    for z in dane:
                        if x != z and y != z:
                            if x[1] == z[1] and abs(x[0] - z[0]) == abs(x[1] - y[1]):
                                for w in dane:
                                    if x != w and y != w and z != w:

                                        if y[1] == w[1] and z[0] == w[0]:
                                            check = True

                                            for k in dane:
                                                if k[0] > min(x[0], z[0]) and k[0] < max(x[0], z[0]) and k[1] > min(x[1], y[1]) and k[1] < max(x[1], y[1]):
                                                    check = False
                                                    break

                                            if check:
                                                return "Da się, koordynaty to: ", x, y, z, w

                                            else:
                                                break



# dane = [(randint(-50, 50), randint(-50, 50)) for _ in range(100)]


dane = [(3, 7), (-1, 7), (3, 11), (0, 54), (-1, 11), (4, 9)]

print(czy_istnieje(dane))