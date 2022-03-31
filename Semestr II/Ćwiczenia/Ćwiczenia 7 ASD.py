"Zadanie 2: Przedziały jednostkowe"


def partition(tab, p, r):
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def qs_iter(tab):
    stack = []
    stack.append((0, len(tab) - 1))
    while len(stack) > 0:
        p, r = stack.pop()
        if p < r:
            q = partition(tab, p, r)
            stack.append((p, q - 1))
            stack.append((q + 1, r))


def do_the_magic(T):
    n = len(T)
    output = []
    qs_iter(T)

    i = 0
    while i < n:
        start = T[i]
        i += 1
        stop = start + 1

        while i < n and T[i] <= stop:
            i += 1

        output.append((start, stop))

    return output


# T = [0.5, 0.25, 1.6]
# print(do_the_magic(T))


"""Zadanie 3: z przedziałami"""


# krotki (profit, deadline)
def maxProfit(P, times):
    sorted(P, key=lambda tuple: tuple[0], reverse=True)
    T = [-1 for i in range(times)]
    for profit, deadline in P:
        tmp = deadline
        while T[tmp] != -1 and tmp >= 0:
            tmp -= 1
        if tmp != -1:
            T[tmp] = profit

    res = 0
    for i in T:
        if i != -1:
            res += i

    return res


# P=[8,7,5,4,4]
# D=[1,2,4,5,3]


# P = [(8, 1), (7, 2), (5, 4), (4, 5), (4, 3)]
# times = 8
#
# print(maxProfit(P, times))


"""
(pokrycie przedziałami jednostkowymi) Dany jest zbiór punktów X = {x1, . . . , xn} na
prostej. Proszę podać algorytm, który znajduje minimalną liczbę przedziałów jednostkowych domkniętych,
potrzebnych do pokrycia wszystkich punktów z X. (Przykład: Jeśli X = {0.25, 0.5, 1.6} to potrzeba dwóch
przedziałów, np. [0.2, 1.2] oraz [1.4, 2.4]).
"""

def check_if_possible(X):
    def quicksort1(Tab, p, r):
        def quicksort(Tab, p, r):
            while p < r:
                q = partition(Tab, p, r)
                quicksort(Tab, p, q - 1)
                p = q + 1

        def partition(Tab, p, r):
            x = Tab[r]
            i = p - 1
            for j in range(p, r):
                if Tab[j] < x:
                    i += 1
                    Tab[i], Tab[j] = Tab[j], Tab[i]
            Tab[i + 1], Tab[r] = Tab[r], Tab[i + 1]
            return i + 1

        quicksort(Tab, p, r)

    n = len(X)
    quicksort1(X, 0, n-1)
    output = []
    start = X[0]
    end = X[0] + 1
    for i in range(1, n):
        if X[i] > end:
            output.append((start, end))
            start = X[i]
            end = start + 1

    output.append((start, end))
    return output

# T = [0.5, 0.25, 1.6]
# print(check_if_possible(T))


"""
Zadanie 2. (wybór zadań z terminami) Mamy dany zbiór zadań T = {t1, . . . , tn}. Każde zadanie ti
dodatkowo posiada: (a) termin wykonania d(ti) (liczba naturalna) oraz (b) zysk g(ti) za wykonanie w
terminie (liczba naturalna). Wykonanie każdego zadania trwa jednostkę czasu. Jeśli zadanie ti zostanie
wykonane przed przekroczeniem swojego terminu d(ti), to dostajemy za nie nagrodę g(ti) (pierwsze wybrane
zadanie jest wykonywane w chwili 0, drugie wybrane zadanie w chwili 1, trzecie w chwili 2, itd.).
Proszę podać algorytm, który znajduje podzbiór zadań, które można wykonać w terminie i który prowadzi
do maksymalnego zysku. Proszę uzasadnić poprawność algorytmu.
"""

def task_order(T, d, g):
    def quicksort1(Tab, p, r, d, q):
        def quicksort(Tab, p, r, d, q):
            while p < r:
                q = partition(Tab, p, r, d, q)
                quicksort(Tab, p, q - 1, d, q)
                p = q + 1

        def partition(Tab, p, r, d, q):
            x = g[r]
            i = p - 1
            for j in range(p, r):
                if g[j] > x:
                    i += 1
                    Tab[i], Tab[j] = Tab[j], Tab[i]
                    d[i], d[j] = d[j], d[i]
                    g[i], g[j] = g[j], g[i]
            Tab[i + 1], Tab[r] = Tab[r], Tab[i + 1]
            d[i + 1], d[r] = d[r], d[i + 1]
            g[i + 1], g[r] = g[r], g[i + 1]
            return i + 1

        quicksort(Tab, p, r, d, g)

    n = len(T)
    quicksort1(T, 0, n-1, d, g)
    print(g)
    print(d)
    output = [-1]*n
    for x in range(n):
        d_x = d[x]
        for i in range(d_x, -1, -1):
            if i < n and output[i] == -1:
                output[i] = T[x]
                break

    return output


T = [0, 1, 2, 3, 4, 5, 6]
d = [3, 6, 3, 2, 5, 4, 3]
g = [7, 4, 10, 2, 3, 5, 2]
print(task_order(T, d, g))