"""
Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
element listy o wartościach typu int, usuwającą wszystkie elementy, których
wartość jest mniejsza od wartości bezpośrednio poprzedzających je
elementów.
"""
from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def delete_directly_lesser(first):
    p = first
    prev = None

    while p.next != None:
        if p.next.val > p.val:
            if not prev:
                first = p.next
            else:
                prev.next = p.next

        else:
            prev = p

        p = p.next

    return first

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


k = Node(6)
k = wstaw(k, randint(1, 20))
k = wstaw(k, randint(1, 20))
k = wstaw(k, randint(1, 20))
k = wstaw(k, randint(1, 20))
k = wstaw(k, randint(1, 20))
k = wstaw(k, randint(1, 20))
wypisz(k)
k = delete_directly_lesser(k)
wypisz(k)