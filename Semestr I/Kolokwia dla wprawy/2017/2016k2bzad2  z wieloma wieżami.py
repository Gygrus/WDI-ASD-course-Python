"""
Dana jest tablica int t[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
W każdej kolumnie znajduje się dokładnie jedna wieża, której numer wiersza zawiera tablica
int w[N]. Proszę napisać funkcję która wybiera do usunięcia z szachownicy dwie wieże, tak aby
suma liczb na polach szachowanych przez pozostałe wieże była najmniejsza. Do funkcji należy
przekazać tablice t i w, funkcja powinna zwrócić numery kolumn z których usunięto wieże.
"""
from random import randint

def f(t, w):
    minimum = 100**10
    for x in range(len(w)):
        for y in range(x + 1, len(w)):
            print(x, y)
            sum_of_all = 0
            copy_t = [0]*len(t)
            for l in range(len(copy_t)):
                copy_t[l] = t[l][:]

            for p in range(len(copy_t)):                          #p to indeks kolumny, w[p] to indeks wiersza punktu w którym jest wieża
                if p != x and p != y:
                    for k in range(len(copy_t)):
                        if k != p:
                            sum_of_all += copy_t[w[p]][k]
                            copy_t[w[p]][k] = 0

                        if k != w[p]:
                            sum_of_all += copy_t[k][p]
                            copy_t[p][k] = 0

                    print(sum_of_all)
            if sum_of_all < minimum:
                print("brrbrbr", sum_of_all)
                minimum = sum_of_all
                result = (x, y)

    return result, minimum



w = [randint(0,9) for _ in range(10)]

t = [0]*10
for x in range(len(t)):
    t[x] = [randint(1, 10) for _ in range(10)]
    print(t[x])

print(f(t, w))




