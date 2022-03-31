"""
Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która
zwraca wskaźnik do ostatniego elementu przed cyklem.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def wypisz(first):
    napis = ""
    while first is not None:
        print(f"{first.val} ---> ", end='')
        napis += str(f"{first.val} ---> ")
        first = first.next

    print(napis[:-5])

def wstaw(first, value):
    p = first
    r = Node(value)
    if p == None:
        return r

    while p != None:
        previous = p
        p = p.next

    previous.next = r
    return first


def get_pointer(first):
    p = q = first
    while True:
        p = p.next
        q = q.next.next
        if p == q:
            break

    p = first
    prev = None
    while p != q:
        prev = p
        p = p.next
        q = q.next
    return prev

a1 = Node(4)
a2 = Node(5)
a3 = Node(7)
a4 = Node(53)
a5 = Node(12)
a6 = Node(6)
a7 = Node(56)
a8 = Node(6)
a9 = Node(5)
a10 = Node(10)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a6
a6.next = a7
a7.next = a8
a8.next = a9
a9.next = a10
a10.next = a1
z = get_pointer(a1)
if z:
    print(z.val)
else:
    print(z)
