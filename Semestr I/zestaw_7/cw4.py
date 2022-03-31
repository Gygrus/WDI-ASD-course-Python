"""
 Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
kolejność jej elementów.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse(first):
    if first == None:
        return first

    prev = None
    while first.next != None:
        x = first.next
        first.next = prev
        prev = first
        first = x
    first.next = prev
    return first


def wstaw(pointer, x):
    p = pointer
    q = None

    while p != None and p.val < x:
        q = p
        p = p.next

    if p != None and p.val == x:
        return pointer

    r = Node(x)


    if q == None:
        r.next = p
        return r

    q.next = r
    r.next = p
    return pointer

def wypisz(first):
    while first is not None:
        print(first.val, '--->', end='')
        first = first.next
    print()




z = Node(5)
z = wstaw(z, 7)
z = wstaw(z, 64)
z = wstaw(z, 35)
z = wstaw(z, 27)
z = wstaw(z, 3)
z = wstaw(z, 10)
wypisz(z)
x = reverse(z)
wypisz(x)