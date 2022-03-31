"""
Dany jest graf skierowany G = (V, E) oraz funkcja opisująca pojemności jego
krawędzi c: E → N. Proszę zaimplementować funkcję max extending path, która dostaje na wejściu G, c, oraz wierzchołki s i t i znajduje ścieżkę skierowaną z
s do t o maksymalnej przepustowości (czyli minimalna przepustowość krawędzi
na ścieżce powinna być jak największa).
Graf G oraz funkcja c reprezentowane są łącznie przez listy sąsiedztwa. Formalnie zbiorem wierzchołków jest V = {0, 1, . . . , n − 1} a G[i] to lista par opisujących krawędzie wychodzące z wierzchołka i. Pierwszym elementem każdej
pary jest wierzchołek do którego dochodzi krawędź a drugim elementem jest
pojemność tej krawędzi. Przykładowo lista:
G = [[(1,4), (2,3)], # 0
[(3,2)], # 1
[(3,5)], # 2
[]] # 3
opisuje graf z wierzchołkami V = {0, 1, 2, 3}, gdzie z wierzchołka 0 mamy krawędzie do wierzchołków 1 i 2 o przepustowościach 4 i 3. Z wierzchołka 1 mamy
krawędź do wierzchołka 3 o przepustowości 2, a z wierzchołka 2 mamy krawędź
do 3 o przepustowości 5. Funkcja powinna zwracać ścieżkę jako listę jej kolejnych
krawędzi. Implementowana funkcja powinna być postaci:
def max_extending_path( G, s, t )
Dla przykładowego grafu G oraz s = 0 i t = 3 wynikiem powinna być lista
[0, 2, 3]. Pojemność tej ścieżki to 3.
"""
from queue import PriorityQueue
# G w postaci list sąsiedztwa
def max_extending_path(G, s, t):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    capacity = [-float('inf')]*n
    queue = PriorityQueue()
    queue.put((capacity[s], s))
    while not queue.empty():
        cap, u = queue.get()
        cap *= -1
        visited[u] = True
        for v, length in G[u]:
            if not visited[v] and min(cap, length) > capacity[v]:
                capacity[v] = min(cap, length)
                parent[v] = u
                queue.put((-capacity[v], v))

    output = []
    idx = t
    while idx != s:
        output.append(idx)
        idx = parent[idx]

    output.append(idx)
    output.reverse()
    return output, capacity[t]

G = [[(1,4), (2,3)], # 0
     [(3,2)], # 1
     [(3,5)], # 2
     []] # 3

print(max_extending_path(G, 0, 3))

