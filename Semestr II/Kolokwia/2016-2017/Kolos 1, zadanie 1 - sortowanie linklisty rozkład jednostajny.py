"""Dana jestr struktura opisująca listę jednokierunkową dla liczb rzeczywistych:
struct Node{ Node* next; double value; }
Proszę zaimplementować funkcję void Sort( Node* list ), która otrzymuje na wejściu listę
liczb rzeczywistych (z wartownikiem), wygenerowaną zgodnie z rozkładem jednostajnym na
przedziale [0,10) i sortuje jej zawartość w kolejności niemalejącej. Funkcja powinna być możliwie
jak najszybsza (biorąc pod uwagę warunki zadania). Proszę oszacować złożoność
zaimplementowanej funkcji.
"""

"""Iterując po liście będę odpowiednio umieszczał wartości listy w odpowiednich kubełkach z odpowiadającemu
wartości node'a zakresu. Umieszczane do odpowiednich kubełków node'y będą sortowane. Na końcu posortowane kubełki połączę
wo wyjściową posortowaną tablicę. Złożoność będzie liniowa."""


class Node:
    def __init__(self):
        self.next = None
        self.value = None


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next

def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")

def Sort(guard):
    counter = 0
    pointer = guard.next
    while pointer is not None:
        counter += 1
        pointer = pointer.next

    tab_of_tabs = [None]*counter
    for x in range(counter):
        tab_of_tabs[x] = Node()


    while guard.next is not None:
        x = guard.next
        guard.next = guard.next.next
        x.next = None
        index = int(x.value // (1/counter))
        if tab_of_tabs[index].next is not None:
            if tab_of_tabs[index].next.value > x.value:
                y = tab_of_tabs[index].next
                tab_of_tabs[index].next = x
                x.next = y
            else:
                current = tab_of_tabs[index].next
                while current.next is not None and current.next.value < x.value:
                    current = current.next

                if current.next:
                    y = current.next
                    current.next = x
                    x.next = y
                else:
                    current.next = x
        else:
            tab_of_tabs[index].next = x

    pointer = None
    for x in range(counter):
        if tab_of_tabs[x].next is not None:
            if pointer is not None:
                pointer.next = tab_of_tabs[x].next
                pointer = pointer.next
            else:
                pointer = tab_of_tabs[x].next

            while pointer.next is not None:
                pointer = pointer.next


    for x in range(counter):
        if tab_of_tabs[x].next is not None:
            return tab_of_tabs[x].next


T = [0.23, 0.11, 0.45, 0.83, 0.77, 0.92, 0.05, 0.30, 0.69, 0.54, 0.91, 0.21]
T = tab2list(T)
# counter = 10
# tab_of_tabs = [None]*counter
# for x in range(counter):
#     tab_of_tabs[x] = Node()
#
#
# a = Node()
# a.value = 20
# b = Node()
# b.value = 23
# tab_of_tabs[1].next = a
# tab_of_tabs[1].next.next = b
# print(tab_of_tabs[1].value)
# print(tab_of_tabs[1].next.next.value)
a = Node()
a.next = T
k = Sort(a)
printlist(k)