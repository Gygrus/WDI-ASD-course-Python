def euler(graph):
    n = len(graph)
    for x in range(n):
        sum = 0
        for y in range(n):
            sum += graph[x][y]

        if sum%2:
            return None

    pointers = [0] * len(graph)
    stack = []
    result = []
    sum = 0
    def dfs_visit(u):
        nonlocal graph, pointers, stack, result, n, sum
        stack.append(u)
        while pointers[u] <= n-1:
            sum += 1
            pointers[u] += 1
            if graph[u][pointers[u]-1]:
                graph[u][pointers[u]-1] *= -1
                graph[pointers[u]-1][u] *= -1
                dfs_visit(pointers[u]-1)

        result.append(stack.pop())

    dfs_visit(0)
    for x in range(n):
        for y in range(n):
            graph[x][y] *= -1

    if sum == n**2:
        return result

    return None

G = [[0,1,1,0,0,0,0,0,0],
     [1,0,1,1,0,1,1,0,1],
     [1,1,0,0,1,1,0,1,1],
     [0,1,0,0,0,1,0,0,0],
     [0,0,1,0,0,1,1,1,0],
     [0,1,1,1,1,0,0,0,0],
     [0,1,0,0,1,0,0,1,1],
     [0,0,1,0,1,0,1,0,1],
     [0,1,1,0,0,0,1,1,0]]
G1 = [[0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],                                                                                                                                               [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],                                                                                                                                                    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],                                                                                                                                                    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],                                                                                                                                                    [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],                                                                                                                                                    [0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],                                                                                                                                                    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],                                                                                                                                                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0],                                                                                                                                                    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1],                                                                                                                                                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],                                                                                                                                                    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],                                                                                                                                                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],                                                                                                                                                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],                                                                                                                                                    [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],                                                                                                                                                    [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],                                                                                                                                                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],                                                                                                                                                    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],                                                                                                                                                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0],                                                                                                                                                    [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],                                                                                                                                                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]
n = 38
G2 = [[1 for _ in range(n)] for _ in range(n)]
for x in range(n):
    G2[x][x] = 0

print(euler(G))
