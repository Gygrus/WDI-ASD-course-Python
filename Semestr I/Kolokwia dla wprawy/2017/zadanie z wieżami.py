"""
Dana jest tablica t[N][N] (reprezentuj¡ca szachownic¦) wypeªniona liczbami naturalnymi. Na szachownicy
znajduj¡ si¦ dwie wie»e. Prosz¦ napisa¢ funkcj¦, która odpowiada na pytanie: czy istnieje ruch wie»¡
zwi¦kszaj¡cy sum¦ liczb na "szachowanych" przez wie»e polach? Do funkcji nale»y przekaza¢ tablic¦ oraz
poªo»enia dwóch wie», funkcja powinna zwróci¢ warto±¢ logiczn¡.
Uwaga: zakªadamy, »e wie»a szachuje caªy wiersz i kolumn¦ z wyª¡czeniem pola, na którym stoi
"""
from random import randint


def f(t, cord_1, cord_2):
    sum_of_line = 0
    for x in t[cord_1[0]]:
        sum_of_line += x

    sum_of_col = 0
    for x in range(len(t)):
        sum_of_col += t[x][cord_1[1]]


    new_sum_of_line = 0
    new_sum_of_col = 0
    for y in range(t):
        for i in range(t):
            new_sum_of_line += t[y][i]
            new_sum_of_col += t[i][y]

        new_sum_of_col -= t[cord_1[0]][y]
        new_sum_of_line -= t[y][cord_1[1]]
        if new_sum_of_line > sum_of_line and y != cord_2[0]:
            return True
        if new_sum_of_col > sum_of_col and y != cord_2[1]:
            return True

    sum_of_line = 0
    for x in t[cord_2[0]]:
        sum_of_line += x

    sum_of_col = 0
    for x in range(len(t)):
        sum_of_col += t[x][cord_2[1]]

    new_sum_of_line = 0
    new_sum_of_col = 0
    for y in range(t):
        for i in range(t):
            new_sum_of_line += t[y][i]
            new_sum_of_col += t[i][y]

        new_sum_of_col -= t[cord_2[0]][y]
        new_sum_of_line -= t[y][cord_2[1]]
        if new_sum_of_line > sum_of_line and y != cord_1[0]:
            return True
        if new_sum_of_col > sum_of_col and y != cord_1[1]:
            return True



t = [0]*10
for x in t:
    x = [randint(1, 10) for _ in range(10)]
print(t)

cord_1 = (3, 6)
cord_2 = (1, 8)


print(f(t, cord_1, cord_2))



