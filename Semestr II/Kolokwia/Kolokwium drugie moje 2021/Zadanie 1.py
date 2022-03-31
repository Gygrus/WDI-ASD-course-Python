#Piotr Socała
"""
Szablon rozwiązania: zad1.py
Inwestor planuje wybudować nowe osiedle akademików. Architekci przedstawili projekty budynków, z których inwestor musi wybrać podzbiór spełniając jego oczekiwania. Każdy budynek
reprezentowany jest jako prostokąt o pewnej wysokości h, podstawie od punktu a do punktu b,
oraz cenie budowy w (gdzie h, a, b i w to liczby naturalne, przy czym a < b). W takim budynku
może mieszkać h ⋅ (b − a) studentów.
Proszę zaimplementować funkcję:
def select_buildings(T, p):
...
która przyjmuje:
• Tablicę T zawierająca opisy n budynków. Każdy opis to krotka postaci (h, a, b, w), zgodnie
z oznaczeniami wprowadzonymi powyżej.
• Liczbę naturalną p określającą limit łącznej ceny wybudowania budynków.
Funkcja powinna zwrócić tablicę z numerami budynków (zgodnie z kolejnością w T, numerowanych
od 0), które nie zachodzą na siebie, kosztują łącznie mniej niż p i mieszczą maksymalną liczbę
studentów. Jeśli więcej niż jeden zbiór budynków spełnia warunki zadania, funkcja powinna zwrócić
zbiór o najmniejszym łącznym koszcie budowy. Dwa budynki nie zachodzą na siebie, jeśli nie mają
punktu wspólnego.
Można założyć, że zawsze istnieje rozwiązanie zawierające co najmniej jeden budynek. Funkcja
powinna być możliwie jak najszybsza i zużywać jak najmniej
"""

"""
Najpierw sortuję tablicę T rosnąco po pierwszej współrzędnej a
Definiuję funkcję f(i, j) - maksymalna ilość pojemności budynków rozważanych do i-tego o koszcie mniejszym niż j
oraz ostatnia współrzędna budynku znajdującego się najbardziej "z prawej"
f(i, j) = [f(i-1, j)[0], f(i-1,j)[1]] jeśli a_i <= f(i-1, j)[1] lub (a_i > f(i-1, j)[1] i f(i-1, j-w_i) + h_i*(b_i-a_i) < f(i-1, j)[0])
f(i, j) = [f(i-1, j-w_i) + h_i*(b_i-a_j), b_i] jeśli a_i > f(i-1, j)[1] i (a_i > f(i-1, j)[1] i f(i-1, j-w_i) + h_i*(b_i-a_i)
f(i, 0) = [0, 0]
"""

def select_buildings(T, p):
    def get_value(x):
        return (x[2]-x[1])*x[0]

    def quicksort(Tab, p, r, copy):
        def quicksort1(Tab, p, r, copy):
            while p < r:
                q = partition(Tab, p, r, copy)
                quicksort1(Tab, p, q - 1, copy)
                p = q + 1

        def partition(Tab, p, r, copy):
            x = Tab[r][1]
            i = p - 1
            for j in range(p, r):
                if Tab[j][1] < x:
                    i += 1
                    Tab[i], Tab[j] = Tab[j], Tab[i]
                    copy[i], copy[j] = copy[j], copy[i]
            Tab[i + 1], Tab[r] = Tab[r], Tab[i + 1]
            copy[i + 1], copy[r] = copy[r], copy[i + 1]
            return i + 1

        quicksort1(Tab, p, r, copy)


    n = len(T)
    copy_of_T = list(range(n))

    quicksort(T, 0, n-1, copy_of_T)
    F = [[[0, 0, []] for _ in range(p+1)] for _ in range(n)]
    for x in range(T[0][3], p+1):
        F[0][x] = [get_value(T[0]), T[0][2], [copy_of_T[0]]]

    for i in range(1, n):
        for j in range(p+1):
            F[i][j] = F[i-1][j]
            if T[i][3] <= j:
                if T[i][1] > F[i-1][j-T[i][3]][1] and F[i-1][j-T[i][3]][0] + get_value(T[i]) > F[i][j][0]:
                    F[i][j] = [F[i-1][j-T[i][3]][0] + get_value(T[i]), T[i][2], F[i-1][j-T[i][3]][2] + [copy_of_T[i]]]
                if T[i][1] <= F[i-1][j-T[i][3]][1] and get_value((T[i])) > F[i][j][0]:
                    F[i][j] = [get_value(T[i]), T[i][2], F[i-1][j-T[i][3]][2] + [copy_of_T[i]]]

    rem = F[n-1][p][0]
    idx = n-1
    for x in range(p, -1, -1):
        if F[n-1][x][0] < rem:
            idx = x+1
            break

    return sorted(F[n-1][idx][2])








T = [(8, 2, 6, 2), (9, 4, 8, 5), (9, 8, 9, 2), (3, 10, 15, 1)]
# T = [(2, 1, 5, 3),
#     (3, 7, 9, 2),
# (2, 8, 11, 1) ]
p = 7
# p = 5
print(select_buildings(T, p))