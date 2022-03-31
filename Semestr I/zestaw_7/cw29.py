"""
 Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby
naturalne. W obu listach liczby są posortowane rosnąco. Proszę napisać
funkcję usuwającą z każdej listy liczby nie występujące w drugiej. Do
funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić
łączną liczbę usuniętych elementów.
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
    return first


def del_uniques(first_one, second_one):
    counter = 0
    p = first_one.first
    prev = None
    q = second_one.first
    q_prev = None
    while p != None:
        check = False
        while q != None and q.val < p.val:
            q_prev = q
            q = q.next

        if q and q.val != p.val or q == None:
            check = True
            counter += 1
            if prev:
                prev.next = p.next
            else:
                first_one.first = p.next
        if not check:
            prev = p
        p = p.next

    return counter

def func_proper(first_one, second_one):
    if first_one.first == None or second_one.first == None:
        return 0

    sum_1 = del_uniques(first_one, second_one)
    sum_2 = del_uniques(second_one, first_one)
    return  sum_1 + sum_2

a = Node(4)
a = wstaw(a, 6)
a = wstaw(a, 8)
a = wstaw(a, 11)
a = wstaw(a, 12)
a = wstaw(a, 17)
a = wstaw(a, 19)

b = Node(4)
b = wstaw(b, 5)
b = wstaw(b, 6)
b = wstaw(b, 12)
b = wstaw(b, 17)
b = wstaw(b, 19)
b = wstaw(b, 42)
b = wstaw(b, 224)

b2 = Lista(b)
a1 = Lista(a)
a1.wypisz()
b2.wypisz()
print(func_proper(a1, b2))
a1.wypisz()
b2.wypisz()