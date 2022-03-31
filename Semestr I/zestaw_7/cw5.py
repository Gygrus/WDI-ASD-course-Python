"""
Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do
10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy
należy połączyć w jedną listę odsyłaczową, która jest posortowana
niemalejąco według ostatniej cyfry pola val.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_last(n):
    return n%10

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

def divide(first):
    tab = [None]*10
    while first != None:
        x = get_last(first.val)
        pom = first.next
        cur = first
        cur.next = None
        if tab[x] == None:
            tab[x] = cur
        else:
            kupsko = tab[x]
            while kupsko.next != None:
                kupsko = kupsko.next
            kupsko.next = cur
            #wstaw(tab[x], first.val)

        first = pom
    p = None
    for x in tab:
        if x != None:
            if p == None:
                p = x
            else:
                t.next = x

            while x.next != None:
                x = x.next

            t = x

    return p





z = Node(2)
wstaw(z, 34)
wstaw(z, 3)
wstaw(z, 3323)
wstaw(z, 636)
wstaw(z, 74)
wstaw(z, 35)
wstaw(z, 5)
wstaw(z, 63)
wstaw(z, 78)
wstaw(z, 234)
wstaw(z, 13462)
wstaw(z, 675)
wstaw(z, 74)
wstaw(z, 35)
wstaw(z, 24)
m = divide(z)
wypisz(m)