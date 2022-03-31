"""
Asystent znanego profesora otrzymał polecenie wyliczenia sumy pewnego ciągu liczb (liczby mogą
być zarówno dodatnie jak i ujemne):
n1 + n2 + ... + nk
Aby zminimalizować błędy zaokrągleń asystent postanowił wykonać powyższe dodawania w takiej
kolejności, by największy co do wartości bezwzględnej wynik tymczasowy (wynik każdej operacji
dodawania; wartość końcowej sumy również traktujemy jak wynik tymczasowy) był możliwie jak
najmniejszy. Aby ułatwić sobie zadanie, asystent nie zmienia kolejności liczb w sumie a jedynie
wybiera kolejność dodawań.
Napisz funkcję opt sum, która przyjmuje tablicę liczb n1, n2, . . . , nk (w kolejności w jakiej występują w sumie; zakładamy, że tablica zwiera co najmniej dwie liczby) i zwraca największą wartość
bezwzględną wyniku tymczasowego w optymalnej kolejności dodawań. Na przykład dla tablicy
wejściowej:
[1,−5, 2]
funkcja powinna zwrócić wartość 3, co odpowiada dodaniu −5 i 2 a następnie dodaniu 1 do wyniku.
Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność obliczeniową. Nagłówek funkcji opt sum powinien mieć postać:
"""

def opt_sum(tab):
    n = len(tab)
    rem = None
    result = 0
    for x in range(n-1):
        print(tab)
        best = float('inf')
        rem = None
        for y in range(len(tab)-1):
            if abs(tab[y] + tab[y+1]) < best:
                best = abs(tab[y] + tab[y+1])
                best_original = tab[y] + tab[y+1]
                rem = [y, y+1]
        print(best, tab[rem[0]], tab[rem[1]])
        i = 0
        for y in range(len(tab)-1):
            if y == rem[0]:
                tab[y] = best_original
                i += 1
            else:
                temp = tab[i]
                tab[y] = temp
            i += 1

        if result < best:
            result = best

        tab.pop()

    return result

def sum_parts(tab, a, b):
    output = 0
    for x in range(a, b+1):
        output += tab[x]
    return output

def opt_sum_2(tab):
    n = len(tab)
    F = [[float('inf') for _ in range(n)] for _ in range(n)]
    for x in range(n-1):
        F[x][x+1] = abs(tab[x]+tab[x+1])
        F[x][x] = 0
    F[n-1][n-1] = 0

    for t in range(2, n):
        for i in range(n-t+1):
            for k in range(i, i+t):
                if i+t < n:
                    print(i, t, k)
                    F[i][i+t] = min(F[i][i+t], max(F[i][k], F[k+1][i+t], abs(sum_parts(tab, i, i+t))))
                # if temp < F[i][j]:
                #     F[i][j] = temp
                # print(F[i][j])

        for x in F:
            print(x)

    for x in F:
        print(x)

    return F[0][n-1]
# print(sum_parts(tab, 1, 2))
tab = [1, -5, 3, -1, -3, 5, -8, 3, 2, -7, 6, 3]
# print(sum_parts(tab, 0, 0))
print(opt_sum_2(tab))
# print(opt_sum(tab))