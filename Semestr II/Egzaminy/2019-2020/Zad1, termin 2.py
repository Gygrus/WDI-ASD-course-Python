"""
Żab Zbigniew skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc wyłącznie w kierunku
większych liczb. Skok z liczby i do liczby j (j > i) kosztuje Zbigniewa j − i jednostek energii, a jego
energia nigdy nie może spaść poniżej zera. Na początku Zbigniew ma 0 jednostek energii, ale na
szczęście na niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej
(wartość przekąki dodaje się do aktualnej energii Zbigniewa).
Proszę zaimplementować funkcję zbigniew(A), która otrzymuje na wejściu tablicę A długości
len(A) = n, gdzie każde pole zawiera wartość energetyczną przekąski leżącej na odpowiedniej liczbie. Funkcja powinna zwrócić minimalną liczbę skoków potrzebną, żeby Zbigniew dotarł z zera do
n-1 lub −1 jeśli nie jest to możliwe.
Podpowiedź. Warto rozważyć funkcję f(i, y) zwracającą minimalną liczbę skoków potrzebną by
dotrzeć do liczby i mając w zapasie dokładnie y jednostek energii.
Przykład. Dla tablicy A = [2,2,1,0,0,0] wynikiem jest 3 (Zbigniew skacze z 0 na 1, z 1
na 2 i z 2 na 5, kończąc z zerową energią). Dla tablicy A = [4,5,2,4,1,2,1,0] wynikiem jest 2
(Zbigniew skacze z 0 na 3 i z 3 na 7, kończąc z jedną jednostką energii).
"""

def zbigniew(A):
    n = len(A)
    energy = 0
    for x in range(n):
        energy += A[x]

    energy += n

    F = [[float('inf') for _ in range(energy+1)] for _ in range(n)]
    F[0][A[0]] = 0

    for x in range(1, n):
        for y in range(energy+1 - n):
            if y >= A[x]:
                for i in range(x-1, -1, -1):
                    print(x, y, i, A[x])
                    if F[i][y-A[x]+(x-i)] + 1 < F[x][y]:
                        F[x][y] = F[i][y-A[x]+(x-i)] + 1

    smallest = float('inf')
    for x in F:
        print(x)
    for x in F[n-1]:
        if x < smallest:
            smallest = x

    return smallest


A = [4,5,2,4,1,2,1,0]
print(zbigniew(A))