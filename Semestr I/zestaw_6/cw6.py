"""
Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów.
Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.
"""


def search_for_set(T, x, sum_of_index, sum_of_el, i, smallest, settt):
    settt = settt[:]
    settt.append(T[x])
    sum_of_el += T[x]
    sum_of_index += x
    if sum_of_el == sum_of_index:
        if i < smallest:
            smallest = sum_of_index
            return smallest

    for p in range(x + 1, len(T)):
        if search_for_set(T, p, sum_of_index, sum_of_el, i+1, smallest, settt) < smallest:
            smallest = search_for_set(T, p, sum_of_index, sum_of_el, i+1, smallest, settt)


    return smallest


def rekur(T):
    smallest = 10*10
    settt = list()
    for k in range(len(T)):
        if search_for_set(T, k, 0, 0, 1, smallest, settt) < smallest:
            smallest = search_for_set(T, k, 0, 0, 1, smallest, settt)

    return smallest




print(rekur([ 1,7,3,5,11,2, 5, 3, 1, 3, 5, 7, 1435, 3, 14, 42, 553 ]))