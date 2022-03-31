"""
Dany jest graf nieskierowany G = (V,E) z ważonymi krawędziami (w: E -> N).
Proszę zaproponować jak najszybszy algorytm, który znajduje ścieżkę z
danego wierzchołka s do danego wierzchołka t taką, że:
    Każda kolejne krawędź ma mniejszą wagę niż poprzednia
    Spośród ścieżek spełniających powyższy warunek, znaleziona ma najmniejszą sumę wag
"""
from queue import PriorityQueue
def find_path(G, s, t):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    distance = [float('inf')]*n
    edge = [float('inf')]*n
    dist_edge = [[] for _ in range(n)]
    # left = [0]*n
    # distance[t] = 0
    # edge[t] = -1
    dist_edge[t].append([0, None, -1])
    # for x in range(n):
    #     for i in range(n):
    #         if G[x][i] > 0:
    #             left[x] += 1

    q = PriorityQueue()
    q.put((dist_edge[t][0][0], t, dist_edge[t][0][2]))
    # check = True
    while not q.empty():
        # print(parent)
        print(distance)
        dist, u, edge = q.get()
        print(dist, u)
        visited[u] = True
        for v in range(n):
            if G[u][v] > 0 and G[u][v] > edge and not visited[v]:
                # edge[v] = G[u][v]
                # distance[v] = G[u][v] + distance[u]
                # parent[v] = u
                dist_edge[v].append([G[u][v] + dist, u, G[u][v]])
                q.put((G[u][v] + dist, v, G[u][v]))

            elif G[u][v] > 0 and G[u][v] > edge and visited[v]:
                check = True
                for x, y, z in dist_edge[v]:
                    if z < edge:
                        check = False
                        break

                if check:
                    # edge[v] = G[u][v]
                    # distance[v] = G[u][v] + distance[u]
                    dist_edge[v].append([G[u][v] + dist, u, G[u][v]])
                    q.put((G[u][v] + dist, v, G[u][v]))

    print(distance)
    output = []
    idx = s
    min = float('inf')
    save = None
    for dist, vertex, edge in dist_edge[idx]:
        if dist < min:
            min = dist
            save = [dist, vertex, edge]
    output.append(idx)
    idx = save[1]
    temp = None
    while idx != t:
        output.append(idx)
        for dist, vertex, edge in dist_edge[idx]:
            if save[0] - save[2] == dist:
                save = [dist, vertex, edge]
                break
        idx = save[1]

    output.append(idx)
    # print(parent)
    # idx = s
    # while idx != t:
    #     output.append(idx)
    #     idx = parent[idx]
    #
    # output.append(t)

    return output, min

# G = [[-1, 1, -1, -1, -1, 6, -1],
#      [1, -1, 2, -1, -1, -1, -1],
#      [-1, 2, -1, 3, -1, -1, -1],
#      [-1, -1, 3, -1, 4, -1, -1],
#      [-1, -1, -1, 4, -1, 5, -1],
#      [6, -1, -1, -1, 5, -1, 7],
#      [-1, -1, -1, -1, -1, 7, -1]]

# G = [[-1, 1, -1, -1, -1, 7, -1, -1],
#      [1, -1, 2, -1, -1, -1, -1, -1],
#      [-1, 2, -1, 3, -1, -1, -1, -1],
#      [-1, -1, 3, -1, 4, -1, -1, -1],
#      [-1, -1, -1, 4, -1, -1, -1, 5],
#      [7, -1, -1, -1, -1, -1, 7, 6],
#      [-1, -1, -1, -1, -1, 7, -1, -1],
#      [-1, -1, -1, -1, 5, 6, -1, -1]]

# G = [[-1, 4, -1, -1, -1, -1, -1, 8, -1], [4, -1, 8, -1, -1, -1, -1, 11, -1], [-1, 8, -1, 1, -1, -1, -1, -1, 2],
#      [-1, -1, 1, -1, 1, 14, -1, -1, -1], [-1, -1, -1, 1, -1, 2, -1, -1, -1], [-1, -1, -1, 14, 2, -1, 3, -1, -1],
#      [-1, -1, -1, -1, -1, 3, -1, 1, 6], [8, 11, -1, -1, -1, -1, 1, -1, 7], [-1, -1, 2, -1, -1, -1, 6, 7, -1]]

# G = [[-1, 1, -1, -1, 5, -1, -1, -1],
#      [1, -1, 2, -1, -1, -1, -1, -1],
#      [-1, 2, -1, 3, -1, -1, -1, -1],
#      [1, -1, 3, -1, 4, -1, -1, -1],
#      [5, -1, -1, 4, -1, 6, -1, -1],
#      [-1, -1, -1, -1, 6, -1, 7, -1],
#      [-1, -1, -1, -1, -1, 7, -1, 8],
#      [-1, -1, -1, -1, -1, -1, 8, -1]]
G = [[-1, 10, -1,  4],
     [10, -1, 10,  3],
     [-1, 10, -1, -1],
     [4,  3,  -1, -1]]


print(find_path(G, 0, 2))