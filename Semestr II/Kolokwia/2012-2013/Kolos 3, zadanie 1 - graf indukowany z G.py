"""
Niech G = (V, E) będzie pewnym grafem nieskierowanym a U ⊆ V pewnym podzbiorem jego
wierzchołków. Grafem indukowanym G|U nazywamy graf powstały z G przez usunięcie
wszystkich wierzchołków spoza U. Proszę podać i zaimplementować wielomianowy algorytm,
który mając na wejściu graf G = (V, E) (reprezentacja przez listy sąsiedztwa) oraz liczbę
naturalną k, znajduje maksymalny co do rozmiaru zbiór U ⊆ V taki, że wszystkie wierzchołki
w G|U mają stopień większy lub równy k. Proszę oszacować czas działania algorytmu.
"""

"""
Za pomocą algorytmu BFS przechodzimy po wierzchołkach grafu, sprawdzamy stopień wierzchołków, jeśli któryś stopień 
jest mniejszy od k, to oznaczamy ten wierzchołek jako "usunięty" (a tym samym krawędź do niego jest usuwana) oraz 
powtarzamy te operacje. Po jednym przebiegu przechodzimy jeszcze raz po nieusuniętych jeszcze wierzchołkach oraz wykonujemy
tą operację dopóki nie usuniemy żadnego wierzchołka, albo nie będzie pozostałego wierzchołka z którego moglibyśmy przejść
dalej. Wynik to nieusunięte wierzchołki.
Złożoność pamięciowa: O(n)
Złożoność obliczeniowa: O(n(V+E))
"""
from queue import Queue


def check_if_exists(G, k):
    def bfs(graph, s, visited, exist, k):
        nonlocal check_2
        queue = Queue()

        queue.put(s)
        visited[s] = True

        while not queue.empty():
            u = queue.get()
            count = 0
            for v in graph[u]:
                if not visited[v] and exist[v]:
                    visited[v] = True
                    queue.put(v)
                if exist[v]:
                    count += 1

            if count < k:
                check_2 = True
                exist[u] = 0

    n = len(G)
    visited = [False]*n
    exist = [1]*n
    check_1 = False
    check_2 = False
    while True:
        # print(exist)
        for x in range(n):
            visited[x] = False
        check_2 = False
        for x in range(n):
            if exist[x] and not visited[x]:
                bfs(G, x, visited, exist, k)
                check_1 = True

        if not check_1:
            return
        # print(check_2)
        if not check_2:
            for x in range(n):
                if exist[x]:
                    print(x, end=' ')
            return

G = [[2, 3], [4], [0, 4, 5, 3], [4, 2, 0, 5], [1, 2, 3, 5], [4, 2, 3]]
k = 3
check_if_exists(G, k)
