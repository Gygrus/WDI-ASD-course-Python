"""
Dana jest tablica dwuwymiarowa G, przedstawiająca macierz sąsiedztwa skierowanego grafu ważonego, który odpowiada mapie drogowej (wagi przedstawiają odległości, liczba -1 oznacza brak
krawędzi). W niektórych wierzchołkach są stacje paliw, podana jest ich lista P. Pełnego baku wystarczy na przejechanie odległości d. Wjeżdżając na stację samochód zawsze jest tankowany do pełna.
Proszę zaimplemntować funkcję jak dojade(G, P, d, a, b), która szuka najkrótszej możliwej
trasy od wierzchołka a do wierzchołka b, jeśli taka istnieje, i zwraca listę kolejnych odwiedzanych
na trasie wierzchołków (zakładamy, że w a też jest stacja paliw; samochód może przejechać najwyżej
odległość d bez tankowania).
Zaproponowana funkcja powinna być możliwe jak najszybsza. Uzasadnij jej poprawność i oszacuj
złożoność obliczeniową.
Przykład Dla tablic
G = [[-1, 6,-1, 5, 2],
[-1,-1, 1, 2,-1],
[-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1],
[-1,-1, 8,-1,-1]]
P = [0,1,3]
"""

def jak_dojade(G, P, d, a, b):
    n = len(G)

    def dijkstra_matrix(G, P, d, s, t):
        n = len(G)
        dist = [[float('inf') for _ in range(d+1)] for _ in range(n)]
        visited = [[False for _ in range(d+1)] for _ in range(n)]
        parent = [[[None, None] for _ in range(d+1)] for _ in range(n)]
        tab_of_fuel = [0]*n
        for x in P:
            tab_of_fuel[x] = 1

        dist[s][d] = 0
        check = True
        rem = 0
        for _ in range(n * (d+1)):
            min = float('inf')
            rem_fuel = 0
            for x in range(n):
                for y in range(d+1):
                    if dist[x][y] < min and not visited[x][y]:
                        rem = x
                        rem_fuel = y
                        min = dist[x][y]

            visited[rem][rem_fuel] = True
            for v in range(n):
                # print('gówno')
                if not tab_of_fuel[v]:
                    if G[rem][v] >= 0 and G[rem][v] <= rem_fuel and dist[rem][rem_fuel] + G[rem][v] < dist[v][rem_fuel - G[rem][v]]:
                        # print('gówno')
                        dist[v][rem_fuel - G[rem][v]] = dist[rem][rem_fuel] + G[rem][v]
                        parent[v][rem_fuel - G[rem][v]][0] = rem
                        parent[v][rem_fuel - G[rem][v]][1] = rem_fuel

                else:
                    if G[rem][v] >= 0 and G[rem][v] <= rem_fuel and dist[rem][rem_fuel] + G[rem][v] < dist[v][d]:
                        dist[v][d] = dist[rem][rem_fuel] + G[rem][v]
                        parent[v][d][0] = rem
                        parent[v][d][1] = rem_fuel

        return parent, dist

    parent, dist = dijkstra_matrix(G, P, d, a, b)
    rem_d = 0
    rem_val = float('inf')
    for x in range(d+1):
        if dist[b][x] < rem_val:
            rem_val = dist[b][x]
            rem_d = x

    if rem_val == float('inf'):
        return None

    output = [b]
    p = b
    while parent[p][rem_d][0] is not a:
        output.append(parent[p][rem_d][0])
        temp_p = parent[p][rem_d][0]
        temp_d = parent[p][rem_d][1]
        p = temp_p
        rem_d = temp_d

    output.append(a)
    return output[::-1]

G = [[-1, 6,-1, 5, 2],
[-1,-1, 1, 2,-1],
[-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1],
[-1,-1, 8,-1,-1]]
P = [0,1,3]

print(jak_dojade(G, P, 6, 0, 2))
