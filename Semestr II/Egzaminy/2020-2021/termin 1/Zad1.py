# Piotr Socała
"""
Mówimy, że tablica T ma współczynnik nieuporządkowania równy k (jest k-Chaotyczna), jeśli spełnione są łącznie dwa warunki:
1. tablicę można posortować niemalejąco przenosząc każdy element A[i] o co najwyżej k pozycji
(po posortowaniu znajduje się on na pozycji różniącej się od i co najwyżej o k),
2. tablicy nie da się posortować niemalejąco przenosząc każdy element o mniej niż k pozycji.
Proszę zaproponować i zaimplementować algorytm, który otrzymuje na wejściu tablicę liczb rzeczywistych T i zwraca jej współczynnik nieuporządkowania. Algorytm powinien być jak najszybszy
oraz używać jak najmniej pamięci. Proszę uzasadnić jego poprawność i oszacować złożoność obliczeniową. Algorytm należy zaimplementować jako funkcję:
def chaos_index( T ):
...
przyjmującą tablicę T i zwracającą liczbę całkowitą będącą wyznaczonym współczynnikiem nieuporządkowania.
"""

"""
Posortuję tablicę niemalejąco, zapamiętując indeks oryginalny każdej liczby, a następnie zwrócę maksymalną wartość bezwzględną
różnicy indeksów poszczególnych elementów"""

def chaos_index(T):
    n = len(T)
    new_tab = [[0, 0] for _ in range(n)]
    for x in range(n):
        new_tab[x] = [T[x], x]

    def quicksort1(Tab, p, r):
        def quicksort(Tab, p, r):
            while p < r:
                q = partition(Tab, p, r)
                quicksort(Tab, p, q - 1)
                p = q + 1

        def partition(Tab, p, r):
            x = Tab[r][0]
            i = p - 1
            for j in range(p, r):
                if Tab[j][0] <= x:
                    i += 1
                    Tab[i], Tab[j] = Tab[j], Tab[i]
            Tab[i + 1], Tab[r] = Tab[r], Tab[i + 1]
            return i + 1

        quicksort(Tab, p, r)

    quicksort1(new_tab, 0, n-1)
    k = 0
    for x in range(n):
        if abs(new_tab[x][1] - x) > k:
            k = abs(new_tab[x][1] - x)

    return k


T = [0, 2, 1.1, 2]
print(chaos_index(T))