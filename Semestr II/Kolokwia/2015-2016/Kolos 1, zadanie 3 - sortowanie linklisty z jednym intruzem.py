"""Dana jest struktura Node opisująca listę jednokierunkową:
struct Node { Node * next; int value; };
Proszę zaimplementować funkcję Node* fixSortedList( Node* L ), która otrzymuje na
wejściu listę jednokierunkową bez wartowanika. Lista ta jest prawie posortowana w tym sensie, że
powstała z listy posortowanej przez zmianę jednego losowo wybranego elementu na losową
wartość. Funkcja powinna przepiąć elementy listy tak, by lista stała się posortowana i zwrócić
wskaźnik do głowy tej listy. Można założyć, że wszystkie liczby na liście są różne i że lista ma co
najmniej dwa elementy. Funkcja powinna działać w czasie liniowym względem długości listy
wejściowej."""



"""
Iterując po liście, znajduję element nieposortowany i go wypinam z listy. Następnie znowu iteruję od początku
listy i wpinam intruza w odpowiednie miejsce. Stworzę wartownika (którego potem usunę), dla swojej wygody.
Złożoność: jeśli intruz wystąpi na pozycji k, to oczekiwana złożoność wynosi O(2k-1)"""


from random import randint, seed
from time import time
seed(42)

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


def fixSortedList(first):
    guard = Node()
    guard.next = first
    pointer = first.next
    pom_prev = None
    prev = guard.next
    while pointer is not None and pointer.value > prev.value:
        pom_prev = prev
        prev = pointer
        pointer = pointer.next

    if prev is first:
        guard.next = pointer
        prev.next = None
        pointer = prev
    elif pointer is not None:
        if pointer.next is not None and prev.value < pointer.next.value:
            prev.next = pointer.next
            pointer.next = None
        else:
            pom_prev.next = pointer
            prev.next = None
            pointer = prev


    #printlist(guard.next)
    if pointer is not None:
        prev = guard
        pointer_2 = guard.next
        while pointer_2 is not None and pointer_2.value < pointer.value:
            prev = pointer_2
            pointer_2 = pointer_2.next

        prev.next = pointer
        pointer.next = pointer_2

    return guard.next
n = 10000000
T = list(range(1, n, 2))
T[randint(0, n-1)] = 2*randint(1, 499900)
T = tab2list(T)
#printlist(T)
start = time()
k = fixSortedList(T)
end = time()
#printlist(k)
print(end-start)
