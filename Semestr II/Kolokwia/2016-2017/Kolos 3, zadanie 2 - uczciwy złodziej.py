"""
Złodziej widzi na wystawie po kolei n przedmiotów o wartościach A[0], A[1], ..., A[n − 1]. Złodziej
chce wybrać przedmioty o jak największej wartości, ale resztki przyzwoitości zabraniają mu
ukraść dwa przedmioty leżące obok siebie. Proszę zaimplementować funkcję:
int goodThief( int A[], int n );
która zwraca maksymalną wartość przedmiotów, które złodziej może ukraść zgodnie ze swoim
kodeksem moralnym oraz wypisuje numery przemiotów które powinien wybrać. Proszę uzasadnić
poprawność algorytmu oraz oszacować jego złożoność czasową. Algorytm powinien być możliwie
jak najszybszy (ale przede wszystkim poprawny).
"""
"""
Algorytm dynamiczny
f(i) - maksymalny koszt ukradzionych przedmiotów, jeśli złodziej ma możliwość zabrania przedmiotów od 1 do i
f(i) = max(f(i-1), f(i-2) + A(i)), A(i) - profit zyskany z kradzieży przedmiotu i-tego
f(1) = A(i)
f(0) =  0
f(i) = F[i], F to tablica wielkości n + 1, gdzie n to ilość przedmiotów
złożoność czasowa: O(n)
złożoność pamięciowa: O(n)
"""

def goodThief(A, n):
    F = [0]*(n+1)
    F[1] = A[0]
    for x in range(2, n+1):
        F[x] = max(F[x-1], F[x-2] + A[x-1])
    result = F[n]
    tab = []
    x = n
    print(F)
    while x > 1:
        if F[x] == F[x-2] + A[x-1]:
            tab.append(A[x-1])
            x -= 2
        elif F[x] == F[x-1]:
            x -= 1
    if x == 1:
        tab.append(A[0])

    for x in range(len(tab)-1, -1, -1):
        print(tab[x], end=" ")
    print()
    return result

A = [42, 12, 63, 43, 32, 120, 4, 23, 1]
print(goodThief(A, len(A)))