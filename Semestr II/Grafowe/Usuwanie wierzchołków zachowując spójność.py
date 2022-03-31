from random import shuffle

def dfs_deletion(graph):
    visited = [False] * len(graph)
    result = []

    def dfs_visit(u):
        print(u)
        nonlocal graph, visited, result

        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs_visit(v)

        result.append(u)

    dfs_visit(0)
    for x in range(len(result)):
        print(result[x], end=' ')

graph = [[1, 4], [0, 2], [3, 4], [5, 6], [2, 0, 7], [3, 6], [5, 3], [4]]
a = [1, 4]
b = [0, 2]
c = [3, 4, 1]
d = [5, 6, 2]
e = [2, 0, 7]
f = [3, 6]
g = [5, 3]
h = [4]
shuffle(a)
shuffle(b)
shuffle(c)
shuffle(d)
shuffle(e)
shuffle(f)
shuffle(g)
shuffle(h)
graph = [a, b, c, d, e, f, g, h]
G1 = [
    [1, 2, 3],
    [0],
    [0, 3, 4],
    [0, 2, 4],
    [2, 3]
]
dfs_deletion(graph)