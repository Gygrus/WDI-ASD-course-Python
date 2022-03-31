
"""
1. Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to miasta a krawędzie to
drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba
naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V ,
zamieniając się za kierownicą w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje kto
prowadzi pierwszy. Proszę zaproponować algorytm, który wskazuje taką trasę (oraz osobę, która
ma prowadzić pierwsza), żeby Alicja przejechała jak najmniej kilometrów. Algorytm powinien
być jak najszybszy (ale przede wszystkim poprawny). Proszę oszacować złożoność
zaproponowanego algorytmu, zakładając, że graf jest reprezentowany macierzowo.
"""

"""
1.
Jako że dla grafu nieważonego można znaleźć najkrótszą drogę pomiędzy dwoma wierzchołkami za pomocą BFS, 
a każdy graf ważony o wagach większych od 0 da się przedstawić za pomocą grafu nieważonego o odpowiednio
wstawionych dodatkowych wierzchołkach, to użyję BFS, ale połączenia będę traktował jako drogi o długości 1
pomiędzy którymi są miasta "nieważne", w których alicja i bob się nie zatrzymują i cały czas prowadzi jedna 
osoba. Raz użyję BFS-a na jednym z miast, policzę w ten sposób odległości Alicji (albo Boba), potem
pomijając wagę przechodzę do kolejnych miast nie dodając wagi do mojej sumy, następnie z kolejnego miasta
znów po kolei liczę długość i wrzucam przebyte jednostkowe drogi do sumy. Potem robię to samo, ale pomijam 
pierwsze odległości z miasta początkowego, liczę dopiero od drugiego.
Zapisujemy przebytą odległość między miastami do odpowiedniej z dwóch sum oraz zapisujemy przebyte miasta.
"""

