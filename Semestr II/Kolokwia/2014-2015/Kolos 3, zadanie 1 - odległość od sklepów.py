"""
1. W miasteczku są sklepy i domy. Trzeba sprawdzić jak daleko do najbliższego sklepu mają
mieszkańcy.
struct Vertex {
bool shop; // true-sklep, false-dom
int* distances; // tablica odległości do innych wierzchołków
int* edges; // numery wierzchołków opisanych w distances
int edge; // rozmiar tablicy distances (i edges)
int d store; // odległość do najbliższego sklepu
};
Zaimplementować funkcję distanceToClosestStore (int n, Vertex* village)
uzupełniającą d store dla tablicy Vertexów i oszacować złożoność algorytmu.
"""

"""
Puszczam zmodyfikowanego BFS-a, który w jednej kolejce przechodzi po jednej jednostce odległości. Jeśli pozostała odległość
jest większa od 1 to zmniejszamy odległość do przebycia o 1 i z powrotem dodajemy wierzchołek do kolejki. Najpierw znajdujemy
wszystkie sklepy i umieszczamy je w kolejce, następnie dla takiej kolejki wypełnionej sklepami puszczamy zmodyfikowanego BFS-a.
Złożoność obliczeniowa: O(k), gdzie k to maksymalna długość ścieżki w grafie
"""
from queue import Queue


def distanceToClosestStore(n, shop, distances, edges, edge, d_store):

    def bfs_2(n, shop, distances, edges, edge, d_store):
        queue = Queue()
        visited = [False] * n
        for x in range(n):
            if shop[x]:
                queue.put([x, 0, -1])

        while not queue.empty():
            u = queue.get()
            if not visited[u[0]]:
                if u[1] > 1:
                    queue.put([u[0], u[1] -1, u[2]+1])
                else:
                    d_store[u[0]] = u[2] + 1
                    visited[u[0]] = True
                    for v in range(edge[u[0]]):
                        if not visited[edges[u[0]][v]]:
                            queue.put([edges[u[0]][v], distances[u[0]][v], d_store[u[0]]])

    bfs_2(n, shop, distances, edges, edge, d_store)

shop = [0, 0, 1, 1, 0, 0]
edges = [[1], [3, 4, 0], [4], [1, 5], [2, 1, 5], [4, 3]]
distances = [[3], [11, 8, 3], [4], [11, 9], [4, 8, 12], [12, 9]]
edge = [1, 3, 1, 2, 3, 2]
n = len(shop)
d_store = [0]*n
distanceToClosestStore(n, shop, distances, edges, edge, d_store)
print(d_store)