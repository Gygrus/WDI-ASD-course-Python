"""
Dany jest zbiór N zadań, gdzie niektóre zadania muszą być wykonane przed innymi zadaniami.
Wzajemne kolejności zadań opisuje dwuwymiarowa tablica T[N][N]. Jeżeli T[a][b] = 1 to wykonanie zadania a musi poprzedzać wykonanie zadania b. W przypadku gdy T[a][b] = 2 zadanie b
musi być wykonane wcześniej, a gdy T[a][b] = 0 kolejność zadań a i b jest obojętna. Proszę zaimplementować funkcję tasks(T), która dla danej tablicy T, zwraca tablicę z kolejnymi numerami
zadań do wykonania.
Przykład Dla tablicy T = [ [0,2,1,1], [1,0,1,1], [2,2,0,1], [2,2,2,0] ] wynikiem
jest tablica [1,0,2,3].
"""

def dfs(graph, s, visited, output):
    def dfs_visit(u):
        nonlocal graph, visited, output
        visited[u] = True
        for v in range(len(graph)):
            if graph[u][v] == 1 and not visited[v]:
                dfs_visit(v)

        output.append(u)

    dfs_visit(s)

def tasks(T):
    n = len(T)
    visited = [False]*n
    result = []
    for x in range(n):
        if not visited[x]:
            dfs(T, x, visited, result)

    return result[::-1]


T = [ [0,2,1,1], [1,0,1,1], [2,2,0,1], [2,2,2,0] ]
A = [ [0,0,2,1,1], [1,0,0,0,0], [1,1,0,0,0], [0,0,0,0,0], [2,0,0,1,0] ]
print(tasks(A))

    

