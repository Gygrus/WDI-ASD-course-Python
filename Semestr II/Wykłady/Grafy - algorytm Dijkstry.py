from math import inf
from queue import PriorityQueue



def dijkstra(graph, s, t):
    def relax(u, v, w):
        nonlocal distances, parent, graph
        if distances[v] > distances[u] + w:
            distances[v] = distances[u] + w
            parent[v] = u

    n = len(graph)
    counter = n
    parent = [None]*n
    distances = [inf]*n
    visited = [False]*n
    distances[s] = 0
    queue = PriorityQueue()
    queue.put((distances[s], s))

    while not queue.empty() and counter > 0:
        val, u = queue.get()
        counter -= 1
        if not visited[u]:
            visited[u] = True
            for v, dist in graph[u]:
                if not visited[v]:
                    relax(u, v, dist)
                    queue.put((distances[v], v))

    output = []
    copy_t = t
    output.append(t)
    while parent[t] != parent[s]:
        output.append(parent[t])
        t = parent[t]

    return distances[copy_t], output[::-1]


def dijkstra_algo(graph, s):
    q = PriorityQueue()
    dist = [float('inf') for _ in range(len(graph))]
    counter = len(graph)
    dist[s] = 0
    q.put((0, s))

    while not q.empty() and counter > 0:
        d, v = q.get()
        if d <= dist[v]:
            counter -= 1
            dist[v] = d
            for edge in graph[v]:
                neighbor, edge_len = edge
                q.put((d + edge_len, neighbor))

    return dist


def dijkstra_matrix(G, s, t):
    n = len(G)
    dist = [float('inf')]*n
    visited = [False]*n
    parent = [None]*n
    dist[s] = 0
    check = True
    rem = 0
    for _ in range(n):
        min = float('inf')
        for x in range(n):
            if dist[x] < min and not visited[x]:
                rem = x
                min = dist[x]

        visited[rem] = True
        for v in range(n):
            if G[rem][v] >= 0 and dist[rem] + G[rem][v] < dist[v]:
                dist[v] = dist[rem] + G[rem][v]
                parent[v] = rem

    output = []
    idx = t
    while parent[idx] != None:
        output.append(idx)
        idx = parent[idx]

    output.append(idx)

    return output[::-1], dist[t]

graph_matrix = [[-1, 4, -1, -1, -1, -1, -1, 8, -1],
         [4, -1, 8, -1, -1, -1, -1, 11, -1],
         [-1, 8, -1, 7, -1, 4, -1, -1, 2],
         [-1, -1, 7, -1, 9, 14, -1, -1, -1],
         [-1, -1, -1, 9, -1, 10, -1, -1, -1],
         [-1, -1, 4, 14, 10, -1, 2, -1, -1],
         [-1, -1, -1, -1, -1, 2, -1, 1, 6],
         [8, 11, -1, -1, -1, -1, 1, -1, 7],
         [-1, -1, 2, -1, -1, -1, 6, 7, -1]]

graph = [[[1, 1], [2, 5]],
         [[0, 1], [4, 7], [3, 8], [2, 2]],
         [[0, 5], [1, 2], [3, 3]],
         [[2, 3], [1, 8], [4, 87]],
         [[1, 7], [3, 87]]]
print(dijkstra_matrix(graph_matrix, 0, 4))
