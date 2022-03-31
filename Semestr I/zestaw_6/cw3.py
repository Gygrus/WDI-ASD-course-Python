"""
Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie
k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
polu startowym i ostatnim także wliczamy do kosztu przejścia.
"""
from random import randint

def func(T, k, w, sum, minimal):
    sum += T[w][k]
    if w == 7:
        if sum < minimal:
            minimal = sum
        return sum


    else:
        if k == 7:
            return min(func(T, k, w+1, sum, minimal), func(T, k-1, w+1, sum, minimal))
        elif k == 0:
            return min(func(T, k, w+1, sum, minimal), func(T, k+1, w+1, sum, minimal))
        else:
            return min(func(T, k, w+1, sum, minimal), func(T, k-1, w+1, sum, minimal), func(T, k+1, w+1, sum, minimal))

def rek(T, k):
    minimal = 10**10
    sum = 0
    return func(T, k, 0, sum, minimal)


T = [[randint(1, 8) for _ in range(8)] for _ in range(8)]
for x in T:
    print(x)

print(rek(T, 0))