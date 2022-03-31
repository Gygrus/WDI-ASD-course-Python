def bridges(G):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    value = [[0, 0] for _ in range(n)]
    wsteczne = []
    time = 0
    def dfs_visit(u, parent, value):
        nonlocal G, visited, time, wsteczne

        visited[u] = True
        time += 1
        value[u][0], value[u][1] = time, time
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs_visit(v, parent, value)
            elif visited[v] and v != parent[u]:
                wsteczne.append([u, v])
                wsteczne.append([v, u])
                if value[u][1] > value[v][0]:
                    value[u][1] = value[v][0]
        for v in G[u]:
            if visited[v] and v != parent[u] and [u, v] not in wsteczne:
                if value[u][1] > value[v][1]:
                    value[u][1] = value[v][1]

    dfs_visit(0, parent, value)
    for x in range(n):
        if value[x][0] == value[x][1] and parent[x] is not None:
            print(x, parent[x])


G = [[1, 4], [0, 2], [1, 3, 4], [2, 6, 5], [2, 0, 7], [6, 3], [5, 3], [4]]
bridges(G)
