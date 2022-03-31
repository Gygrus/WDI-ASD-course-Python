"""
Dany jest graf skierowany G = (V,E) w reprezentacji macierzowej (bez wag).
Proszę zaimplementować algorytm, który oblicza domknięcie przechodnie grafu G
(domknięcie przechodnie grafu G to taki graf H, że w H mamy krawędź z u do v
wtedy i tylko wtedy gdy w G jest ścieżka skierowana z u do v).
"""

# zakładam że w reprezentacji macierzowej "-1" oznacza brak krawędzi a "1" istnienie krawędzi
def domkniecie_przechodnie(G):
    n = len(G)
    S = [[float('inf') for _ in range(n)] for _ in range(n)]
    P = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]:
                S[i][j] = G[i][j]
                P[i][j] = i

        S[i][i] = 0

    for t in range(n):
        for u in range(n):
            for v in range(n):
                if G[u][t] + G[t][v] < G[u][v]:
                    G[u][v] = G[u][t] + G[t][v]
                    P[u][v] = P[t][v]

    for x in range(n):
        for y in range(n):
            if S[x][y] == 0 or S[x][y] == float('inf'):
                S[x][y] = -1
            else:
                S[x][y] = 1

    for x in S:
        print(x)


