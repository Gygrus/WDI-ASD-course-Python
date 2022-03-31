"""
Napisać funkcję: void sortString(string A[]); Funkcja sortuje tablicę n stringów różnej
długości. Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego.
"""


"""
Użyję algorytmu radixsort, który sortuje kolejne znaki (zaczynając od końca, czyli "najmniej ważnych" znaków) za pomocą
countsorta, jeśli dwa stringi nie mają równej długości, to gdy badam znak i-ty, gdzie i > długość stringa krótszego, 
to traktuje jakby na tym indeksie dany string miał najmniejszą możliwą wartość (0)."""
"""
Złożoność: jeśli k to długość najdłuższego stringa, a countsort działa w czasie liniowym n, to złożoność wynosi
O(n*k) (czyli złożoność liniowa)"""
import random
import string
import time


def radixsort(T, n, tab_len, tab_of_occur, biggest):
    pom_T = [0]*n
    pom_len = [0]*n
    for i in range(biggest, 0, -1):
        for x in range(n):
            if tab_len[x] >= i:
                tab_of_occur[ord(T[x][i-1]) - 97] += 1
            else:
                tab_of_occur[0] += 1
        for x in range(1, 26):
            tab_of_occur[x] += tab_of_occur[x-1]

        for x in range(n-1, -1, -1):
            if tab_len[x] >= i:
                tab_of_occur[ord(T[x][i-1]) - 97] -= 1
                pom_T[tab_of_occur[ord(T[x][i-1]) - 97]] = T[x]
                pom_len[tab_of_occur[ord(T[x][i-1]) - 97]] = tab_len[x]
            else:
                tab_of_occur[0] -= 1
                pom_T[tab_of_occur[0]] = T[x]
                pom_len[tab_of_occur[0]] = tab_len[x]

        for x in range(26):
            tab_of_occur[x] = 0

        for x in range(n):
            T[x] = pom_T[x]
            tab_len[x] = pom_len[x]




def sortString(T):
    n = len(T)
    tab_len = [0]*n
    biggest = 0
    for x in range(n):
        k = len(T[x])
        tab_len[x] = k
        if k > biggest:
            biggest = k

    tab_of_occur = [0]*(122-96)

    radixsort(T, n, tab_len, tab_of_occur, biggest)


A = [''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 150))) for _ in range(100000)]

print(A)
start = time.time()
sortString(A)
end = time.time()
print(A)
print(end-start)