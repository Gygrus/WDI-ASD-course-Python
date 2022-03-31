# Piotr Socała

"""
Robot porusza się po dwuwymiarowym labiryncie i ma dotrzeć z pocycji A = (xa, ya) na pozycję
B = (xb, yb). Robot może wykonać następujące ruchy:
1. ruch do przodu na kolejne pole,
2. obrót o 90 stopni zgodnie z ruchem wskazówek zegara,
3. obrót o 90 stopni przeciwnie do ruchów wskazówek zegara.
Obrót zajmuje robotowi 45 sekund. W trakcie ruchu do przodu robot się rozpędza i pokonanie
pierwszego pola zajmuje 60 sekund, pokonanie drugiego 40 sekund, a kolejnych po 30 sekund na
pole. Wykonanie obrotu zatrzymuje robota i następujące po nim ruchy do przodu ponownie go
rozpędzają. Proszę zaimplementować funkcję:
def robot( L, A, B):
...
która oblicza ile minimalnie sekund robot potrzebuje na dotarcie z punktu A do punktu B (lub
zwraca None jeśli jest to niemożliwe).
Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową
użytego algorytmu.
Labirynt. Labirynt reprezentowany jest przez tablicę w wierszy, z których każdy jest napisem
składającym się z k kolumn. Pusty znak oznacza pole po którym robot może się poruszać, a znak
’X’ oznacza ścianę labiryntu. Labirynt zawsze otoczony jest ścianami i nie da się opuścić planszy.
Pozycja robota. Początkowo robot znajduje się na pozycji A = (xa, ya) i jest obrócony w prawo
(tj. znajduje się w wierszu ya i kolumnie xa, skierowany w stronę rosnących numerów kolumn).
Przykład. Rozważmy labirynt skłądający się z 5 wierszy i 10 kolumn:
# 0123456789
L = [ "XXXXXXXXXX", # 0
"X X X", # 1
"X XXXXXX X", # 2
"X X", # 3
"XXXXXXXXXX", # 4
"""

"""
Zmodyfikowana Djikstra, w której dla każdego pola w które mogę wejść """

def robot(L, A, B):
    def dijkstra_matrix(G, s):
        n = len(G)
        k = len(G[0])
        print(n, k)
        dist = [[[[float('inf') for _ in range(4)] for _ in range(3)] for _ in range(k)] for _ in range(n)]
        visited = [[[[False for _ in range(4)] for _ in range(3)] for _ in range(k)] for _ in range(n)]
        dist[s[1]][s[0]][0][0] = 0
        for _ in range(n*k*12):
            minim = float('inf')
            for x in range(n):
                for y in range(k):
                    for move in range(3):
                        for pos in range(4):
                            if dist[x][y][move][pos] < minim and not visited[x][y][move][pos]:
                                rem_x = x
                                rem_y = y
                                rem_move = move
                                rem_pos = pos
                                minim = dist[x][y][move][pos]

            visited[rem_x][rem_y][rem_move][rem_pos] = True
            # print(rem_x, rem_y, rem_move, rem_pos)
            # print(visited[rem_x][rem_y][0][int((rem_pos+1)%4)])
            if not visited[rem_x][rem_y][0][int((rem_pos+1)%4)] and dist[rem_x][rem_y][0][int((rem_pos+1)%4)] > dist[rem_x][rem_y][rem_move][rem_pos] + 45:
                # print('gówno')
                dist[rem_x][rem_y][0][int((rem_pos+1)%4)] = dist[rem_x][rem_y][rem_move][rem_pos] + 45

            if not visited[rem_x][rem_y][0][int((rem_pos-1)%4)] and dist[rem_x][rem_y][0][int((rem_pos-1)%4)] > dist[rem_x][rem_y][rem_move][rem_pos] + 45:
                dist[rem_x][rem_y][0][int((rem_pos-1)%4)] = dist[rem_x][rem_y][rem_move][rem_pos] + 45

            if rem_move == 0:
                if rem_pos == 0:
                    if G[rem_x][rem_y+1] != "X":
                        if not visited[rem_x][rem_y+1][1][rem_pos] and dist[rem_x][rem_y+1][1][rem_pos] > dist[rem_x][rem_y][rem_move][rem_pos] + 60:
                            dist[rem_x][rem_y + 1][1][rem_pos] = dist[rem_x][rem_y][rem_move][rem_pos] + 60

                elif rem_pos == 1:
                    # print(G[rem_x+1][rem_y], 'gónwo')
                    if G[rem_x+1][rem_y] != "X":
                        if not visited[rem_x+1][rem_y][1][rem_pos] and dist[rem_x+1][rem_y][1][rem_pos] > dist[rem_x][rem_y][rem_move][rem_pos] + 60:
                            dist[rem_x + 1][rem_y][1][rem_pos] = dist[rem_x][rem_y][rem_move][rem_pos] + 60

                elif rem_pos == 2:
                    if G[rem_x][rem_y-1] != "X":
                        if not visited[rem_x][rem_y-1][1][rem_pos] and dist[rem_x][rem_y-1][1][rem_pos] > dist[rem_x][rem_y][rem_move][rem_pos] + 60:
                            dist[rem_x][rem_y - 1][1][rem_pos] = dist[rem_x][rem_y][rem_move][rem_pos] + 60

                elif rem_pos == 3:
                    if G[rem_x-1][rem_y] != "X":
                        if not visited[rem_x-1][rem_y][1][rem_pos] and dist[rem_x-1][rem_y][1][rem_pos] > dist[rem_x][rem_y][rem_move][rem_pos] + 60:
                            dist[rem_x-1][rem_y][1][rem_pos] = dist[rem_x][rem_y][rem_move][rem_pos] + 60

            elif rem_move == 1:
                if rem_pos == 0:
                    if G[rem_x][rem_y+1] != "X":
                        if not visited[rem_x][rem_y+1][2][rem_pos] and dist[rem_x][rem_y+1][2][rem_pos] > dist[rem_x][rem_y][rem_move][rem_pos] + 40:
                            dist[rem_x][rem_y + 1][2][rem_pos] = dist[rem_x][rem_y][rem_move][rem_pos] + 40

                elif rem_pos == 1:
                    if G[rem_x+1][rem_y] != "X":
                        if not visited[rem_x+1][rem_y][2][rem_pos] and dist[rem_x+1][rem_y][2][rem_pos] > dist[rem_x][rem_y][rem_move][rem_pos] + 40:
                            dist[rem_x + 1][rem_y][2][rem_pos] = dist[rem_x][rem_y][rem_move][rem_pos] + 40

                elif rem_pos == 2:
                    if G[rem_x][rem_y-1] != "X":
                        if not visited[rem_x][rem_y-1][2][rem_pos] and dist[rem_x][rem_y-1][2][rem_pos] > dist[rem_x][rem_y][rem_move][rem_pos] + 40:
                            dist[rem_x][rem_y - 1][2][rem_pos] = dist[rem_x][rem_y][rem_move][rem_pos] + 40

                elif rem_pos == 3:
                    if G[rem_x-1][rem_y] != "X":
                        if not visited[rem_x-1][rem_y][2][rem_pos] and dist[rem_x-1][rem_y][2][rem_pos] > dist[rem_x][rem_y][rem_move][rem_pos] + 40:
                            dist[rem_x-1][rem_y][2][rem_pos] = dist[rem_x][rem_y][rem_move][rem_pos] + 40

            else:
                if rem_pos == 0:
                    if G[rem_x][rem_y+1] != "X":
                        if not visited[rem_x][rem_y+1][2][rem_pos] and dist[rem_x][rem_y+1][2][rem_pos] > dist[rem_x][rem_y][rem_move][rem_pos] + 30:
                            dist[rem_x][rem_y + 1][2][rem_pos] = dist[rem_x][rem_y][rem_move][rem_pos] + 30

                elif rem_pos == 1:
                    if G[rem_x+1][rem_y] != "X":
                        if not visited[rem_x+1][rem_y][2][rem_pos] and dist[rem_x+1][rem_y][2][rem_pos] > dist[rem_x][rem_y][rem_move][rem_pos] + 30:
                            dist[rem_x + 1][rem_y][2][rem_pos] = dist[rem_x][rem_y][rem_move][rem_pos] + 30

                elif rem_pos == 2:
                    if G[rem_x][rem_y-1] != "X":
                        if not visited[rem_x][rem_y-1][2][rem_pos] and dist[rem_x][rem_y-1][2][rem_pos] > dist[rem_x][rem_y][rem_move][rem_pos] + 30:
                            dist[rem_x][rem_y - 1][2][rem_pos] = dist[rem_x][rem_y][rem_move][rem_pos] + 30

                elif rem_pos == 3:
                    if G[rem_x-1][rem_y] != "X":
                        if not visited[rem_x-1][rem_y][2][rem_pos] and dist[rem_x-1][rem_y][2][rem_pos] > dist[rem_x][rem_y][rem_move][rem_pos] + 30:
                            dist[rem_x-1][rem_y][2][rem_pos] = dist[rem_x][rem_y][rem_move][rem_pos] + 30

        return dist

    distances = dijkstra_matrix(L, A)
    # for x in range(len(L)):
    #     for y in range(len(L[0])):
    #         print("x =", x, "y =", y, distances[x][y])

    # print(distances[1][3])

    best = float('inf')
    for x in range(3):
        for y in range(4):
            best = min(best, distances[B[1]][B[0]][x][y])


    if best == float('inf'):
        return None

    return best




L =["XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                                      X",
"X                                      X",
"XXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                                      X",
"X                                      X",
"XXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX XX",
"X                                      X",
"X                                      X",
"XXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                                      X",
"X                                      X",
"X        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                                      X",
"X                                      X",
"X                                      X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   X",
"X                                      X",
"X                                      X",
"X                                      X",
"X                                      X",
"X                                      X",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                                      X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   X",
"X                                      X",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                                      X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"]
A = (1, 27)
B = (38, 1)
print(robot(L, A, B))

