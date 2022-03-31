from collections import deque

def max_flow(G, s, t):
    n = len(G)
    parent = [None for _ in range(n)]

    def bfs(G, s, t, parent):
        nonlocal n
        visited = [False for _ in range(n)]
        queue = deque()

        queue.append(s)
        while queue and not visited[t]:
            u = queue.popleft()
            visited[u] = True
            for v in range(n):
                if G[u][v] > 0 and not visited[v]:
                    parent[v] = u
                    queue.append(v)

        return visited[t]

    max_flow_value = 0
    while bfs(G, s, t, parent):
        curr_flow = float('inf')
        temp = t
        while temp != s:
            curr_flow = min(curr_flow, G[parent[temp], temp])
            temp = parent[temp]

        max_flow_value += curr_flow

        temp = t
        while temp != s:
            G[parent[temp]][temp] -= curr_flow
            G[temp][parent[temp]] += curr_flow
            temp = parent[temp]

    return max_flow_value