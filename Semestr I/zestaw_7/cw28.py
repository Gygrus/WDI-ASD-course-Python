"""
Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby
naturalne. W pierwszej liście liczby są posortowane rosnąco, a w drugiej
nie. Proszę napisać funkcję usuwającą z obu list liczby występujące w obu
listach. Do funkcji należy przekazać wskazania na obie listy, funkcja
powinna zwrócić łączną liczbę usuniętych elementów.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Lista:
    def __init__(self, first):
        self.first = first

    def wypisz(self):
        napis = ""
        t = self.first
        while t != None:
            napis += str(f'{t.val} --->')
            t = t.next
        print(napis)


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

def del_dupl_s(first_one, second_one):
    if first_one == None or second_one == None:
        return 0
    counter = 0
    p = second_one.first
    prev = None
    while p != None:
        check = False
        q = first_one.first
        q_prev = None
        while q != None and q.val < p.val:
            q_prev = q
            q = q.next
        if q and q.val == p.val:
            check = True
            counter += 1
            if q_prev:
                q_prev.next = q.next
            else:
                first_one.first = q.next
            if prev:
                prev.next = p.next
            else:
                second_one.first = p.next
        if not check:
            prev = p
        p = p.next

    return counter

a = Node(23)
a = wstaw(a, 42)
a = wstaw(a, 123)

b = Node(23)
b = wstaw(b, 123)
b = wstaw(b, 3)

b2 = Lista(b)
a1 = Lista(a)
a1.wypisz()
b2.wypisz()
print(del_dupl_s(a1, b2))
a1.wypisz()
b2.wypisz()