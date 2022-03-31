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
from random import randint
from time import time

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
    pointer = guard.next
    counter = 0
    while pointer is not None:
        counter += 1
        pointer = pointer.next

    buckets = [Node() for _ in range(counter)]
    buck_tails = [Node() for _ in range(counter)]

    # for x in range(counter):
    #     printlist(buck_tails[x].value)

    curr = guard.next
    while guard.next is not None:
        guard.next = curr.next
        curr.next = None
        index = int(curr.value // (10/counter))
        # print(index, curr.value)
        insert_and_sort(buckets[index], curr, buck_tails[index])
        # printlist(buck_tails[index])
        curr = guard.next

    # for x in range(counter):
    #     printlist(buckets[x])
    #
    # for x in range(counter):
    #     printlist(buck_tails[x])

    last = guard
    for x in range(counter):
        last.next = buckets[x].next
        if buckets[x].next is not None:
            last = buck_tails[x].next

    return guard.next


def insert_and_sort(guard, new, tail):
    if guard.next is None:
        guard.next = new
        tail.next = new

    else:
        pointer = guard
        while pointer.next is not None and pointer.next.value < new.value:
            pointer = pointer.next

        if pointer.next is None:
            pointer.next = new
            tail.next = new
        else:
            rem = pointer.next
            pointer.next = new
            new.next = rem


T = [randint(0, 9999999)/1000000 for _ in range(1000000)]
T = tab2list(T)
#printlist(T)
guard = Node()
guard.next = T
start = time()
k = Sort(guard)
end = time()
#printlist(k)
print(end-start)
# z = k
# counter = 0
# while z is not None:
#     counter += 1
#     z = z.next
# print(counter)