"""Piotr Socała"""
"""Węzły jednokierunkowej listy odsyłaczowej reprezentowane są w postaci:
class Node:
def __init__(self):
self.val = None # przechowywana liczba rzeczywista
self.next = None # odsyłacz do nastepnego elementu
Niech p będzie wskaźnikiem na niepustą listę odsyłaczową zawierającą parami różne liczby rzeczywiste a1, a2, . . . , an 
(lista nie ma wartownika). Mówimy, że lista jest k-chaotyczna jeśli dla każdego elementu zachodzi, 
że po posortowaniu listy znalazłby się na pozycji różniącej się od bieżącej
o najwyżej k. Tak więc 0-chaotyczna lista jest posortowana, przykładem 1-chaotycznej listy jest
1, 0, 3, 2, 4, 6, 5, a (n − 1)-chaotyczna lista długości n może zawierać liczby w dowolnej kolejności.
Proszę zaimplementować funkcję SortH(p,k), która sortuje k-chaotyczną listę wskazywaną przez p.
Funkcja powinna zwrócić wskazanie na posortowaną listę. Algorytm powinien być jak najszybszy
oraz używać jak najmniej pamięci (w sensie asymptotycznym, mierzonym względem długości n
listy oraz parametru k). Proszę oszacować jego złożoność czasową dla k = Θ(1), k = Θ(log n) oraz
k = Θ(n)."""

"""
W pierwszym przedziale k elementów, znajdę node'a o najmniejszej wartości, wiadomo, że będzie to element który po posortowaniu
znajdowałby się na 1 pozycji. Następnie powtarzam operację dla kolejnych k elementów, ale już bez znalezionego pierwszego elementu,
który znajduje się na pierwszym miejscu listy. Operację powtarzam aż do posortowania wszystkich elementów.
"""


class Node:
    def __init__(self):
        self.val = None
        self.next = None

def SortH(p, k):
    guard_main = Node()
    guard_main.next = p

    guard = guard_main
    # pointer = guard.next
    # prev = guard
    # prev_imp = guard
    # lowest_imp = pointer
    # lowest = pointer.val
    # for x in range(k):
    #     if pointer.val < lowest:
    #         lowest_imp = pointer
    #         prev_imp = prev
    #
    #     prev = pointer
    #     pointer = pointer.next
    #
    #
    # rest = guard.next
    # prev_imp.next = lowest_imp.next
    # lowest_imp.next = None
    # guard.next = lowest_imp
    # lowest_imp.next = rest



    while guard.next is not None:
        # guard = guard.next
        pointer = guard.next
        prev = guard
        counter = 0
        lowest_imp = pointer
        prev_imp = guard
        if pointer is not None:
            lowest = pointer.val
        while pointer is not None and counter < k:
            if pointer.val < lowest:
                lowest_imp = pointer
                prev_imp = prev

            prev = pointer
            pointer = pointer.next
            counter += 1

        if lowest_imp is not guard.next:
            rest = guard.next
            prev_imp.next = lowest_imp.next
            lowest_imp.next = None
            guard.next = lowest_imp
            lowest_imp.next = rest

        guard = guard.next


    return guard_main.next



