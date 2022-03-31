"""
Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do
której przekazujemy wskaźnik na początek oraz wartość klucza. Jeżeli
element o takim kluczu występuje w liście należy go usunąć z listy. Jeżeli
elementu o zadanym kluczu brak w liście należy element o takim kluczu
wstawić do listy.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def func(first, value):
    if first != None and first.val == value:
        first = first.next
        return first

    p = first
    prev = None
    while first != None:
        if first.val == value:
            prev.next = first.next
            return p

        prev = first
        first = first.next

    r = Node(value)
    if prev:
        prev.next = r
        return p

    return r

def wypisz(first):
    while first is not None:
        #print(first)
        print(first.val, '--->', end='')
        first = first.next
    print()

def wstaw(first, value):
    p = first
    r = Node(value)
    if p == None:
        return r

    while p != None:
        previous = p
        p = p.next

    previous.next = r
    r.prev = previous
    return first


stare = None
stare = func(stare, 6)
stare = func(stare, 8)
stare = func(stare, 9)
wypisz(stare)