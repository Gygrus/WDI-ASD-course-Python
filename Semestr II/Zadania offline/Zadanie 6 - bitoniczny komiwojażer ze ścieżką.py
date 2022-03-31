from math import inf
from math import *

C = [["A", 0, 2], ["B", 4, 3], ["C", 2, 4], ["D", 3, 1], ["E", 1, 3],["F",0.5,-2]]
# C = [["Wrocław", 3, 0], ["Warszawa",36,3],
# ["Gdańsk", -1,10], ["Kraków",-5,1]]

def bitonicTSP(C):
    def q_sort(Tab, p, r):
        def quicksort(Tab, p, r):
            while p < r:
                q = partition(Tab, p, r)
                quicksort(Tab, p, q - 1)
                p = q + 1

        def partition(Tab, p, r):
            x = Tab[r][1]
            i = p - 1
            for j in range(p, r):
                if Tab[j][1] < x:
                    i += 1
                    Tab[i], Tab[j] = Tab[j], Tab[i]
            Tab[i + 1], Tab[r] = Tab[r], Tab[i + 1]
            return i + 1

        quicksort(Tab, p, r)

    def get_distance(first, second):
        return (abs(first[1] - second[1])**2 + abs(first[2] - second[2])**2)**(1/2)

    def tspf(i, j, F, D):
        # print(i, j, F)
        if F[i][j][0] != inf:
            # print(i, j, F)
            return F[i][j]
        if i == j - 1:
            best = inf
            for k in range(j - 1):
                x = list(tspf(k, j - 1, F, D))
                # print(x)
                if best > x[0] + D[k][j]:
                    a = x[0] + D[k][j]
                    # print(x[1])
                    # x[1].append(C[j][0])
                    b = list(x[1])
                    b.append(C[j][0])
                    # print(b)
                    c = list(x[2])
                    best = x[0] + D[k][j]
                del x

            F[j - 1][j][0] = a
            F[j - 1][j][1] = c
            F[j - 1][j][2] = b
            del a
            del b
            del c

        else:
            x = list(tspf(i, j - 1, F, D))
            # print(i, j, x)
            # x[2].append(C[j][0])
            a = x[0]+D[j-1][j]
            c = list(x[2])
            c.append(C[j][0])
            b = list(x[1])
            F[i][j][0] = a
            F[i][j][1] = b
            F[i][j][2] = c
            del x
            del a
            del b
            del c
        # print(i, j, F)
        return F[i][j]

    n = len(C)
    q_sort(C, 0, n-1)
    print(C)
    D = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            D[x][y] = get_distance(C[x], C[y])

    F = [[[inf, list(), list()] for _ in range(n)]  for _ in range(n)]
    F[0][1] = [D[0][1], list(), [C[1][0]]]

    minimal = [inf, list(), list()]
    for k in range(n-1):
        x = list(tspf(k, n-1, F, D))
        if x[0] + D[k][n-1] < minimal[0]:
            minimal = x
            minimal[0] += D[k][n-1]

    for x in range(n):
        print(F[x])

    x = len(minimal[2])
    y = len(minimal[1])
    print(minimal[0])
    print(C[0][0], end=", ")
    # new = 0
    # prev = 0
    for j in range(x):
        print(minimal[2][j], end=", ")

    for i in range(y-1, -1, -1):
        print(minimal[1][i], end=", ")
    print(C[0][0])



bitonicTSP(C)


