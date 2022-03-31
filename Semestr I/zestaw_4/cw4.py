"""
Dana jest tablica int t[MAX][MAX] wypełniona liczbami naturalnymi. Proszę napisać
funkcję która zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz
sumy elementów w kolumnie w którym leży element do sumy elementów wiersza w
którym leży element jest największa.
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
    print(sum_of_columns)
    print(sum_of_lines)
    i = 0
    maximum = 0
    while i < len(t):
        k = 0
        while k < len(t[i]):
            if sum_of_columns[k] / sum_of_lines[i] > maximum:
                result = i + 1, k + 1                            #wypisuje indeksy zwiększone o 1, żeby zyskać numer wiersza i kolumny
                new = t[i][k]
                maximum = sum_of_columns[k] / sum_of_lines[i]
            k += 1
        i += 1

    return result, new, maximum


print(cw4([[3, 65, 68, 47],
           [66, 49, 9, 90],
           [68, 54, 1, 60],
           [47, 89, 38, 3]]))