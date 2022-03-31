class Node():
    def __init__(self):
        self.d = 0
        self.parent = None
        self.neighbours = []
        self.visited = False

def top_sort(G):
    def DFSVisit(G, u):
        nonlocal time
        u.visited = True
        for v in u.neighbours:
            if not G[v].visited:
                G[v].parent = u
                DFSVisit(G, G[v])

        output.append(u.d)

    output = []
    n = len(G)
    for v in range(n):
        G[v].parent = None
        G[v].visited = False
        G[v].d = v

    time = 0
    for u in range(n):
        if not G[u].visited:
            DFSVisit(G, G[u])

    print(output)


# G = [[1, 2],
#          [2, 4],
#          [],
#          [],
#          [3, 5, 6],
#          [],
#          []]
A = Node()
A.neighbours = [1, 2]
B = Node()
B.neighbours = [2, 4]
C = Node()
D = Node()
E = Node()
E.neighbours = [3, 5, 6]
F = Node()
H = Node()
G =[A, B, C, D, E, F, H]
top_sort(G)