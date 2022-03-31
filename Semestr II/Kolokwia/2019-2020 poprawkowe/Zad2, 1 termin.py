"""
W szybkiej liscie odsyłaczowej i-ty element posiada referencje (odsyłacze) do elementów: i+2
0
, i+2
1
,
i + 2
2
, . . . (lista odsyłaczy z i-tego elementu kończy się na ostatnim elemencie o numerze postaci
i + 2
k
, który występuje w liście). Lista ta przechowuje liczby całkowite w kolejności niemalejącej.
Przykładową szybką listę przedstawia poniższy rysunek:
3 4 9 12 21 103 107 119
Napisz funkcję fast list prepend:
def fast_list_prepend(L, a):
...
która przyjmuje referencję na pierwszy węzeł szybkiej listy (L) oraz liczbę całkowitą (a) mniejszą
od wszystkich liczb w przekazanej liście i wstawia tę liczbę na początek szybkiej listy (jako nowy
węzeł). W wyniku dodania nowego elementu powinna powstać prawidłowa szybka lista. W szczególności każdy węzeł powinien mieć poprawne odsyłacze do innych węzłów. Funkcja powinna zwrócić
referencję na nowy pierwszy węzeł szybkiej listy.
Zaproponowana funkcja powinna być możliwe jak najszybsza. Uzasadnij jej poprawność i oszacuj
złożoność obliczeniową. Węzły szybkiej listy reprezentowane są w postaci:
class FastListNode:
def __init__(self, a):
self.a = a # przechowywana liczba całkowita
self.next = [] # lista odsyłaczy do innych elementów; początkowo pusta
def __str__(self): # zwraca zawartość węzła w postaci napisu
res = ’a: ’ + str(self.a) + ’\t’ + ’next keys: ’
res += str([n.a for n in self.next])
return res
"""

class FastListNode:
    def __init__(self, a):
        self.a = a # przechowywana liczba całkowita
        self.next = [] # lista odsyłaczy do innych elementów; początkowo pusta

def fast_list_prepend(L, a):
    new = FastListNode(a)
    new.next.append(L)
    temp = L
    counter = 1
    # while (counter-1) < len(temp.next):
    #     new.next.append(temp.next[counter-1])
    #     temp = temp.next[counter - 1]
    #     counter += 1

    return new

