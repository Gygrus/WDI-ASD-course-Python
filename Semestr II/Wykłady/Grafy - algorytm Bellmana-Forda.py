def bellman_ford(G, s, t):
    def relax(u, v, dist):
        nonlocal G, distance, parent
        if distance[v] > distance[u] + dist:
            distance[v] = distance[u] + dist
            parent[v]  = u

    n = len(G)
    parent = [None]*n
    distance = [float('inf')]*n
    distance[s] = 0
    for i in range(n-1):
        for u in range(n):
            for v, dist in G[u]:
                relax(u, v, dist)

    for u in range(n):
        for v, dist in G[u]:
            if distance[v] > distance[u] + dist:
                return "Mamy ujemny cykl!"

    output = []
    idx = t
    while parent[idx] != None:
        output.append(idx)
        idx = parent[idx]

    output.append(idx)

    return output[::-1], distance[t]