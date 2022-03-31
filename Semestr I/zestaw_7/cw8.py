"""
 Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
element listy. Do funkcji należy przekazać wskazanie na pierwszy element
listy.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def every_other_1(first):
    p = first
    while p != None and p.next != None:
        p.next = p.next.next
        p = p.next

    return first

def every_other_2(first):
    p = first.next
    copy_p = p
    first = None
    while p != None and p.next != None:
        p.next = p.next.next
        p = p.next

    return copy_p

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
        prev = p
        p = p.next

    prev.next = r
    return first

nowe = Node(43)
nowe = wstaw(nowe, 342)
nowe = wstaw(nowe, 15)
nowe = wstaw(nowe, 2)
nowe = wstaw(nowe, 632)
nowe = wstaw(nowe, 89)
nowe = wstaw(nowe, 635642)

wypisz(nowe)
nowe = every_other_1(nowe)
wypisz(nowe)
