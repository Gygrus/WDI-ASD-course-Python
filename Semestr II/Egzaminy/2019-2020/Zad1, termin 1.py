"""
Pewna kraina składa się z wysp pomiędzy którymi istnieją połączenia lotnicze, promowe oraz mosty.
Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
na wyspę wynosi 8B, koszt przeprawy promowej wynosi 5B, za przejście mostem trzeba wnieść
opłatę 1B. Poszukujemy trasy z wyspy A na wyspę B, która na kolejnych wyspach zmienia środek
transportu na inny oraz minimalizuje koszt podróży.
Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy
oznacza brak bezpośredniego połączenia. Proszę zaimplementować funkcję islands( G, A, B )
zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca warunki zadania
nie istnieje, funkcja powinna zwrócić wartość None.
Przykład Dla tablicy
G1 = [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,1,0 ],
[0,8,0,0,1,0,5 ],
[0,0,8,1,0,5,0 ] ]
funkcja islands(G1, 5, 2) powinna zwrócić wartość 13.
"""
from queue import PriorityQueue

def islands(G, A, B):
    n = len(G)
    visited = [[False, False, False] for _ in range(n)]
    distance = [[float('inf'), float('inf'), float('inf')] for _ in range(n)]
    distance[A] = [0, 0, 0]
    # visited[A] = [True, True, True]
    # queue = PriorityQueue()
    # queue.put(0, A, 1)
    # queue.put(0, A, 5)
    # queue.put(0, A, 8)
    for _ in range(3):
        for _ in range(n):
            min = float('inf')
            for i in range(n):
                for j in range(3):
                    if distance[i][j] < min and not visited[i][j]:
                        min = distance[i][j]
                        dist, isle, value = distance[i][j], i, j

            # print(dist, isle, value)
            visited[isle][value] = True
            for x in range(n):
                if G[isle][x] == 1 and not visited[x][0] and value != 0:
                    if dist + 1 < distance[x][0]:
                        distance[x][0] = dist + 1

                elif G[isle][x] == 5 and not visited[x][1] and value != 1:
                    if dist + 5 < distance[x][1]:
                        distance[x][1] = dist + 5

                elif G[isle][x] == 8 and not visited[x][2] and value != 2:
                    if dist + 8 < distance[x][2]:
                        distance[x][2] = dist + 8

    result = float('inf')
    for i in distance[B]:
        if i < result:
            result = i

    for x in distance:
        print(x)
    return result


G1 = [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,1,0 ],
[0,8,0,0,1,0,5 ],
[0,0,8,1,0,5,0 ] ]
print(islands(G1, 5, 2))