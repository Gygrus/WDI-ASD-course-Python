"""
Proszę napisać program, który wypełnia N-elementową tablicę t pseudolosowymi liczbami
nieparzystymi z zakresu [1..99], a następnie wyznacza i wypisuje różnicę pomiędzy długością najdłuższego
znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy, a długością najdłuższego ciągu
arytmetycznego o ujemnej różnicy, przy założeniu, że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych
indeksach.

"""
from random import randint
n = 50
#t = [randint(0, 49)*2 + 1 for x in range(n)]
t = [3, 0, 7, 9, 11, 5, -1, 3, -1, -7, -13, -19, -20]
print(t)

r_d = 0
r_u = 0
count_d = 1
count_u = 1
maximum_d = 0
maximum_u = 0
k = True
tab = [t[0]]
for x in t[1:]:
    if x > tab[-1]:
        count_d += 1
        if count_u > maximum_u and count_u > 1:
            maximum_u = count_u
        if x - tab[-1] != r_d or r_d == 0:
            count_d = 2
            r_d = x - tab[-1]

        r_u = 0
        count_u = 1
    elif x < tab[-1]:
        count_u += 1
        if count_d > maximum_d and count_d > 1:
            maximum_d = count_d
        if x - tab[-1] != r_u or r_u == 0:
            count_u = 2
            r_u = x - tab[-1]
        r_d = 0
        count_d = 1
    if count_d > maximum_d:
        maximum_d = count_d
    if count_u > maximum_u:
        maximum_u = count_u
    tab.append(x)
print("dodatnie", maximum_d)
print("ujemne", maximum_u)
print(maximum_d - maximum_u)
