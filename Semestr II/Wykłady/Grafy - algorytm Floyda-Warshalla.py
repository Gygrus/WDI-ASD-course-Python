
# zakładam, że tam gdzie pomiędzy i a j nie ma krawędzi, to G[i][j] = False
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

    for x in S:
        print(x)

    print()
    for y in P:
        print(y)

    # # odtwarzanie ścieżki dla ścieżki od s do t
    # s = 2
    # t = 1
    # output = []
    # idx = t
    # while P[s][idx] != None:
    #     output.append(idx)
    #     idx = P[s][idx]
    #
    # output.append(s)
    # print(output[::-1])



G = [[False, 1, False, False, 4],
     [False, False, 4, False, -1],
     [False, False, False, -2, False],
     [-3, 5, False, False, False],
     [False, False, False, False, False]]

floyd_warshall(G)