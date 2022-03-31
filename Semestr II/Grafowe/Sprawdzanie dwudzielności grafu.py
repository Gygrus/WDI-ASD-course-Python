from queue import Queue



def check_if_bipartite(graph):
    visited = [False] * len(graph)
    n = len(graph)
    check = False
    def bfs(graph, s):
        queue = Queue()
        nonlocal visited, check
        colors = [0] * len(graph)
        queue.put(s)
        colors[s] = 1

        while not queue.empty():
            u = queue.get()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    colors[v] = colors[u] * (-1)
                    queue.put(v)

                else:
                    if colors[v] == colors[u]:
                        check = True
                        return


    for x in range(n):
        if not visited[x]:
            visited[x] = True
            bfs(graph, x)

    if check:
        return False

    return True




pom = [[3], [3, 6], [3, 4, 5], [0, 1, 2], [2], [2], [1, 4]]

print(check_if_bipartite(pom))