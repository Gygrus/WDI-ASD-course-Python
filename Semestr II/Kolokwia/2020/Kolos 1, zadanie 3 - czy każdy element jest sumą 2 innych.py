"""
Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy każda liczba z tablicy jest sumą dwóch innych liczb z tablicy. Zaproponowany
algorytm powinien być możliwie jak najszybszy. Proszę oszacować jego złożoność obliczeniową.
"""


"""
Najpierw posortuję tablicę funkcją quicksort() (czas nlog(n)), następnie liniowo sprawdzę czy każda liczba ma swoją sumę
złożoną z dwóch innych ustawiając dwa pomocnicze wskaźniki, jeden na początek, drugi na koniec tablicy. Jeśli suma elementów
o indeksach będących wskaźnikami jest większa niż żądana liczba, wtedy wksaźnik z końca tablicy zmniejszam o jeden i dalej sprawdzam,
jeśli jest inaczej, zwiększam wskaźnik "mniejszy".
Złożoność: quicksort zajmuje nlog(n) czasu, a przejście po wszystkich elementach tablicy i sprawdzenie sumy zajmie n*n czasu,
więc skoro n^2 > nlog(n), złożoność = O(n^2)"""

from random import randint, shuffle



def quicksort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        quicksort(T, p, q-1)
        p = q+1

def partition(T, p, r):

    x = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] < x:
            i += 1
            T[j], T[i] = T[i], T[j]

    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def check_sum_tab(T):
    n = len(T)
    if n < 3:
        return False

    quicksort(T, 0, n-1)
    for x in range(n):
        i = 0
        j = n-1
        check = False
        while i < j:
            if i != x and j != x:
                sum = T[i] + T[j]
                if sum > T[x]:
                    j -= 1
                elif sum < T[x]:
                    i += 1
                else:
                    check = True
                    break

            else:
                if i == x:
                    i += 1
                else:
                    j -= 1

        if not check:
            return False

    return True

T = [-4, -3, -3, -2, -1, 0, 1, 3, 2, 5, 8, 4]
print(T)
shuffle(T)
print(T)
print(check_sum_tab(T))
print(T)
