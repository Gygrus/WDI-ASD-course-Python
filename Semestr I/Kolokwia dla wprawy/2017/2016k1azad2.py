"""
Proszę napisać program, który wypełnia tablicę int tab[MAX] liczbami pseudolosowymi
z zakresu [1 .. 1000], a następnie wyznacza i wypisuje sumę 10 największych elementów
z tablicy
"""
from random import randint

tab = [randint(1, 5000) for _ in range(1000)]

t = [0]*10

for x in tab:
    temp = x
    for i in range(len(t)):
        if temp > t[i]:
            temp_1 = t[i]
            t[i] = temp
            temp = temp_1

suma = 0
for x in t:
    suma += x

print(t)
print(suma)