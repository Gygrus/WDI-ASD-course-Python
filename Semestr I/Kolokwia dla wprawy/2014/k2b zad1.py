"""
Na szachownicy o wymiarach 201 wierszy i 201 kolumn umieszczono pewną liczbę wież
szachowych tak, że każde z pól na jest szachowane. Przyszedł zły człowiek i zmienił położenie jednej z
wież na szachownicy, tak że nie wszystkie pola są szachowane. Proszę zaproponować funkcję, która
znajdzie przeniesienie jednej wieży tak aby ponownie wszystkie pola były szachowane. Do funkcji
przekazujemy tablicę bool t[201][201] z układem wież po zmianie, funkcja powinna wyznaczyć i
zwrócić dwa pola (wiersz, kolumna) – skąd , dokąd należy przenieść wieżę
"""
from random import randint

def fix_chess(t):

    def zerowanie(t):
        tab = [[1 for _ in range(len(t))] for _ in range(len(t))]
        for p in t:
            for x in range(len(t)):
                if tab[p[0]][x] != tab[p[0]][p[1]]:
                    tab[p[0]][x] = 0
                if tab[x][p[1]] != tab[p[0]][p[1]]:
                    tab[x][p[1]] = 0


        missing_space = []
        for p in range(len(tab)):
            for k in range(len(tab)):
                if tab[p][k] != 0:
                    missing_space.append([p, k])

        for x in tab:
            print(x)

        return tab, missing_space

    tab = [[1 for _ in range(len(t)) for _ in range(len(t))]]
    tab, missing_space = zerowanie(t)
    print()
    for i in tab:
        print(i)
    print(tab)
    print(missing_space)

    for x in range(len(t)):
        for y in range(len(missing_space)):
            if t[x][0] == missing_space[y][0]:
                temp = t[x]
                t[x][1] = missing_space[y][1]
                new, check = zerowanie(t)
                if check:
                    t[x] = temp
                else:
                    return t[x], missing_space[y]

            if t[x][1] == missing_space[y][1]:
                temp = t[x]
                t[x][0] = missing_space[y][0]
                new, check = zerowanie(t)
                if check:
                    t[x] = temp
                else:
                    return t[x], missing_space[y]



#t = [[randint(0, 9) for _ in range(2)] for _ in range(10)]
t = [[0, 0], [1, 1], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]
for x in t:
    print(x)
print(len(t))
print(fix_chess(t))