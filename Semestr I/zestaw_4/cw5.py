"""
Poprzednie zadanie z tablicą wypełnioną liczbami całkowitymi.
"""


def cw4(t):
    sum_of_lines = [0]*len(t)
    sum_of_columns = [0]*len(t[0])
    i = 0
    while i != len(t):
        sum_of_lines[i] = sum(t[i])
        k = 0
        new = [0]*len(t[0])
        for x in t:                           #iteruje po kolejnych i-tych indeksach poszczególnych wierszy, żeby zyskać ich wartości do nowej zmiennej
            new[k] = x[i]
            k += 1
        sum_of_columns[i] = sum(new)          #dodaje do zmiennej przechowującej sumy kolumn sumę wszystkich i-tych elementów
        i += 1
    i = 0
    maximum = 0
    result = None
    new = None
    while i < len(t):
        k = 0
        while k < len(t[i]):
            if sum_of_lines[i] != 0 and sum_of_columns[k] / sum_of_lines[i] > maximum:
                result = i + 1, k + 1                            #wypisuje indeksy zwiększone o 1, żeby zyskać numer wiersza i kolumny
                new = t[i][k]
                maximum = sum_of_columns[k] / sum_of_lines[i]
            k += 1
        i += 1

    return result, new, maximum


print(cw4([[3, 65, -3, -65],
           [66, 49, -49, -66],
           [-60, -1, -6, 60],
           [47, 89, -89, -47]]))