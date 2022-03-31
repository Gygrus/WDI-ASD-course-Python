"""
Dany jest ciąg klocków (a1, b1), . . . (an, bn). Każdy klocek zaczyna się na pozycji ai
i ciągnie się
do pozycji bi
. Klocki mogą spadać w kolejności takiej jak w ciągu. Proszę zaimplementować funkcję
tower(A), która wybiera możliwie najdłuższy podciąg klocków taki, że spadając tworzą wieżę i
żaden klocek nie wystaje poza którykolwiek z wcześniejszych klocków. Do funkcji przekazujemy
tablicę A zawierającą pozycje klocków ai
,bi
. Funkcja powinna zwrócić maksymalną wysokość wieży
jaką można uzyskać w klocków w tablicy A.
Przykład Dla tablicy A = [(1,4),(0,5),(1,5),(2,6),(2,4)] wynikiem jest 3, natomiast dla
tablicy A = [(10,15),(8,14),(1,6),(3,10),(8,11),(6,15)] wynikiem jest 2.
"""


def tower(A):
    n = len(A)
    #pierwsza krotka to współrzędne klocka wiszącego na brzegu, druga wysokość wieży zaczynającej się w i a mającej szczyt w b
    F = [[[[0, 0], 0] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        F[x][x] = [A[x], 1]

    for i in range(n):
        for j in range(i+1, n):
            if A[j][0] >= F[i][i][0][0] and A[j][1] <= F[i][i][0][1]:
                for x in range(i, j):
                    if A[j][0] >= F[i][x][0][0] and A[j][1] <= F[i][x][0][1]:
                        if F[i][j][1] < F[i][x][1] + 1:
                            F[i][j][1] = F[i][x][1] + 1
                            F[i][j][0][0] = A[j][0]
                            F[i][j][0][1] = A[j][1]

    best = 0
    for x in range(n):
        for y in range(x+1, n):
            best = max(best, F[x][y][1])

    return best


def tower_2(A):
    n = len(A)
    F = [1 for _ in range(n)]

    for i in range(1, n):
        for x in range(i):
            if A[i][0] >= A[x][0] and A[i][1] <= A[x][1]:
                F[i] = max(F[i], F[x] + 1)

    best = 0
    for x in range(n):
        best = max(best, F[x])

    return best

A = [(10,15),(8,14),(1,6),(3,10),(8,11),(6,15)]
print(tower(A))
