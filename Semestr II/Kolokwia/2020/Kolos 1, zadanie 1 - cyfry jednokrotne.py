""""
 Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
pretty_sort(T)
która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową.
"""

"""
Rozwiązanie będzie polegało na zastosowaniu radixsort (najpierw sortując po "mniej ważnym" kryterium, czyli liczbach wielokrotnych,
a następnie po liczbach jednokrotnych, w obu przypadkach sortować będę countsortem (jest stabilny)). 
Odpowiednie ilości liczb wiel. i jedn. umieszczę w krotkach w tablicy pomocniczej długości tablicy T i sortuję po tych wartościach
na dwóch pozycjach.
Złożoność: (przy założeniu że przypisanie danej liczbie odpowiedniej krotki zajmuje czas c, a countsort zajmuje czas liniowy
z współczynnikiem b) O(n*c +2(b*n)) = O((c+2b)n) = O(n) 
"""

from random import randint
from time import time

def get_values(num, tab_of_nums):
    for x in range(10):
        tab_of_nums[x] = 0

    x = num
    while x != 0:
        y = x%10
        x //= 10
        tab_of_nums[y] += 1

    single = multiple = 0
    for x in range(10):
        if tab_of_nums[x] == 1:
            single += 1
        elif tab_of_nums[x] > 1:
            multiple += 1

    return (single, multiple)

# print(get_values(455, [0]*10))
# print(get_values(2344, [0]*10))
# print(get_values(67333, [0]*10))

def countsort(T, tab_pom, n):
    C = [0]*10
    B = [0]*n
    B_numbers = [0]*n

    for x in range(n):
        C[tab_pom[x][1]] += 1

    for x in range(1, 10):
        C[x] += C[x-1]

    for x in range(n-1, -1, -1):
        C[tab_pom[x][1]] -= 1
        B[C[tab_pom[x][1]]] = tab_pom[x]
        B_numbers[C[tab_pom[x][1]]] = T[x]

    C = [0] * 10

    for x in range(n):
        C[9 - B[x][0]] += 1

    for x in range(1, 10):
        C[x] += C[x-1]

    for x in range(n-1, -1, -1):
        C[9 -B[x][0]] -= 1
        T[C[9 -B[x][0]]] = B_numbers[x]


def RadixSort(T):
    n = len(T)
    tab_pom = [0]*n
    tab_of_nums = [0]*10
    for x in range(n):
        tab_pom[x] = get_values(T[x], tab_of_nums)

    countsort(T, tab_pom, n)


T = [randint(1, 1000000) for _ in range(1000000)]
print(T)
start = time()
RadixSort(T)
end = time()
print(T)
print(end - start)

