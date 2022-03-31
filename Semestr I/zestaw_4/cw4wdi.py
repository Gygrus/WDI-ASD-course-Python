"""
Dana jest tablica int t[MAX][MAX] wypełniona liczbami naturalnymi. Proszę napisać
funkcję która zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz
sumy elementów w kolumnie w którym leży element do sumy elementów wiersza w
którym leży element jest największa.
"""
from random import randint

def f(t):
    n = len(t)
    pom_k = 0
    pom_w = 10**100

    for x in range(n):
        sw = sk = 0
        for y in range(n):
            sw += t[x][y]
            sk += t[y][x]
        if pom_w > sw:
            pom_w = sw
            w = x
        if pom_k < sk:
            pom_k = sk
            k = x


    return w, k

t = [[randint(1, 9) for _ in range(4)] for i in range(4)]
for n in t:
    print(n)
print(f(t))