"""Proszę zaimplementować funkcję void SumSort(int A[], int B[], int n). Funkcja ta
przyjmuje na wejściu dwie n
2
-elementowe tablice (A i B) i zapisuje w tablicy B taką permutację
elementów z A, że:
nX−1
i=0
B[i] ¬
2
Xn−1
i=n
B[i] ¬ ... ¬
nX2−1
i=n2−n
B[i].
Proszę zaimplementować funkcję SumSort tak, by działała możliwie jak najszybciej. Proszę
oszacować i podać jej złożoność czasową."""

"""
Za pomoca funkcji select(), która w czasie liniowym znajduje (i umieszcza na odpowiednim miejscu, dzieląc tablicę
na elementy o wartości mniejszej od elem na indeksie k i na większe od elem na indeksie k) element,
który po posortowaniu znajdowałby się na pozycji k-tej, umieszczę na indeksach n-1, 2n-1, 3n-1, ..., n^2-n-1,
dzieląc tablicę na (niekoniecznie posortowane) przedziały o odpowiednio rosnących sumach. Następnie przepiszę tablicę A do tablicy B.
Złożoność obliczeniowa: n-1 razy wywołuję select, który działa w czasie liniowym n^2, na koniec przepisuję elementy do drugiej tablicy
, co daje n operacji, więc złożoność wynosi O((n-1)*n^2 + n) = O(n^3) 
"""
"""
Pomysł drugi: bierzemy n sum kolejnych wyrazów i te sumy permutujemy niemalejąco, pamiętając o ich przedziałach.
Złożoność: O(n^2)"""
from random import randint
from time import time

def select(T, p, r, k):
    if p == r:
        return T[p]

    q = partition(T, p, r)

    if q == k:
        return T[k]
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
            T[j], T[i] = T[i], T[j]

    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def SumSort(A, B, n):
    length = n*n-1
    for x in range(1, n):
        #print((x-1)*n, length, x*n-1)
        select(A, (x-1)*n, length, x*n-1)
        #print(A)

    for x in range(length+1):
        B[x] = A[x]

def partition2(T, p, r):
    x = T[r][1]
    i = p-1
    for j in range(p, r):
        if T[j][1] < x:
            i += 1
            T[j], T[i] = T[i], T[j]

    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def quicksort(T, p, r):
    while p < r:
        q = partition2(T, p, r)
        quicksort(T, p, q-1)
        p = q+1


def SumSort_2(A, B, n):
    C = [[0, 0] for _ in range(n)]
    for x in range(n):
        C[x][0] = x
        for i in range(x*n, x*n+n):
            C[x][1] += A[i]

    quicksort(C, 0, n-1)
    # print("A: ", A)
    # print("C: ", C)
    # print("B: ", B)
    i = 0
    for x in range(n):
        for i in range(C[x][0]*n, C[x][0]*n+n):
            B[x*n + i%n] = A[i]

    return B






n = 3
A_1 = [randint(1, 1000) for _ in range(n*n)]
A_2 = A_1[::]
B_1 = [0]*(n*n)
B_2 = [0]*(n*n)
start_1 = time()
SumSort_2(A_1, B_1, n)
stop_1 = time()
print(B_1)
print(stop_1 - start_1, "Czas O(n^2)")
# start_2 = time()
# SumSort(A_2, B_2, n)
# stop_2 = time()
# start_1 = time()
# SumSort_2(A_1, B_1, n)
# stop_1 = time()
#print(A_1)
#print(B_2)

#print(stop_1 - start_1, "Czas O(n^2)")
#print(stop_2 - start_2, "Czas O(n^3)")

