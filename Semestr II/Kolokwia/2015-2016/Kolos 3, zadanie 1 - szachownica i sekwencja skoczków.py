"""
Szachownica NxN, ustawiono pewną ilość skoczków. Opisać algorytm który sprawdzi czy jest
możliwa sekwencja ruchów spełniająca:
- każdy ruch kończy się zbiciem skoczka
- sekwencja kończy się gdy zostanie jeden skoczek.
"""

"""
Przechodząc po szachownicy tworzymy graf, gdzie pozycje skoczków to wierzchołki, a mają krawędź do innego skoczka gdy
mogą go "zbić". Następnie sprawdzenie czy dana sekwencja jest możliwa, sprowadza się do sprawdzenia czy istnieje cykl 
Hamiltona. Można to sprawdzić za pomocą zmodyfikowanej funkcji dfs, która będzie oznaczać skoczków jako odwiedzonych przed
przetworzeniem (od razu po odwiedzeniu) oraz ich odznaczać po przetworzeniu. 
"""