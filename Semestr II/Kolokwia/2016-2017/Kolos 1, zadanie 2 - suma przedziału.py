"""
Proszę zaimplementować funkcję:
int SumBetween(int T[], int from, int to, int n);
Zadaniem tej funkcji jest obliczyć sumę liczb z n elementowej tablicy T, które w posortowanej
tablicy znajdywałyby się na pozycjach o indeksach od from do to (włącznie). Można przyjąć, że
liczby w tablicy T są parami różne (ale nie można przyjmować żadnego innego rozkładu danych).
Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę oszacować jej złożoność
czasową (oraz bardzo krótko uzasadnić to oszacowanie).
"""

"""
Za pomocą funkcji select() przemieszczę elementy, które po posortowaniu byłyby na indeksach from i to, na te właśnie indeksy,
następnie wyznaczę sumę elementów z przedziału from do to, iterując po indeksach z tego przedziału (elementy w nim zawarte, 
choć może nieposortowane, są niewiększe od elementu na indeksie "to" i niemniejsze od elementu na indeksie "from".
Złożoność select jest liniowa (w pesymistycznym przypadku n^2), a obliczenie sumy zajmuje (to-from), więc 
złożoność SumBetween będzie wynosiła O(2n + (to-from)) = O(n)
"""
from random import randint


def select(T, p, r, k):
    if p == r:
        return T[r]

    q = partition(T, p, r)

    if q == k:
        return T[q]
    elif q > k:
        return select(T, p, q-1, k)
    else:
        return select(T, q+1, r, k)

def partition(T, p, r):
    pivot = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] < pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def SumBetween(T, left, right, n):
    if left == right:
        return select(T, 0, n-1, left)

    select(T, 0, n-1, left)
    select(T, left+1, n-1, right)
    suma = 0
    for x in range(left, right+1):
        suma += T[x]
    return suma


# n = 20
# T = [randint(1, 20) for _ in range(n)]
# print(T)
# print(SumBetween(T, 5, 6, n))
# print(T)