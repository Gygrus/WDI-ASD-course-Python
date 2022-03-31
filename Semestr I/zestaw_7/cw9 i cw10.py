"""
 Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne
elementy listy przechowują kolejne cyfry. Proszę napisać funkcję
zwiększającą taką liczbę o 1.

Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać
funkcję dodającą dwie takie liczby. W wyniku dodawania dwóch liczb powinna
powstać nowa lista.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

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


def append_one(first):
    p = first
    if p.next == None:
        if p.val == 9:
            p.val = 0
            r = Node(1)
            r.next = p
            p.prev = r
            return r

        p.val += 1
        return p

    while p.next != None:
        p = p.next

    p.val += 1
    while p.val == 10 and p.prev != None:
        p.val = 0
        p = p.prev
        p.val += 1

    if p.val == 10 and p.prev == None:
        p.val = 0
        r = Node(1)
        r.next = p
        p.prev = r
        return r

    return first

def get_length(p):
    n = p
    length = 0
    while n != 0:
        n //= 10
        length += 1

    return length


def add_two(first_1, first_2):
    first_number = 0
    second_number = 0
    while first_1 != None or first_2 != None:
        if first_1 != None:
            first_number = first_number*10 + first_1.val
            first_1 = first_1.next

        if first_2 != None:
            second_number = second_number*10 + first_2.val
            first_2 = first_2.next

    new = first_number + second_number
    length = get_length(new)
    if length == 0:
        first = Node(new)
        return first

    first = Node(new//10**(length-1))
    p = first
    for x in range(length-2, -1, -1):
        r = Node(new//10**(x) % 10)
        first.next = r
        r.prev = first
        first = first.next

    return p





nowe = Node(9)
nowe = wstaw(nowe, 9)
nowe = wstaw(nowe, 9)
nowe = wstaw(nowe, 6)
nowe = wstaw(nowe, 9)
wypisz(nowe)

stare = Node(3)
stare = wstaw(stare, 6)
stare = wstaw(stare, 1)
stare = wstaw(stare, 7)
wypisz(stare)

x = add_two(stare, nowe)
#x = append_one(x)
wypisz(x)