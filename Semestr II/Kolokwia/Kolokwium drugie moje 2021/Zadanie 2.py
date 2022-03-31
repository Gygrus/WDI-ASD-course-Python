#Piotr Socała

"""
Dany jest graf nieskierowany G = (V, E) oraz dwa wierzchołki s, t ∈ V . Proszę zaproponować i
zaimplementować algorytm, który sprawdza, czy istnieje taka krawędź {p, q} ∈ E, której usunięcie
z E spowoduje wydłużenie najkrótszej ścieżki między s a t (usuwamy tylko jedną krawędź). Algorytm powinien być jak najszybszy i używać jak najmniej pamięci. Proszę skrótowo uzasadnić jego
poprawność i oszacować złożoność obliczeniową.
Algorytm należy zaimplementować jako funkcję:
def enlarge(G, s, t):
...
która przyjmuje graf G oraz numery wierzchołków s, t i zwraca dowolną krawędź spełniającą
warunki zadania, lub None jeśli takiej krawędzi w G nie ma. Graf przekazywany jest jako lista list
sąsiadów, t.j. G[i] to lista sąsiadów wierzchołka o numerze i. Wierzchołki numerowane są od 0.
Funkcja powinna zwrócić krotkę zawierającą numery dwóch wierzchołków pomiędzy którymi jest
krawędź spełniająca warunki zadania, lub None jeśli takiej krawędzi nie ma. Jeśli w grafie oryginalnie
nie było ścieżki z s do t to funkcja powinna zwrócić None
"""
"""
Za pomocą zmodyfikowanego algorytmu BFS znajdę najkrótszą ścieżkę z s do t. Jeśli istnieje tylko
jedna najkrótsza ścieżka, to oznacza, że da się usunąć taką krawędź (choćby tą prowadzącą bezpośrednio do
t. Jeśli istnieje więcej takich, wtedy szukam krawędzi wspólnej dla tych ścieżek - usunięcie jej będzie prowadziło
do zwiększenia najkrótszej ścieżki w grafie
"""


import collections, math
def enlarge(G, s, t):
    n = len(G)
    t_count = 0
    t_path = []
    shortest_path = math.inf
    counter = 0
    def bfs(graph, s):
        nonlocal t_count, t_path, shortest_path, t, counter
        queue = collections.deque()
        visited = [False] * len(graph)
        queue.append([s, 0, [s]])
        visited[s] = True

        while queue:
            u = queue.popleft()
            counter += 1
            print(u[2])
            # print(visited)
            if u[1] > shortest_path:
                break
            if u[0] == t:
                t_count += 1
                t_path.append(u[2])
                shortest_path = u[1]
            else:
                for v in graph[u[0]]:
                    # if v != u[2][len(u[2])-1]:
                    if not visited[v]:
                        if v == t:
                            visited[v] = u[1]+1
                            t_count += 1
                            t_path.append((u[2]+[v]))
                            shortest_path = u[1] + 1
                        else:
                            queue.append([v, u[1]+1, u[2]+[v]])
                    elif visited[v] and v == t and u[1]+1 == shortest_path:
                        t_count += 1
                        t_path.append((u[2]+[v]))


    bfs(G, s)
    print("counter: ", counter)
    return None
    print(t_count, t_path)
    if t_count == 1:
        return (t_path[0][len(t_path[0])-2], t)
    if t_count == 0:
        return None

    k = len(t_path)
    for x in range(len(t_path[0])-1):
        pair = [t_path[0][x], t_path[0][x+1]]
        print(pair)
        counter = 0
        for i in range(1, k):
            for j in range(len(t_path[i])-1):
                print(f"aaa p0: {pair}, pi: {t_path[i][j], t_path[i][j+1]}")

                if [t_path[i][j], t_path[i][j+1]] == pair:
                    counter += 1
                    break

        if counter == t_count-1:
            return pair
        else:
            print(counter)
    return None


# G = [[1, 4], [0, 2], [1, 3], [2, 5], [0, 5], [4, 3]]
# s = 0
# t = 3
# G =  [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8]]
G = [[1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [7]]
s = 0
t = 7
print(enlarge(G, s, t))
