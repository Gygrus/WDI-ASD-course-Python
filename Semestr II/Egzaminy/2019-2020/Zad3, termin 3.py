"""
Dana jest struktura realizująca listę jednokierunkową:
class Node:
def __init__( self, val ):
self.next = None
self.val = val
Proszę napisać funkcję, która mając na wejściu ciąg tak zrealizowanych posortowanych list scala je
w jedną posortowaną listę (składającą się z tych samych elementów).
Przykład Dla tablicy [[0,1,2,4,5],[0,10,20],[5,15,25]] - po przekształceniu jej elementów
z Python’owskich list na listy jednokierunkowe - wynikiem powinna być lista jednokierunkowa, która
po przekształceniu jej na listę Python’owską przyjmie postać [0,0,1,2,4,5,5,10,15,20,25]
"""

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

def sort_lists(T):
    n = len(T)

    def left(i):
        return 2 * i + 1

    def right(i):
        return 2 * i + 2

    def parent(i):
        return (i - 1) // 2

    def heapify(A, n, i):  # "Naprawia" dany element i całą podgałąź
        l = left(i)
        r = right(i)
        m = i
        if l < n and A[l].next.val < A[m].next.val:
            m = l

        if r < n and A[r].next.val < A[m].next.val:
            m = r

        if m != i:
            A[i], A[m] = A[m], A[i]
            heapify(A, n, m)

    def buildheap(A):  # Buduje kopiec (typu maxheap)
        n = len(A)
        for i in range(parent(n - 1), -1, -1):
            heapify(A, n, i)

    def extract_min(A):
        n = len(A)
        if n < 1:
            return "Kopiec jest pusty"

        save = A[0].next
        A[0].next = save.next
        save.next = None
        heapify(A, n, 0)
        return save

    tab = [Node(0) for _ in range(n)]
    for x in range(n):
        tab[x].next = T[x]
        temp = tab[x].next
        while temp.next is not None:
            temp = temp.next

        temp.next = Node(float('inf'))

    buildheap(tab)
    result = Node(0)
    rem = result
    while tab[0].next.val != float('inf'):
        rem.next = extract_min(tab)
        print(rem.next.val)
        rem = rem.next

    return result.next





