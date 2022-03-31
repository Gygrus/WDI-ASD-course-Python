"""
 Dana jest tablica int t[N][N] zawierająca liczby naturalne. Dokładnie w jednym z wierszy
tablicy znajduje się fragment ciągu Fibonacciego o długościwiększej niż2,a mniejszej niż N. Proszę
napisać funkcję, która odszuka ten fragment ciągu i zwróci numer wiersza w którym on się znajduje.
"""
from random import randint

def check_if_fib(n):
    a = 1
    b = 1
    while a <= n:
        if a == n:
            return True

        c = a
        a += b
        b = c

    return False



def search_for_fib(t):
    for x in range(len(t)):
        for y in range(len(t)-2):
            if t[x][y] < t[x][y+1] and check_if_fib(t[x][y]) and check_if_fib(t[x][y + 1]) and check_if_fib(t[x][y + 2]) and t[x][y] + t[x][y + 1] == t[x][y + 2]:
                return x

t = [[randint(1, 13) for _ in range(20)] for _ in range(20)]
for x in t:
    print(x)
print(search_for_fib(t))