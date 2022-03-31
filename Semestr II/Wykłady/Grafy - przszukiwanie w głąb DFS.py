class Node():
    def __init__(self):
        self.d = 0
        self.parent = None
        self.neighbours = []
        self.visited = False

def DFS(G):
    def DFSVisit(G, u):
        nonlocal time
        time += 1
        u.visited = True
        for v in u.neighbours:
            if not G[v].visited:
                G[v].parent = u
                DFSVisit(G, G[v])

        time += 1

    n = len(G)
    for v in range(n):
        G[v].parent = None
        G[v].visited = False

    time = 0
    for u in range(n):
        if not G[u].visited:
            DFSVisit(G, G[u])


# wersja bit algo
### Implementacja DFS dla grafu w postaci list sąsiedztwa

def dfs(graph, s):
    visited = [False] * len(graph)

    def dfs_visit(u):
        nonlocal graph, visited

        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs_visit(v)

    dfs_visit(s)


pom = [[1, 2], [0, 4], [0, 3, 5], [2, 4], [1, 3, 5], [2, 4, 6], [5, 7], [6]]
G = [[] for _ in range(len(pom))]
for x in range(len(pom)):
    G[x] = Vertex()
    G[x].neighbours = pom[x]
    print(G[x].neighbours)

DFS(G)
