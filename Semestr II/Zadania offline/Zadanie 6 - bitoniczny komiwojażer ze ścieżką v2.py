from math import inf
from math import *

C = [['s', 9, 24], ['e', 11, 2], ['y', -5, 26], ['a', 28, -17], ['i', 23, 11], ['W', -24, -24], ['h', 29, 24],
     ['*', -25, 27], ['U', 22, -16], ['b', 5, 2], ['j', 15, -25], ['s', 24, -10], ['i', -9, 9], ['k', 18, 4],
     ['e', -19, 10], ['t', 16, -3], ['W', 30, 10], ['c', 26, 11], ['s', -20, -17], ['z', -17, 27]]
"""Główną ideą tego pomysłu jest odtwarzanie rozwiązania na podstawie tablicy pomocniczej o długości n (gdzie
n jest rozmiarem tablicy C), która będzie przechowywać informację, czy i-te miasto należy do ścieżki "w prawo",
czy "w lewo". Wypełnienie tej tablicy pozwoli funkcja get_solution."""

def bitonicTSP(C):
    # quicksort do posortowania elementów tablicy C
    # po współrzędnej x-owej
    def q_sort(Tab, p, r):
        def quicksort(Tab, p, r):
            while p < r:
                q = partition(Tab, p, r)
                quicksort(Tab, p, q - 1)
                p = q + 1

        def partition(Tab, p, r):
            x = Tab[r][1]
            i = p - 1
            for j in range(p, r):
                if Tab[j][1] < x:
                    i += 1
                    Tab[i], Tab[j] = Tab[j], Tab[i]
            Tab[i + 1], Tab[r] = Tab[r], Tab[i + 1]
            return i + 1

        quicksort(Tab, p, r)

    # funkcja zwracająca odległość między dwoma miastami
    def get_distance(first, second):
        return (abs(first[1] - second[1])**2 + abs(first[2] - second[2])**2)**(1/2)

    # funkcja zwracająca najkrótszą długość drogi zawierającej
    # wszystkie miasta do j włącznie, gdzie ścieżka "w lewo"
    # kończy się na mieście i-tym, a ścieżka "w prawo"
    # kończy się na mieście j-tym. Funkcja jak z wykładu
    def tspf(i, j, F, D):
        if F[i][j] != inf:
            return F[i][j]

        if i == j - 1:
            best = inf
            for k in range(j - 1):
                best = min(best, tspf(k, j - 1, F, D) + D[k][j])

            F[j - 1][j] = best

        else:
            F[i][j] = tspf(i, j - 1, F, D) + D[j - 1][j]

        return F[i][j]

    # funkcja wypełniająca tablicę pomocniczą tab
    def get_solution(i, j, F, C, tab):
        # warunek końcowy
        if j == 0:
            return

        # jeśli i < j-1 wystarczy oznaczyć miasto j-te
        # jako miasto należące do ścieżki "w prawo" (wiemy
        # to na pewno z definicji funkcji F) i wywołać
        # get_solution dla indeksu j o jeden mniejszego. Tak naprawdę
        # wszystkie miasta od i+1 do j włącznie muszą należeć
        # do ścieżki w prawo
        if i < j-1:
            tab[j] = 1
            get_solution(i, j-1, F, C, tab)

        # w przypadku kiedy i = j-1, zapisujemy miasto j-te
        # do ścieżki "w prawo", a następnie musimy znaleźć takie
        # k, że F[k][j-1] + D[k][j] jest najmniejsze (to samo
        # robi funkcja tspf, tutaj de facto odtwarzamy jej działanie).
        # Wszystkie miasta od znalezionego k+1-tego do i-tego włącznie
        # należą do ścieżki "w lewo". Następnie znów szukamy i takiego,
        # że F[i][k] + D[i][k+1] jest najmniejsze (czyli również
        # odtwarzamy działanie tspf), to da nam kolejne
        # indeksy i oraz j dla których odległość ścieżki będzie optymalna
        # i możemy na tych indeksach wywołać get_solution
        else:
            tab[j] = 1
            best = inf
            save_k = 0
            for k in range(j-1):
                new = F[k][j-1] + D[k][j]
                if new < best:
                    best = new
                    save_k = k

            for x in range(save_k+1, i+1):
                tab[x] = -1

            best = inf
            save_i = 0
            for i in range(save_k):
                new = F[i][save_k] + D[i][save_k+1]
                if new < best:
                    best = new
                    save_i = i

            get_solution(save_i, save_k, F, C, tab)

    # rozmiar tablicy C
    n = len(C)
    # posortowanie C po współrzędnej x
    q_sort(C, 0, n-1)
    # zadeklarowanie i wypełnienie tablicy odległości
    D = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            D[x][y] = get_distance(C[x], C[y])

    # zadeklarowanie tablicy funkcji f i wypełnienie
    # przypadku brzegowego
    F = [[inf for _ in range(n)]  for _ in range(n)]
    F[0][1] = D[0][1]

    # deklaracja tablicy pomocniczej (1 oznacza
    # ścieżkę "w prawo", -1 "w lewo"
    tab = [0 for _ in range(n)]
    tab[1] = 1
    minimal = inf
    save_i = 0

    # znajdywanie optymalnej ścieżki i indeksu i,
    # potrzebnego potem do wywołania get_solution
    for x in range(n-1):
        a = tspf(x, n-1, F, D)
        if a + D[x][n-1]< minimal:
            save_i = x
            minimal = a+D[x][n-1]

    # wypełnianie tablicy tab za pomocą get_solution
    get_solution(save_i, n-1, F, D, tab)

    # wypisanie rozwiązania
    print(minimal)
    print(C[0][0], end=", ")
    for x in range(1, n):
        if tab[x] == 1:
            print(C[x][0], end=", ")

    for x in range(n-1, 0, -1):
        if tab[x] == -1:
            print(C[x][0], end=", ")

    print(C[0][0])

bitonicTSP(C)
