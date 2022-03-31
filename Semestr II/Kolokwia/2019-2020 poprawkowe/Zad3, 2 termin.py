"""
Dana jest tablica T zawierająca N liczb naturalnych. Z pozycji a można przeskoczyć na pozycję b
jeżeli liczby T[a] i T[b] mają co najmniej jedną wspólną cyfrę. Koszt takego skoku równy ∣T[a] −
T[b]∣. Proszę napisać funkcję, która wyznacza minimalny sumaryczny koszt przejścia z najmniejszej
do największej liczby w tablicy T. Jeżeli takie przejście jest niemożliwe, funkcja powinna zwrócić
wartość -1.
Przykład Dla tablicy T = [123,890,688,587,257,246] wynikiem jest liczba 767, a dla tablicy
T = [587,990,257,246,668,132] wynikiem jest liczba -1.
"""
def check_if_exists(num1, num2):
    rem1 = num1
    rem2 = num2
    tab_of_numbers = [0]*10
    while rem1 > 0:
        if tab_of_numbers[rem1%10] == 0:
            tab_of_numbers[rem1%10] = 1
        rem1 //= 10

    check = False
    while rem2 > 0:
        if tab_of_numbers[rem2%10] == 1:
            check = True
            break
        rem2 //= 10

    if check:
        return abs(num1-num2)

    return -1



def find_cost(P):
    def dijkstra_matrix(G, s, t):
        n = len(G)
        dist = [float('inf')] * n
        visited = [False] * n
        parent = [None] * n
        dist[s] = 0
        rem = 0
        for _ in range(n):
            minimum = float('inf')
            for x in range(n):
                if dist[x] < minimum and not visited[x]:
                    rem = x
                    minimum = dist[x]

            visited[rem] = True
            for v in range(n):
                if G[rem][v] >= 0 and dist[rem] + G[rem][v] < dist[v]:
                    dist[v] = dist[rem] + G[rem][v]
                    parent[v] = rem

        return dist[t]

    n = len(P)
    distance = [[float('inf') for _ in range(n)] for _ in range(n)]
    graph = [[-1 for _ in range(n)] for _ in range(n)]
    minimal = float('inf')
    maximal = 0
    a, b = 0, 0
    for x in range(n):
        if P[x] < minimal:
            minimal = P[x]
            a = x
        if P[x] > maximal:
            maximal = P[x]
            b = x

    for x in range(n):
        for y in range(n):
            if x != y:
                graph[x][y] = check_if_exists(P[x], P[y])

    result = dijkstra_matrix(graph, a, b)
    if result == float('inf'):
        return -1

    return result


T = [587,990,257,246,668,132]
print(find_cost(T))