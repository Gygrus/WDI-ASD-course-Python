"""
Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
110100 nie jest możliwe.
"""
from random import randint
from math import sqrt

def czy_pierwsza(n):
    new = 0
    k = len(n) - 1
    for x in n:
        if x == 1:
            new += 2**k
            k -= 1
        else:
            k -= 1

    if new <= 1:
        return False

    for k in range(2, int(sqrt(new)) + 1):
        if new % k == 0:
            return False

    return True

def czy_istnieje(T):
    if T == 0:
        return False

    if czy_pierwsza(T):
        return True

    for x in range(1, len(str(T)) + 1):
        p = T[:x]
        if len(p) <= 30 and czy_pierwsza(p):
            if czy_istnieje(T[x:]):
                return True

def transform(T):
    return czy_istnieje(T)
T = [randint(0, 1) for _ in range(10)]
print(T)


print(transform(T))