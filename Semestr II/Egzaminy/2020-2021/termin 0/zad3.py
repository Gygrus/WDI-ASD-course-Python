"""
Dany jest ważony, nieskierowany graf G oraz dwumilowe buty - specjalny sposób poruszania się
po grafie. Dwumilowe buty umożliwiają pokonywanie ścieżki złożonej z dwóch krawędzi grafu tak,
jakby była ona pojedynczą krawędzią o wadze równej maksimum wag obu krawędzi ze ścieżki.
Istnieje jednak ograniczenie - pomiędzy każdymi dwoma użyciami dwumilowych butów należy
przejść w grafie co najmniej jedną krawędź w sposób zwyczajny. Macierz G zawiera wagi krawędzi
w grafie, będące liczbami naturalnymi, wartość 0 oznacza brak krawędzi.
Proszę opisać, zaimplementować i oszacować złożoność algorytmu znajdowania najkrótszej ścieżki
w grafie z wykorzystaniem mechanizmu dwumilowych butów.
Rozwiązanie należy zaimplementować w postaci funkcji:
def jumper(G, s, w):
...
która zwraca długość najkrótszej ścieżki w grafie G pomiędzy wierzchołkami s i w, zgodnie z zasadami używania dwumilowych butów.
Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę przedstawić złożoność
czasową oraz pamięciową użytego algorytmu
"""
from queue import PriorityQueue

def jumper(G, s, w):
    n = len(G)
    distance = [[float('inf'), float('inf')] for _ in range(n)]
    visited = [[False, False] for _ in range(n)]

    Q = PriorityQueue()
    distance[s][0] = distance[s][1] = 0
    visited[s][0] = visited[s][1] = True
    Q.put((0, s, 0, 0))
    while not Q.empty():
        dist, u, val, type = Q.get()
        # print("dist = ", dist, "u = ", u, "val = ", val, "type = ",  type)
        # print(distance)
        if type == 1:
            temp = val
            for v in range(n):
                if G[u][v] > 0 and not visited[v][0] and not visited[v][1]:
                    # print('gówno')
                    val = max(temp, G[u][v])
                    if distance[v][1] > dist+val:
                        # print('gówno')
                        # print(v, val, dist, distance[v][1], 'dupa')
                    # val = max(val, G[u][v])
                    #     distance[v][1] = dist+val
                        Q.put((dist+val, v, val, 2))

        elif type == 2:
            # if not visited[u][1]:
            visited[u][1] = True
            if distance[u][1] > dist:
                distance[u][1] = dist

                for v in range(n):
                    if G[u][v] > 0 and not visited[v][0] and distance[v][0] > distance[u][1]+G[u][v]:
                        # distance[v][0] = distance[u][1] + G[u][v]
                        Q.put((distance[u][1] + G[u][v], v, G[u][v], 0))

        else:
            visited[u][0] = True
            # distance[u][0] = dist
            if distance[u][0] >= dist:
                distance[u][0] = dist
                for v in range(n):
                    if G[u][v] > 0 and not visited[v][0] and distance[v][0] > distance[u][0] + G[u][v]:
                        # distance[v][0] = distance[u][1] + G[u][v]
                        Q.put((distance[u][0] + G[u][v], v, G[u][v], 0))
                    if G[u][v] > 0:
                        Q.put((distance[u][0], v, G[u][v], 1))


    print(distance)
    return min(distance[w][0], distance[w][1])



g = [[0, 1, 200, 200, 200, 200],
 [1, 0, 2, 200, 200, 200],
 [200, 2, 0, 40, 200, 200],
 [200, 200, 40, 0, 40, 200],
 [200, 200, 200, 40, 0, 117],
 [200, 200, 200, 200, 117, 0]]
print(jumper(g, 0, 3))
