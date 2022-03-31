def SSS(G):
    n = len(G)
    stack = []
    tab_of_comp = [0] * n
    def dfs_first(graph, stack):
        n = len(graph)
        visited = [False] * n
        parent = [None] * n

        def dfs_visit_1(u):
            nonlocal graph, visited, parent, stack
            visited[u] = True
            for v in graph[u]:
                if not visited[v]:
                    parent[v] = u
                    dfs_visit_1(v)

            stack.append(u)

        for v in range(n):
            if not visited[v]:
                dfs_visit_1(v)


    def dfs_second(graph, stack, tab_of_comp):
        n = len(graph)
        visited = [False] * n
        parent = [None] * n
        reverse_graph = [[0 for _ in range(n)] for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if graph[x][y] == 1 and not graph[y][x] == 1:
                    reverse_graph[x][y] = 0
                    reverse_graph[y][x] = 1


        # to jest stricte do zadania z codeforces, gdzie chce zapamiętać tylko składowe z co najmniej dwoma wierzchołkami
        def dfs_visit_2(u):
            nonlocal reverse_graph, visited, time, parent, tab_of_comp
            time += 1
            visited[u] = True
            for v in graph[u]:
                if not visited[v]:
                    parent[v] = u
                    dfs_visit_2(v)

            if time > 1:
                tab_of_comp[u] = 1

        while stack:
            s = stack.pop()
            time = 0
            if not visited[s]:
                dfs_visit_2(s)

    dfs_first(G, stack)
    dfs_second(G, stack, tab_of_comp)
    return tab_of_comp
