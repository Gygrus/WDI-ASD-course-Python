"""
Zadanie 5 (dwuwymiarowy problem plecakowy) Proszę zaproponować algorytm dla dwuwymiarowej
wersji dyskretnego problemu plecakowego. Mamy dany zbiór P = {p1, . . . , pn} przedmiotów i dla każdego
przedmiotu pi dane sa nastepujace trzy liczby:
1. v(pi) – wartość przedmiotu,
2. w(pi) – waga przedmiotu, oraz
3. h(pi) – wysokość przedmiotu.
Złodziej chce wybrać przedmioty o maksymalnej wartości, których łączna waga nie przekracza danej liczby
W oraz których łączna wysokość nie przekracza danej liczby H (przedmioty zapakowane są w kartony, które
złodziej układa jeden na drugim). Proszę oszacować złozoność czasową swojego algorytmu oraz uzasadnić
jego poprawność
"""

"""
f(i, j, k) - maksymalna wartość zabranych przedmiotów uwzględniając i początkowych, które nie przkraczają wagi j i 
wysokości k
f(i, j, k) = max(f(i-1, j, k), f(i-1, j-w(i), k-h(i)) + v(i)) if w(i) < j and h(i) < k
f(0, w(0), h(0)) do f(0, W, H) = v(0)
wynik: f(n-1, W, H) 
"""

def knapsack_2d(v, w, h, W, H):
    n = len(v)
    F = [[[0 for _ in range(H+1)] for _ in range(W+1)] for _ in range(n)]
    # F[0][3][2] = 1
    # for x in range(n):
    #     print(F[x])
    for x in range(w[0], W+1):
        for y in range(h[0], H+1):
            F[0][x][y] = v[0]

    for i in range(1, n):
        for j in range(W+1):
            for k in range(H+1):
                F[i][j][k] = F[i-1][j][k]
                if w[i] <= j and h[i] <= k:
                    if F[i-1][j-w[i]][k-h[i]] + v[i] > F[i][j][k]:
                        F[i][j][k] = F[i-1][j-w[i]][k-h[i]] + v[i]

    print(F[n-1][W][H])
    for x in range(n):
        print(F[x])

knapsack_2d([3, 7, 2, 3, 12, 5], [2, 5, 1, 4, 6, 5], [4, 8, 1, 5, 5, 2], 17, 20)