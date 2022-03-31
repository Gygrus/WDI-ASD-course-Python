"""
 Lista reprezentuje wielomian o współczynnikach całkowitych. Elementy w
liście ułożone są według rosnących potęg. Proszę napisać funkcję
obliczającą różnicę dwóch dowolnych wielomianów. Wielomiany reprezentowane
są przez wyżej opisane listy. Procedura powinna zwracać wskaźnik do nowo
utworzonej listy reprezentującej wielomian wynikowy. Listy wejściowe
powinny pozostać niezmienione.
"""
from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

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

def wypisz(first):
    napis = ""
    while first is not None:
        #print(f"{first.val} ---> ", end='')
        napis += str(f"{first.val} ---> ")
        first = first.next

    print(napis[:-5])

def get_difference(first_one, second_one):
    p = first_one
    q = second_one
    new_one = None

    while p and q:
        if not new_one:
            new_one = Node(p.val - q.val)
            copy = new_one
        else:
            copy.next = Node(p.val - q.val)
            copy = copy.next

        p = p.next
        q = q.next

    while p and not q:
        if not new_one:
            new_one = Node(p.val)
            copy = new_one
        else:
            copy.next = Node(p.val)
            copy = copy.next
        p = p.next

    while q and not p:
        if not new_one:
            new_one = Node(-q.val)
            copy = new_one
        else:
            copy.next = Node(-q.val)
            copy = copy.next
        q = q.next

    return new_one


a = Node(randint(-10, 10))
a = wstaw(a, randint(-10, 10))
a = wstaw(a, randint(-10, 10))
a = wstaw(a, randint(-10, 10))
b = Node(randint(-10, 10))
b = wstaw(b, randint(-10, 10))
b = wstaw(b, randint(-10, 10))

wypisz(a)
wypisz(b)
t = get_difference(a, b)
wypisz(t)
wypisz(a)
wypisz(b)


