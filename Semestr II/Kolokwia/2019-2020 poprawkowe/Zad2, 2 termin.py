"""
Dany jest graf nieskierowany G = (V, E), gdzie każdy wierzchołek z V ma przypisaną małą literę z
alfabetu łacińskiego, a każda krawędź ma wagę (dodatnią liczbę całkowitą). Dane jest także słowo
W = W[0], . . . ,W[n − 1] składające się małych liter alfabetu łacińskiego. Należy zaimplementować
funkcję letters(G,W), która oblicza długość najkrótszej ścieżki w grafie G, której wierzchołki
układają się dokładnie w słowo W (ścieżka ta nie musi być prosta i może powtarzać wierzchołki).
Jeśli takiej ścieżki nie ma, należy zwrócić -1.
Struktury danych. Graf G ma n wierzchołków ponumerowanych od 0 do n − 1 i jest reprezentowany jako para (L, E). L to lista o długości n, gdzie L[i] to litera przechowywana w wierzchołku
i. E jest listą krawędzi i każdy jej element jest trójką postaci (u, v, w), gdzie u i v to wierzchołki
połączone krawędzią o wadze w.
Przykład. Rozważmy graf G przedstawiony poniżej:
0∶ k
1∶ k
2∶ o
3∶ o
4∶t
5∶t
2
1
2
3
5
1
3
W reprezentacji przyjętej w zadaniu mógłby być zapisany jako:
# 0 1 2 3 4 5
L = ["k","k","o","o","t","t"]
E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]
G = (L,E)
Rozwiązaniem dla tego grafu i słowa W = "kto" jest 4 i jest osiągane przez ścieżkę 1 − 4 − 3. Inna
ścieżka realizująca to słowo to 1 − 4 − 2, ale ma koszt 8.
"""
from queue import PriorityQueue

# prawdopodobnie gorsze rozwiązanie
# def letters(G, W):
#     def dijkstra(graph, L, word, n):
#         n = len(graph)
#         queue = PriorityQueue()
#         for x in range(n):
#             if L[x] == word[0]:
#                 queue.put((0, x, 0))
#
#         while not queue.empty():
#             distance, vertex, index = queue.get()
#             if index == len(word)-1:
#                 return distance
#
#             for v, dist in graph[vertex]:
#                 if L[v] == word[index+1]:
#                     queue.put((dist+distance, v, index+1))
#
#
#         return -1
#     L = G[0]
#     E = G[1]
#     n = len(L)
#     # tworzę listę sąsiedztwa, gdzie dla indeksu i krotka (a, b) oznacza że istnieje krawędź z i do a o wartości b
#     graph = [[] for _ in range(n)]
#     for e in E:
#         graph[e[0]].append((e[1], e[2]))
#         graph[e[1]].append((e[0], e[2]))
#
#     return dijkstra(graph, L, W, n)

def letters(G, W):
    def dijkstra_matrix(G, L, word):
        n = len(G)
        w = len(word)
        dist = [[float('inf') for _ in range(w)] for _ in range(n)]
        visited = [[False for _ in range(w)] for _ in range(n)]
        for x in range(n):
            if L[x] == word[0]:
                dist[x][0] = 0

        for _ in range(n*w):
            minim = float('inf')
            for x in range(n):
                for y in range(w):
                    if dist[x][y] < minim and not visited[x][y]:
                        rem_x = x
                        rem_y = y
                        minim = dist[x][y]

            visited[rem_x][rem_y] = True
            if rem_y < w-1:
                for v in range(n):
                    if L[v] == word[rem_y+1] and G[rem_x][v] > 0 and not visited[v][rem_y+1] and dist[rem_x][rem_y] + G[rem_x][v] < dist[v][rem_y+1]:
                        dist[v][rem_y + 1] = dist[rem_x][rem_y] + G[rem_x][v]

        return dist

    L = G[0]
    E = G[1]
    n = len(L)
    w = len(W)
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for e in E:
        graph[e[0]][e[1]] = e[2]
        graph[e[1]][e[0]] = e[2]

    # for x in graph:
    #     print(x)

    distances = dijkstra_matrix(graph, L, W)
    # for x in distances:
    #     print(x)
    result = float('inf')
    for x in range(n):
        if distances[x][w-1] < result and L[x] == W[w-1]:
            result = distances[x][w-1]

    if result == float('inf'):
        return -1

    return result




L = ["k","k","o","o","t","t"]
E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]
G = (L,E)
W = "kto"
print(letters(G, W))


