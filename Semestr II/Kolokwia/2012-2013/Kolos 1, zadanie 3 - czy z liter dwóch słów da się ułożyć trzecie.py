"""
Proszę napisać funkcję bool possible( char* u, char* v, char* w ), która zwraca prawdę
jeśli z liter słów u i v da się ułożyć słowo w (nie jest konieczne wykorzystanie wszystkich liter)
oraz fałsz w przeciwnym wypadku. Można założyć, że w i v składają się wyłącznie z małych liter
alfabetu łacińskiego. Proszę krótko uzasadnić wybór zaimplementowanego algorytmu.
"""

"""
Za pomocą dodatkowej tablicy, do której będę dodawał ilość poszczególnych liter dwóch
podanych słów, a potem odejmował na indeksach poszczególnych liter trzeciego słowa 
będę w stanie sprawdzić czy da się zapisać to trzecie za pomocą liter z pierwszego i drugiego.
Jeśli pod odpowiednimi indeksami z liter z trzeciego słowa nie będzie choć jednej
wartości ujemnej, oznacza to, że da się ułożyć trzecie słowo.
"""
"""
Złożoność: 
u-ilość liter słowa u, 
v-ilość liter słowa v, 
w - liczba liter słowa w
złożoność  = O(u+v+2w), czyli liniowa"""



def possible(u, v, w):
    occurences = [0]*(122-97+1)
    for x in range(len(u)):
        occurences[ord(u[x])-97] += 1

    for x in range(len(v)):
        occurences[ord(v[x]) - 97] += 1

    for x in range(len(w)):
        occurences[ord(w[x]) - 97] -= 1

    for x in range(len(w)):
        if occurences[ord(w[x]) - 97] < 0:
            return False

    return True

print(possible('kurczak', 'dupsko', 'kurdupskoczakk'))