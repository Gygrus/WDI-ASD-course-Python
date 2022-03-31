from math import inf
from queue import PriorityQueue

def min_cycle(G):
    def dijkstra(graph, s, t):
        nonlocal distances, parent, visited, n
        def relax(u, v, w):
            nonlocal distances, parent, graph
            if distances[v] > distances[u] + w:
                distances[v] = distances[u] + w
                parent[v] = u

        counter = n
        for x in range(n):
            parent[x] = None
            distances[x] = inf
            visited[x] = False
        distances[s] = 0
        queue = PriorityQueue()
        queue.put((distances[s], s))

        while not queue.empty() and counter > 0:
            val, u = queue.get()
            if u == t:
                return
            counter -= 1
            if not visited[u]:
                visited[u] = True
                for v in range(n):
                    if not visited[v] and graph[u][v] >= 0:
                        relax(u, v, graph[u][v])
                        queue.put((distances[v], v))


    n = len(G)
    distances = [inf]*n
    parent = [None]*n
    visited = [False]*n
    result = []
    best = inf
    pair = None
    for i in range(n):
        temp = 0
        for j in range(i+1, n):
            if G[i][j] >= 0:
                temp = G[i][j]
                G[i][j] = G[j][i] = -1
                dijkstra(G, i, j)
                if distances[j] + temp < best:
                    pair = (i, j)
                    best = distances[j]  + temp
                    result = parent[::]
                G[i][j] = G[j][i] = temp

    if best == inf:
        return []

    idx = pair[1]
    output = []
    output.append(idx)
    while result[idx] != result[pair[0]]:
        output.append(result[idx])
        idx = result[idx]

    return output, best

# G = [[-1, 2,-1,-1, 1],
# [ 2,-1, 4, 1,-1],
# [-1, 4,-1, 5,-1],
# [-1, 1, 5,-1, 3],
# [ 1,-1,-1, 3,-1]]
G = [[-1, 2, 4, -1, 1, 1],
     [2, -1, 1, -1, -1, -1],
     [4, 1, -1, 5, 3, 2],
     [-1, -1, 5, -1, -1, -1],
     [1, -1, 3, -1, -1, 3],
     [1, -1, 2, -1, 3, -1]]

graph = [[-1, 4, -1, -1, -1, -1, -1, 8, -1],
         [4, -1, 8, -1, -1, -1, -1, 11, -1],
         [-1, 8, -1, 7, -1, 4, -1, -1, 2],
         [-1, -1, 7, -1, 9, 14, -1, -1, -1],
         [-1, -1, -1, 9, -1, 10, -1, -1, -1],
         [-1, -1, 4, 14, 10, -1, 2, -1, -1],
         [-1, -1, -1, -1, -1, 2, -1, 1, 6],
         [8, 11, -1, -1, -1, -1, 1, -1, 7],
         [-1, -1, 2, -1, -1, -1, 6, 7, -1]]

G1 = [[-1, 2,-1,-1, 1],
    [ 2,-1, -1, -1,-1],
    [-1, -1,-1, 5,-1],
    [-1, -1, 5,-1, 3],
    [ 1,-1,-1, 3,-1]]

G23 = [[-1, 1,-1, 4, 1],
     [ 1,-1, 1,-1, 4],
     [-1, 1,-1, 1, 4],
     [ 4,-1, 1,-1, 1],
     [ 1, 4, 4, 1,-1]]
print(min_cycle(G23))