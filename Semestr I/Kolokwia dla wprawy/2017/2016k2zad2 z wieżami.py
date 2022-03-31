"""
Dana jest tablica t[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na
„szachowanych” przez wieże polach była największa. Do funkcji należy przekazać tablicę,
funkcja powinna zwrócić położenie wież.
"""
from random import randint


def f(t):

    lines = [0]*len(t)
    cols = [0]*len(t)

    for x in range(len(t)):
        for k in range(len(t)):
            lines[x] += t[x][k]
            cols[x] += t[k][x]
    tab_of_cord = [(),()]
    result = [0, 0]
    for i in range(2):
        maximum = 0
        for x in range(len(t)):
            for y in range(len(t)):
                temp = lines[x] + cols[y] - t[x][y]
                if i == 1:
                    temp -= t[x][tab_of_cord[0][1]] + t[tab_of_cord[0][0]][y]

                if temp > maximum:
                    maximum = temp
                    tab_of_cord[i] = (x, y)
                    result[i] = temp

        lines[tab_of_cord[i][0]] = 0
        cols[tab_of_cord[i][1]] = 0

    return tab_of_cord, result


t = [0]*8
print(t)
for x in range(len(t)):
    t[x] = [randint(1, 20) for _ in range(8)]
    print(t[x])

print(f(t))
