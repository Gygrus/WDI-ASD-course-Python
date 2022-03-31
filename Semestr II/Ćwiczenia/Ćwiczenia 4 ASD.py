"""Zadanie 1. Proszę zaproponować algorytm, który w czasie liniowym sortuje tablicę A zawierającą n liczb
ze zbioru 0, . . . , n2 − 1.
"""
from random import randint

k = 100   #zakres
n = 20    #rozmiar tablicy

A = [randint(0, k*k-1) for _ in range(n)]


def radixsort(T, k):
    T_len = len(T)
    C = [0 for i in range(n)]

    for i in range(T_len):
        C[T[i]%k] += 1
    for i in range(1, k):
        C[i] += C[i-1]

    B = [0 for _ in range(T_len)]
    for i in range(T_len-1, -1, -1):
        C[T[i]%k] -= 1
        B[C[T[i]%k]] = T[i]

    C = [0 for i in range(n)]

    for i in range(T_len):
        C[B[i] // k] += 1
    for i in range(1, k):
        C[i] += C[i - 1]

    for i in range(T_len - 1, -1, -1):
        C[T[i] // k] -= 1
        T[C[T[i] // k]] = B[i]


"""Dana jest tablica A o długości n. Wartości w tablicy pochodzą ze zbioru B, gdzie ∣B∣ = log n.
Proszę zaproponować możliwie jak najszybszy algorytm sortowania tablicy A.
"""

"""pomysł taki jaki miałem, ale na końcu jak mamy przepisywanie do tablicy, 
to bierzemy po kolei ilość wystąpień """

"""3. Proszę zaproponować algorytm, który mając dane dwa słowa A i B o długości n, każde nad
alfabetem długości k, sprawdza czy A i B są swoimi anagramami.
1. Proszę zaproponować rozwiązanie działające w czasie O(n + k).
2. Proszę zaproponować rozwiązanie działające w czasie O(n) (proszę zwrócić uwagę, że k może być dużo
większe od n—np. dla alfabetu unicode; złożoność pamięciowa może być rzędu O(n + k)).
Proszę zaimplementować oba algorytmy.
"""

