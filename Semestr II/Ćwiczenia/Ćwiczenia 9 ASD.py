"""Zadanie 1"""


def Hamilton(G):
   n = len(G)
   visited = [False for _ in range(n)]
   res = []
   def DFS_Visit(v):
       nonlocal G
       nonlocal visited
       nonlocal res
       visited[v] = True
       for u in G[v]:
           if not visited[u]:
               DFS_Visit(u)
       res.append(v)
   # [3, 2, 0, 1]
   for i in range(n-1):
       for u in G[res[i]]:
           if u == res[i+1]:
               break
       else:
           return False
   return True

"""Zadanie 2"""
# zadanie 2 (dobry początek)

# lista sąsiedztwa (graf skierowany, bez wag)
class Graph:
    def __init__(self):
        self.graph = [] * 0
        self.vertices = 0

    def addVertex(self):
        self.graph.append([])
        self.vertices += 1

    def addEdge(self, u, v):
        self.graph[u].append(v)


def reverseEdges(graph):
    revgraph = [] * 0
    for i in range(graph.vertices):
        revgraph.append([])
    for vertex in range(graph.vertices):
        for i in graph.graph[vertex]:
            revgraph[i].append(vertex)
    return revgraph


# silnie spójne składowe (zwraca pierwszy z wierzchołków w "najwyższej" silnie spójnej składowej
def sss(G):
    visited = [False] * G.vertices
    entry = [-1] * G.vertices
    process = [-1] * G.vertices
    time = [0] * 1
    processed = [-1] * G.vertices
    n = [G.vertices] * 1
    sss = [] * 0

    #########################
    def DFSVisit(GG, u, helpvariable, tab):
        time[0] += 1
        visited[u] = True
        entry[u] = time[0]
        for v in GG[u]:
            if not visited[v]:
                DFSVisit(GG, v, helpvariable, tab)
        time[0] += 1
        process[u] = time[0]
        if helpvariable:
            n[0] -= 1
            processed[n[0]] = u
        else:
            tab.append(u)

    #########################

    for v in range(G.vertices):  # DFS
        if not visited[v]: DFSVisit(G.graph, v, True, None)

    #########################
    graph = reverseEdges(G)  # odwracanie krawędzi
    for v in range(G.vertices):  # restart
        visited[v] = False
        entry[v] = -1
        process[v] = -1
    #########################

    for v in processed:  # DFS malejąco
        if not visited[v]:
            sss.append([])
            DFSVisit(graph, v, False, sss[len(sss) - 1])
    return sss


##########################################


# Dane
G = Graph()
for i in range(11): G.addVertex()
G.addEdge(1, 0)
G.addEdge(0, 2)
G.addEdge(2, 1)
G.addEdge(0, 3)
G.addEdge(1, 9)
G.addEdge(7, 9)
G.addEdge(8, 7)
G.addEdge(10, 8)
G.addEdge(9, 10)
G.addEdge(10, 6)
G.addEdge(7, 4)
G.addEdge(4, 6)
G.addEdge(6, 5)
G.addEdge(5, 4)
G.addEdge(4, 3)
G.addEdge(3, 5)

print(sss(G))
##########################################

# zadanie 2 (dobry koniec)