"""
Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
początek listy jednokierunkowej, przenosi na początek listy te z nich,
które mają parzystą ilość piątek w zapisie ósemkowym.
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

def check_pentary(n):
    p = n
    new = ''
    while p != 0:
        new += str(p%8)
        p //= 8

    new = new[::-1]
    print("Oryginał:", n, ", nowa:", new)

    if new.count("5") % 2 == 0:
        print('super')
        return True

    return False

def replace_elements(first):
    p = first
    if p == None:
        return first

    prev = None
    t = False
    while p != None:
        if check_pentary(p.val):
            if prev:
                t = True
                prev.next = p.next
                p.next = first
                first = p
                p = prev.next
            else:
                p = p.next
        else:
            prev = p
            p = p.next

    if t:
        return first

    return first

k = Node(1547)
k = wstaw(k, randint(1, 100))
k = wstaw(k, randint(1, 100))
k = wstaw(k, randint(1, 100))
k = wstaw(k, randint(1, 100))
k = wstaw(k, randint(1, 100))
wypisz(k)
k = replace_elements(k)
wypisz(k)