"""
Zadanie 2. Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
wzrostu. Proszę zaimplementować funkcję:
section(T,p,q)
która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową.
"""

"""Za pomocą dwóch wywołań funkcji select() z wykładu znajdę odpowiednio wzrosty dwóch żołnierzy znajdujących się
na pozycjach p i q. Następnie za pomocą algorytmu quicksort posortuje tablicę w tym zakresie i wpiszę wysokości w 
odwrotnej kolejności do tablicy wyjściowej. 
Szacowana złożoność obliczeniowa: O(2n + (q-p)log(q-p))"""

def partition(T, p, r):
    pivot = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] < pivot:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def quicksort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        if q-p < r-q:
            quicksort(T, p, q-1)
            p = q+1
        else:
            quicksort(T, q+1, r)
            r = q-1


def select(T, left, right, k):
    if left == right:
        return T[left]
    q = partition(T, left, right)

    if q == k:
        return T[q]

    elif q > k:
        return select(T, left, q-1, k)

    else:
        return select(T, q+1, right, k)




def section(T, p, q):
    n = len(T)
    left = select(T, 0, n-1, n-1-q)   # tutaj będę miał mniejszy wzrost
    right = select(T, n-1-q, n-1, n-1-p)    # tutaj będę miał większy wzrost
    print(left, right)
    quicksort(T, n-1-q, n-1-p)
    print(T)
    result = [0]*(q-p+1)
    i = 0
    for x in range(n-p-1, n-q-2, -1):
        result[i] = T[x]
        i += 1

    return result


T = [3, 9, 2, 6, 7, 5, 8, 1, 0, 4, 12, 46, 53, 22]

print(section(T, 5, 12))