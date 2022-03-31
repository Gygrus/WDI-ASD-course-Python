"""Piotr Socała"""
"""
Dana jest dwuwymiarowa tablica T o rozmiarach N × N wypełniona liczbami naturalnymi (liczby
są parami różne). Proszę zaimplementować funkcję Median(T), która przekształca tablicę T, tak
aby elementy leżące pod główną przekątną nie były większe od elementów na głównej przekątnej,
a elementy leżące nad główną przekątną nie były mniejsze od elementów na głównej przekątnej.
Algorytm powinien być jak najszybszy oraz używać jak najmniej pamięci ponad tę, która potrzebna
jest na przechowywanie danych wejściowych (choć algorytm nie musi działać w miejscu). Proszę
podać złożoność czasową i pamięciową zaproponowanego algorytmu.
"""

"""
Przekształcę tablicę dwuwymiarową T na tablicę jednowymiarową, po czym za pomocą dwóch wywołań funkcji
Select() (działającej w czasie liniowym), podzielę elementy w tablicy jednowymiarowej na mniejsze od
n "środkowych" (będących na głównej przekątnej), n środkowych elementów i resztę elementów większych od 
przekątnej. Następnie przepiszę elementy do tablicy dwuwymiarowej T w odpowiedniej kolejności."""
"""
Złożoność:
złożoność select: O(n) (dla n wartości, tutaj mamy n^2 wartości), czyli w tym przypadku O(n^2)
złożoność samej funkcji: przepisywanie wartości do tablicy pomocniczej: O(n^2), wpisywanie zmienionego
układu liczb do tablicy T: O(n^2)
Złożoność czasowa całości: O(n^2)
Złożoność pamięciowa: O(n^2)"""




def Median(T):
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
            return select(T, p, q - 1, k)

        else:
            return select(T, q + 1, r, k)

    n = len(T)
    new_tab = [0]*(n*n)
    i = 0
    for x in range(n):
        for y in range(n):
            new_tab[i] = T[x][y]
            i += 1

    #print(new_tab)
    middle = n*n//2
    if n%2 == 0:
        mid_right = middle + (n // 2) - 1
        right = select(new_tab, 0, n*n-1, middle+(n//2)-1)
        left = select(new_tab, 0, middle+n-2, middle-(n//2))
    else:
        mid_right = middle + (n // 2)
        right = select(new_tab, 0, n*n-1, middle+(n//2))
        left = select(new_tab, 0, middle+(n//2)-1, middle-(n//2))

    #print(new_tab)

    left = 0
    mid_left = middle-(n//2)
    mid_right += 1
    #print(left, mid_left, mid_right)
    for x in range(n):
        for y in range(n):
            if x > y:
                T[x][y] = new_tab[left]
                left += 1
            elif x < y:
                T[x][y] = new_tab[mid_right]
                mid_right += 1
            else:
                T[x][y] = new_tab[mid_left]
                mid_left += 1

    return T


T = [[43, 74, 53, 97],
[80, 61, 61, 19],
[61, 73, 89, 93],
[42, 17, 89, 80],]


Median(T)
for x in range(4):
    print(T[x])


