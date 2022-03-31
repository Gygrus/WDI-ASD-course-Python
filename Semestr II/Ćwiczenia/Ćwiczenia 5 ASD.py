"""
Zadanie 3. (najdłuższy wspólny podciąg) Mamy dane dwie tablice, A[n] i B[n]. Należy znaleźć
długość ich najdłuższego wspólnego podciągu. (Klasyczny algorytm dynamiczny O(n2))
"""


def common_subseries(A, B):
    n = len(A)

    F = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        F[0][i] = 0

    for i in range(n + 1):
        F[i][0] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (A[i - 1] == B[j - 1]):
                F[i][j] = F[i - 1][j - 1] + 1
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])

    return F[n][n]


# A = [1, 2, 3, 4, 7]
# B = [2, 4, 1, 0, 7]
#
# print(common_subseries(A, B))

"""Zadanie 6. (wydawanie monet) Mamy daną tablicę z nominałami monet stosowanych w pewnym dziw-
nym kraju, oraz kwotę T. Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania
kwoty T (algorytm zachłanny, wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda
kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5)."""


def min_coins(coins, t):
    n = len(coins)
    F = [t+1 for _ in range(t + 1)]
    F[0] = 0

    for i in range(n):
        # print(F)
        for j in range(t + 1):
            # print(F)
            if coins[i] <= j:
                F[j] = min(F[j - coins[i]] + 1, F[j])

        print(F)

    print(F)
    return F[t]


print(min_coins([8, 3, 2], 22))

"""
Zadanie 4. (mnożenie macierzy) Dany jest cięg macierzy A1, A2, . . . , An. Ktoś chce policzyć iloczyn
A1A2⋯An. Macierze nie sa koniecznie kwadratowe (ale oczywiście znamy ich rozmiary). Zależnie w jakiej
kolejnosci wykonujemy mnożenia, koszt obliczeniowy moze byc różny—należy podać algorytm znajdujący
koszt mnożenia przy optymalnym doborze kolejności."""

A = [[10, 100], [100, 10], [10, 1000]]

# A = [[10, 100], [100, 10], [10, 1000], [1000, 10]]
A = [[10, 100], [100, 10], [10, 1000]]
#                 i             j
#                 k
#                   X           Y

def cost(A, B):
  return A[0] * A[1] * B[1]

def matrices(A):
  n = len(A)
  F = [[0 for _ in range(n)] for __ in range(n)]

  for i in range(n-2, -1, -1):
    for j in range(i+1, n):
      for k in range(i, j):
        X = [A[i][0], A[k][1]]
        Y = [A[k+1][0], A[j][1]]
        if F[i][j] == 0:
          F[i][j] = cost(X, Y) + F[i][k] + F[k+1][j]
        else:
          F[i][j] = min(F[i][j], cost(X, Y) + F[i][k] + F[k+1][j])

  # print(F)
  return F[0][n-1]

print(matrices(A))


