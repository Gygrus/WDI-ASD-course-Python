"""
W pewnym państwie, w którym znajduje się N miast, postanowiono połączyć wszystkie miasta siecią autostrad, tak aby możliwe było dotarcie autostradą do każdego miasta. Ponieważ kontynent, na
którym leży państwo jest płaski położenie każdego z miast opisują dwie liczby x, y, a odległość w linii
prostej pomiędzy miastami liczona w kilometrach wyraża się wzorem len =
√
(x1 − x2)
2 + (y1 − y2)
2.
Z uwagi na oszczędności materiałów autostrada łączy dwa miasta w linii prostej.
Ponieważ zbliżają się wybory prezydenta, wszystkie autostrady zaczęto budować równocześnie
i jako cel postanowiono zminimalizować czas pomiędzy otwarciem pierwszej i ostatniej autostrady.
Czas budowy autostrady wyrażony w dniach wynosi ⌈len⌉ (sufit z długości autostrady wyrażonej
w km).
Proszę zaimplementować funkcję highway(A), która dla danych położeń miast wyznacza minimalną liczbę dni dzielącą otwarcie pierwszej i ostatniej autostrady
"""
from math import ceil
class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self

def get_distance(x, y):
    return ceil(((x[0]-y[0])**2 + (x[1]-y[1])**2)**(1/2))

def highway(A):
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

    def kruskal(graph, a, b):
        n = len(graph)
        available = [True] * n
        set_of_edges = []
        for x in range(n):
            for e in range(x+1, n):
                if x != a or e != b:
                    set_of_edges.append([x, e, graph[x][e]])


        set_of_edges.sort(key=lambda x: abs(x[2]-graph[a][b]))
        A = []
        list_of_nodes = [Node(i) for i in range(n)]
        union(list_of_nodes[a], list_of_nodes[b])
        A.append((a, b))
        for x in set_of_edges:
            if union(list_of_nodes[x[0]], list_of_nodes[x[1]]):
                A.append((x[0], x[1]))

        print(A)
        min = float('inf')
        max = 0
        for x in range(len(A)):
            if graph[A[x][0]][A[x][1]] < min:
                min = graph[A[x][0]][A[x][1]]
            if graph[A[x][0]][A[x][1]] > max:
                max = graph[A[x][0]][A[x][1]]

        return max-min

    n = len(A)
    tab = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            tab[x][y] = get_distance(A[x], A[y])

    best = float('inf')
    for x in range(n):
        for y in range(x+1, n):
            best = min(best, kruskal(tab, x, y))
    for x in tab:
        print(x)

    return best

A = [(10,10),(15,25),(20,20),(30,40)]
print(highway(A))