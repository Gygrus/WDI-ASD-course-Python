# Piotr Socała
import copy, collections
from queue import PriorityQueue
def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = collections.deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        for ind, val in enumerate(graph[u]):
            if (visited[ind] == False) and (val > 0):
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return visited[t]

def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow, graph, parent

def BlueAndGreen(T, K, D):
    def floyd_warshall(G):
        n = len(G)
        S = [[float('inf') for _ in range(n)] for _ in range(n)]
        P = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if G[i][j] != False:
                    S[i][j] = G[i][j]
                    P[i][j] = i

            S[i][i] = 0

        for t in range(n):
            for u in range(n):
                for v in range(n):
                    if S[u][v] > S[u][t] + S[t][v]:
                        S[u][v] = S[u][t] + S[t][v]
                        P[u][v] = P[t][v]

        for i in range(n):
            if S[i][i] < 0:
                return "Graf ma ujemne cykle!!!"
        return S

    def dijkstra_matrix(G, s, t, original):
        n = len(G)
        dist = [float('inf')] * n
        visited = [False] * n
        parent = [None] * n
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
                if original[rem][v] >= 0 and dist[rem] + original[rem][v] < dist[v]:
                    dist[v] = dist[rem] + original[rem][v]
                    parent[v] = rem


        return dist[t]
    n = len(T)
    modified_graph = [[0 for _ in range(n+2)] for _ in range(n+2)]
    for x in range(1, n+1):
        if K[x-1] == 'B':
            modified_graph[0][x] = 1
            modified_graph[x][0] = 1
        else:
            modified_graph[0][x] = 0

    for x in range(1, n+2):
        for y in range(1, n+2):
            if x == n+1:
                if y != n+1:
                    if K[y-1] == 'G':
                        modified_graph[x][y] = 1
                        modified_graph[y][x] = 1
            elif x < n+1 and y < n+1:
                # print(x, y)
                modified_graph[x][y] = T[x-1][y-1]

    for x in modified_graph:
        print(x)
    copy = modified_graph[::]
    flow, net, parent = edmonds_karp(modified_graph, 0, n+1)
    u = n+1
    results = []
    output = 0
    for v in range(n+2):
        if net[u][v] == 1:
            results.append(v)

    for u in results:
        temp = u
        while temp != 0:
            if dijkstra_matrix(net, u, 0, modified_graph) >= D - 1:
                output += 1

    return output

T = [
[0, 1, 1, 0, 1],
[1, 0, 0, 1, 0],
[1, 0, 0, 0, 1],
[0, 1, 0, 0, 1],
[1, 0, 1, 1, 0],
]
K = ['B', 'B', 'G', 'G', 'B']
D = 2

print(BlueAndGreen(T, K, D))