"""Znajduje element, który znajdowałby się pod indeksem k gdyby tablica była posortowana"""
from random import randint
# p, r => zamknięty przedział (r to ostatni indeks)

def partition(Tab, p, r):
    x = Tab[r]
    i = p - 1
    for j in range(p, r):
        if Tab[j] < x:
            i += 1
            Tab[i], Tab[j] = Tab[j], Tab[i]

    Tab[i + 1], Tab[r] = Tab[r], Tab[i + 1]
    return i + 1


def select(T, p, r, k):
    if p == r:
        return T[p]

    q = partition(T, p, r)

    if q == k:
        return T[q]

    elif q > k:
        return select(T, p, q-1, k)

    else:
        return select(T, q+1, r, k)


T = [randint(-10, 10) for _ in range(15)]
print(T)
q = select(T, 0, len(T)-1, 4)
print(q)
print(T)
