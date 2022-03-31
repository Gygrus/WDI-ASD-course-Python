class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)

    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: return False

    if x.rank > y.rank:
        y.parent = x

    else:
        x.parent = y
        if x.rank == y.rank: y.rank += 1

    return True

def kruskal(graph):
    n = len(graph)
    available = [True]*n
    set_of_edges = []
    for x in range(n):
        for e in range(len(graph[x])):
            if available[graph[x][e][0]]:
                set_of_edges.append([x, graph[x][e][0], graph[x][e][1]])

        available[x] = False

    set_of_edges.sort(key = lambda x: x[2])
    A = []
    list_of_nodes = [Node(i) for i in range(n)]
    for x in set_of_edges:
        if union(list_of_nodes[x[0]], list_of_nodes[x[1]]):
            A.append((x[0], x[1]))

    print(A)



graph = [[[1, 7], [2, 2], [3, 8], [5, 3]],
         [[0, 7], [3, 1]],
         [[0, 2], [4, 5]],
         [[1, 1], [0, 8], [4, 4], [5, 12]],
         [[3, 4], [2, 5], [5, 6]],
         [[3, 12], [0, 3], [4, 6]]]
kruskal(graph)

