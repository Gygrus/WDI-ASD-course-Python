"""
Zadanie 1. (DFS/BFS) Proszę zaimplementować następujące algorytmy:
1. Sprawdzanie czy graf jest dwudzielny (czyli zauważyć, że to 2-kolorowanie i użyć DFS lub BFS).
2. Policzyć liczbę spójnych składowych w grafie (implementacja przeciwna do tej z poprzedniego zadania)
"""

"""2"""

class Node:
	def __init__(self):
		self.visited = False
		self.next = []

def add_edge(G, u,v):
	G[u].next.append(G[v])
	G[v].next.append(G[u])

def connected_components(G):
	res = 0

	def DFS_visit(v):
		v.visited = True
		for u in v.next:
			if not u.visited:
				DFS_visit(u)

	for v in G:
		if not v.visited:
			DFS_visit(v)
			res += 1

	return res



# if __name__ == '__main__':
# 	G = [Node() for _ in range(6)]
# 	add_edge(G, 0, 1)
# 	add_edge(G, 0, 2)
# 	# add_edge(G, 2, 1)
# 	# add_edge(G, 3, 4)
#
# 	print(connected_components(G))


"""1"""

from queue import Queue


def bfs(V, s):
    n = len(V)
    Q = Queue()
    D = [-1] * n
    Q.put(s)

    D[s] = 1

    while not Q.empty():
        q = Q.get()
        for i in range(n):
            if D[i] == D[q] and M[q][i] == 1:
                return False
            if D[i] == -1 and M[q][i] == 1:
                D[i] = (D[q] + 1) % 2
                Q.put(i)

    return True


def dwudzielny(V):
    n = len(V)
    x = bfs(V, 0)
    if x:
        print("tak")
    else:
        print("nie")
    return 0


M = [[0, 1, 0, 0, 0, 0],
     [1, 0, 0, 1, 1, 0],
     [0, 0, 0, 1, 0, 1],
     [0, 1, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 1, 0]]

# dwudzielny(M)



"""
Zadanie 3. (BFS i najkrótsze ścieżki) Proszę zaimplementować algorytm BFS tak, żeby znajdował
najkrótsze ścieżki w grafie i następnie, żeby dało się wypisać najkrotszą ścieżkę z zadanego punktu startowego
do wskazanego wierzchołka
"""
from queue import Queue
# zakładam że graf jest nieskierowany, nieważony
def BFS(G, s, e):
    n = len(G)
    visited = [False]*n
    result = [None]*n
    visited[s] = True
    Q = Queue()
    Q.put([s, 0, 0])
    output = []
    distance = 0
    while not Q.empty():
        u = Q.get()
        print(u)
        print('gónwo')
        result[u[0]] = (u[1], u[2])
        if u[0] == e:
            distance = result[u[0]][0]
            k = result[u[0]][1]
            i = u[0]
            while k != i:
                output.append(k)
                i = k
                k = result[k][1]
            break

        for v in G[u[0]]:
            if not visited[v]:
                visited[v] = True
                Q.put([v, u[1]+1, u[0]])


    return output, distance

# G = [[1, 4], [0, 4], [4, 7, 3], [2], [0, 1, 2, 7, 6, 5], [4, 6], [5, 4, 7], [6, 4, 2]]
# print(BFS(G, 0, 3))

"""
Zadanie 6. (bezpieczny przelot) Dany jest graf G = (V, E), którego wierzchołki reprezentują punkty
nawigacyjne nad Bajtocją, a krawędzie reprezentują korytarze powietrzne między tymi punktami. Każdy
korytarz powietrzny ei ∈ E powiązany jest z optymalnym pułapem przelotu pi ∈ N (wyrażonym w metrach).
Przepisy dopuszczają przelot danym korytarzem jeśli pułap samolotu różni się od optymalnego najwyżej o t
metrów. Proszę zaproponować algorytm (bez implementacji), który sprawdza czy istnieje możliwość przelotu
z zadanego punktu x ∈ V do zadanego punktu y ∈ V w taki sposób, żeby samolot nigdy nie zmieniał pułapu.
Algorytm powinien być poprawny i możliwie jak najszybszy. Proszę oszacować jego złożoność czasową.
"""

"""Było na bitalgo czwartek 11:15"""

"""
Zadanie 1. (kapitan statku, zadanie z kolokwium w 2012/13) Kapitan pewnego statku zastanawia
się, czy może wpłynąć do portu mimo, że nastąpił odpływ. Do dyspozycji ma mapę zatoki w postaci tablicy
M, gdzie M[y][x] to głebokość zatoki na pozycji (x, y). Jeśli jest ona większa niż pewna wartość int T
to statek może się tam znaleźć. Początkowo statek jest na pozycji (0, 0) a port znajduje się na pozycji
(n − 1, m − 1). Z danej pozycji statek może przepłynąć bezpośrednio jedynie na pozycję bezpośrednio obok
(to znaczy, na pozycję, której dokładnie jedna ze współrzędnych różni się o jeden). Proszę napisać funkcję
rozwiązującą problem kapitana.
"""


def Captain_docks(G, T):
    n = len(G)
    m = len(G[0])
    queue = Queue()
    visited = [[False for _ in range(m)] for _ in range(n)]
    s = [0, 0]
    queue.put(s)
    visited[s[0]][s[1]] = True

    while not queue.empty():
        u = queue.get()
        if u[0] > 0:
            if not visited[u[0]-1][u[1]] and G[u[0]-1][u[1]] > T:
                visited[u[0] - 1][u[1]] = True
                queue.put([u[0]-1, u[1]])

        if u[0] < n-1:
            if not visited[u[0]+1][u[1]] and G[u[0]+1][u[1]] > T:
                visited[u[0] + 1][u[1]] = True
                queue.put([u[0]+1, u[1]])

        if u[1] > 0:
            if not visited[u[0]][u[1]-1] and G[u[0]][u[1]-1] > T:
                visited[u[0]][u[1]-1] = True
                queue.put([u[0], u[1]-1])

        if u[1] < m-1:
            if not visited[u[0]][u[1] + 1] and G[u[0]][u[1]+1] > T:
                visited[u[0]][u[1]+1] = True
                queue.put([u[0], u[1]+1])

    for x in visited:
        print(x)
    return visited[n-1][m-1]


G = [[1, 4, 6, 7],
     [3, 2, 2, 5],
     [2, 7, 2, 4],
     [2, 2, 2, 4],
     [6, 3, 4, 8]]
T = 3
print(Captain_docks(G, T))
