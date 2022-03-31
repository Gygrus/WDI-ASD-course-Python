"""
[2pkt.] Zadanie 1. Proszę zaimplementować funkcję heavy path(T), która na wejściu otrzymuje drzewo T z
ważonymi krawędziami (wagi to liczby całkowite—mogą być zarówno dodatnie, ujemne, jak i o wartości zero)
i zwraca długość (wagę) najdłuższej ścieżki prostej w
tym drzewie. Drzewo reprezentowane jest za pomocą obiektów typu Node:
class Node:
def __init__( self ):
self.children = 0 # liczba dzieci węzła
self.child = [] # lista par (dziecko, waga krawędzi)
... # wolno dopisać własne pola
Poniższy kod tworzy drzewo z korzeniem A, który ma dwoje dzieci, węzły B i C, do których
prowadzą krawędzie o wagach 5 i −1:
A = Node()
B = Node()
C = Node()
A.children = 2
A.child = [ (B,5), (C,-1) ]
Rozwiązaniem dla drzewa A jest 5 (osiągnięte przez ścieżkę A-B; ścieżka B-A-C ma wagę
5 − 1 = 4. Proszę skrótowo wyjaśnić ideę algorytmu oraz oszacować jego złożoność czasową.
"""
"""
Przechodząc zmodyfikowanym DFSem z drzewa T znajduję wierzchołek, na którym kończy się najdłuższa ścieżka 
która potencjalnie może kończyć się w T. Następnie znowu za pomocą algorytmu DFS przechodzę przez drzewo, poszukując
najdłuższej możliwej ścieżki od znalezionego wierzchołka."""
class Node:
    def __init__(self):
        self.children = 0
        self.child = []
        self.visited = 0
        self.parent = []


def heavy_path(T):
    max_weight = -999999
    rem = []
    def dfs(u, weight, cur_sum):
        print("lalala")
        nonlocal max_weight, rem
        if cur_sum > weight:
            weight = cur_sum
        if weight > max_weight:
            max_weight = weight
            rem = [u]

        elif weight == max_weight:
            rem.append(u)

        u.visited = 1
        for v in u.child:
            v[0].parent.append((u, v[1]))
            if not v[0].visited:
                dfs(v[0], weight + v[1], v[1])

    def dfs_second(u, weight):
        nonlocal max_weight, rem
        if weight > max_weight:
            # print(weight, max_weight)
            max_weight = weight

        u.visited = 0
        # print(u.parent)
        for v in u.parent:
            if v[0].visited:
                dfs_second(v[0], weight + v[1])

        for v in u.child:
            if v[0].visited:
                dfs_second(v[0], weight + v[1])
        u.visited = 1

    dfs(T, -99999999, -9999999)
    print(max_weight)
    for x in rem:
        print(x.parent, x.child)
    max_weight = -99999
    for x in rem:
        dfs_second(x, 0)

    print(max_weight)


# A = Node()
# B = Node()
# C = Node()
# D = Node()
# E = Node()
# F = Node()
# A.children = 2
# A.child = [ (B,5), (C,-1) ]
# B.children = 2
# B.child = [(D, -2), (E, -3)]
# E.children = 1
# E.child = [(F, 4)]
# heavy_path(A)
v0 = Node()
v1 = Node()
v2 = Node()
v3 = Node()
v4 = Node()
v5 = Node()
v0.children = 2
v0.child = [(v1, 2), (v2, -1)]
v2.children = 2
v2.child = [(v3, 3), (v4, 2)]
v1.children = 1
v1.child = [(v5, 3)]
heavy_path(v0)
