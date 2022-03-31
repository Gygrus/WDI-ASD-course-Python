"""
Dana jest tablica t[N][N] wypełniona liczbami całkowitymi. Tablica reprezentuje szachownicę. Proszę napisać
funkcję, która sprawdza czy da się umieścić w każdym wierszu jednego króla szachowego tak aby żadne dwa króle
nie stały w odległości mniejszej niż dwa ruchy króla. Dodatkowo, suma wartości pól zajmowanych przez wszystkie
figury była równa zero.
"""
from random import randint

def f(t, x, k, tab):
    if k < len(t):
        # print(sum(tab))
        z = x
        for i in range(len(t)):
            if k == 0:
                tab[k] = t[k][i]
                if f(t, i, k + 1, tab):
                    return True, tab
            else:
                if i < z - 1 or i > z + 1:
                    tab[k] = t[k][i]
                    if f(t, i, k + 1, tab):
                        return True, tab

    else:
        if sum(tab) == 0:
            print(sum(tab), tab)
            return True, tab



t = [0]*6
for x in range(len(t)):
    t[x] = [randint(-10, 15) for _ in range(6)]
for x in t:
    print(x)

print('\n\n\n\n')


print(f(t, 0, 0, [0]*len(t)))

