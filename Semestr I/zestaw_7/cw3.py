"""
 Proszę napisać funkcję scalającą dwie posortowane listy w jedną
posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
- funkcja iteracyjna,
- funkcja rekurencyjna.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def scal_listy(start_1, start_2):
    if start_1.val > start_2.val:
        m1 = start_1
        m2 = start_2
        start_1 = m2
        start_2 = m1
    x = start_1

    while start_1.next != None and start_2 != None:
        while start_1.next != None and start_1.next.val <= start_2.val:
            start_1 = start_1.next

        t2 = start_2.next
        t1 = start_1.next
        start_1.next = start_2
        start_2.next = t1
        start_2 = t2
        start_1 = start_1.next

    if start_1.next == None:
        start_1.next = start_2
    wypisz(x)
    return x

def scal_rec(start_1, start_2):
    if start_1.val > start_2.val:
        m1 = start_1
        m2 = start_2
        start_1 = m2
        start_2 = m1


    def rekur(start_1, start_2):
        if start_1.next == None:
            start_1.next = start_2
            return
        if start_2 == None:
            return

        if start_1.next.val < start_2.val:
            start_1 = start_1.next
            rekur(start_1, start_2)
        else:
            new_start_2_next = start_2.next
            start_2.next = start_1.next
            start_1.next = start_2
            start_1 = start_1.next

            rekur(start_1, new_start_2_next)

    rekur(start_1, start_2)
    wypisz(start_1)

    return start_1

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


x = Node(4)
x = wstaw(x, 7)
y = Node(5)
y = wstaw(y, 11)
y = wstaw(y, 5)
y = wstaw(y, 7)
y = wstaw(y, 12)
y = wstaw(y, 12)
y = wstaw(y, 24)
y = wstaw(y, 6)
y = wstaw(y, 73)
y = wstaw(y, 4)
wypisz(x)
wypisz(y)
t = scal_rec(y, x)
#p = scal_listy(x, y)
