"""
Problem plecakowy w czasie O(nP), gdzie P to suma profitów wszystkich elementów
"""

"""
Tym razem tablica F[i] pokazuje najmniejszą możliwą wagę elementów o proficie większym bądź równym i."""


def knapsack_second(W, P, MaxW):
    n = len(W)
    maxP = 0
    m_w = 0
    for x in range(n):
        maxP += P[x]
        m_w += W[x]

    F = [m_w+1]*n
    for x in range(n):
        F[x] = [m_w+1]*(maxP+1)

    for x in range(n):
        F[x][0] = 0

    for x in range(1, maxP+1):
        if x <= P[0]:
            F[0][x] = W[0]
        else:
            break

    for i in range(1, n):
        for j in range(maxP+1):
            if j < P[i]:
                F[i][j] = min(F[i-1][j], W[i])
            else:
                F[i][j] = F[i-1][j]
                F[i][j] = min(F[i][j], F[i-1][j-P[i]] + W[i])

    for x in range(n):
        print(F[x])



    for x in range(maxP, -1, -1):
        if F[n-1][x] <= MaxW:
            return x



W = [4, 5, 6]
P = [1, 2, 3]
MaxW = 6
print(knapsack_second(W, P, MaxW))
