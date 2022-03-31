from queue import Queue

class Vertex():
    def __init__(self):
        self.d = 0
        self.parent = None
        self.neighbours = []


# Zakładam że G to tablica gdzie każdemu wierzchołkowi przypisane są sąsiednie wierzchołki w formie tablicy tablic
# Zakładam też że elementy w G są obiektami klasy Vertex()
def BFS(G, s):
    n = len(G)
    Q = Queue()
    visited = [False for _ in range(n)]
    for v in range(n):
        G[v].d = -1
        G[v].parent = None

    G[s].d = 0
    visited[s] = True
    Q.put(G[s])
    while not Q.empty():
        u = Q.get()
        for v in u.neighbours:
            if not visited[v]:
                visited[v] = True
                G[v].d = u.d + 1
                G[v].parent = u
                Q.put(G[v])

    for x in range(n):
        print(G[x].d)



# wersja bit algo
### Implementacja BFS dla grafu w postaci list sąsiedztwa

def bfs(graph, s):
    queue = Queue()
    visited = [False] * len(graph)

    queue.put(s)
    visited[s] = True

    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.put(v)


G = [[1, 2], [0, 4], [0, 3, 5], [2, 4], [1, 3, 5], [2, 4, 6], [5, 7], [6]]
pom = [[] for _ in range(len(G))]
for x in range(len(G)):
    pom[x] = Vertex()
    pom[x].neighbours = G[x]
    print(pom[x].neighbours)

BFS(pom, 0)