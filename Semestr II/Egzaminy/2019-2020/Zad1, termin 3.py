"""
Każdy nieskierowany, spójny i acyckliczny graf G = (V, E) możemy traktować jako drzewo. Korzeniem tego drzewa może być dowolny wierzchołek v ∈ V . Napisz funkcję best root(L), która
przyjmuje nieskierowany, spójny i acyckliczny graf G (reprezentowany w postaci listy sąsiedztwa) i
wybiera taki jego wierzchołek, by wysokość zakorzenionego w tym wierzchołku drzewa była możliwie najmniejsza. Jeśli kilka wierzchołków spełnia warunki zadania, funkcja może zwrócić dowolny z
nich. Wysokość drzewa definiujemy jako liczbę krawędzi od korzenia do najdalszego liścia. Uzasadnij
poprawność zaproponowanego algorytmu i oszacuj jego złożoność obliczeniową.
Funkcja best root(L) powinna zwrócić numer wierzchołka wybranego jako korzeń. Wierzchołki
numerujemy od 0. Argumentem best root(L) jest lista postaci:
L = [l0,l1, . . . ,ln−1],
gdzie li to lista zawierająca numery wierzchołków będących sąsiadami i−tego wierzchołka. Można
przyjąć (bez weryfikacji), że lista opisuje graf spełniający warunki zadania. W szczególności, graf
jest spójny, acykliczny, oraz jeśli a ∈ lb to b ∈ la (graf jest nieskierowany). Nagłówek funkcji powinien
mieć postać:
def best_root(L):
"""


def best_root(L):
    n = len(L)
    def dfs(graph, s):
        visited = [False] * len(graph)
        distances = [0]*len(graph)
        best = 0
        save = 0

        def dfs_visit(u, counter):
            nonlocal graph, visited, best, save

            visited[u] = True
            distances[u] = counter
            if counter > best:
                best = counter
                save = u

            for v in graph[u]:
                if not visited[v]:
                    dfs_visit(v, counter + 1)

        dfs_visit(s, 0)

        return save, distances

    first, _ = dfs(L, 0)
    second, first_tab = dfs(L, first)
    _, sec_tab = dfs(L, second)
    print(first, second)
    print(first_tab, sec_tab)
    output = float('inf')
    result = 0
    for x in range(n):
        if output > max(first_tab[x], sec_tab[x]):
            result = x
        output = min(output, max(first_tab[x], sec_tab[x]))

    return result


L = [ [ 2 ],
[ 2 ],
[ 0, 1, 3],
[ 2, 4 ],
[ 3, 5, 6 ],
[ 4 ],
[ 4 ] ]
print(best_root(L))


