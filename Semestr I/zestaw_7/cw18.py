"""
Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy
unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy.
"""
from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def wypisz(first):
    napis = ""
    while first is not None:
        #print(first)
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
    #r.prev = previous
    return first


def catch_them_all(first, value):
    check = False
    prev = first
    p = first.next
    if p == None:
        return False

    while p != None:
        if p.val == value:
            check = True
            prev.next = p.next
            p = prev.next

        else:
            prev = p
            p = p.next

    return check



def leave_unique(first):
    if first == None:
        return first

    prev = None
    p = first
    while p != None:
        if catch_them_all(p, p.val):
            if prev:
                prev.next = p.next
                p = prev.next
            else:
                first = p.next
                p = p.next

        else:
            prev = p
            p = p.next

    return first

k = Node(randint(1, 10))
k = wstaw(k, randint(1, 10))
k = wstaw(k, randint(1, 10))
k = wstaw(k, randint(1, 10))
k = wstaw(k, randint(1, 10))
k = wstaw(k, randint(1, 10))
wypisz(k)
k = leave_unique(k)
wypisz(k)