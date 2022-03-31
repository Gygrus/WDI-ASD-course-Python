from math import inf

def tspf(i, j, F, D):
    if F[i][j] != inf:
        return F[i][j]
    if i == j-1:
        best = inf
        for k in range(j-1):
            best = min(best, tspf(k, j-1, F, D)+D[k][j])
        F[j-1][j] = best

    else:
        F[i][j] = tspf(i, j-1, F, D) + D[j-1][j]

    return F[i][j]

n = 10
D[i][j] # odległość pomiędzy miastem i a j
F = [[inf]*n for i in range(n)] # minimalny koszt ścieżki taki, że 0---->i oraz 0----j, j>i,
                                # łącznie te ścieżki odwiedzają wszystkie miasta {1, ..., j}
F[0][1] = D[0][1]

min(f(i, n-1) + d(i, n-1))      # odczytanie rozwiązania