"""
Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
wartość sumy, funkcja powinna zwrócić wartość typu bool.
"""
from random import randint

def is_possible(T, w, k, i, count_sum, check, tab_k):
    print(w, k)
    if i == 7 or w == 8:
        if count_sum == check:
            return True
        else:
            return False
    tab_k = tab_k[:]
    if k < 7:
        is_possible(T, w, k+1, i, count_sum, check, tab_k)
        if k not in tab_k:
            tab_k.append(k)
            is_possible(T, w+1, 0, i+1, count_sum+T[w][k], check, tab_k)
    else:
        is_possible(T, w+1, 0, i + 1, count_sum, check, tab_k)
        if k not in tab_k:
            is_possible(T, w+1, 0, i + 1, count_sum + T[w][k], check, tab_k)


T = [[randint(1, 3) for _ in range(8)] for _ in range(8)]
for x in T:
    print(x)

print(is_possible(T, 0, 0, 0, 0, 5, list()))