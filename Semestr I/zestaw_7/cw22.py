"""
Dana jestlista, który być może zakończona jest cyklem.
Napisać funkcję, która sprawdza ten fakt.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.mark = 0

def wypisz(first):
    napis = ""
    while first is not None:
        print(f"{first.val} ---> ", end='')
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
    return first


def check_if_cycle(first):
    p = first
    while p != None:
        #print(p.val)
        #print(f"{p.val} ---> ", end = '')
        p.mark += 1
        if p.next != None and p.next.mark >= p.mark:
            return True

        p = p.next

    return False

def check_if_cycle_2(first):
    if first == None or first.next == None:
        return False
    a, b = first, first
    while b != None and b.next != None and b.next.next != None:
        #print(a.val, b.val)
        a, b = a.next, b.next.next
        if a == b:
            return True

    return False


k = Node(4)
z = Node(5)
k.next = z
p = Node(5)
z.next = p
a = Node(53)
p.next = a
b = Node(12)
a.next = b
c = Node(6)
b.next = c
a1 = Node(6)
c.next = a1
a2 = Node(6)
a1.next = a2
a3 = Node(5)
a2.next = a3
a4 = Node(7)
a3.next = a4
a5 = Node(7)
a4.next = a5
a6 = Node(7)
a5.next = a6
a7 = Node(7)
a6.next = a7
a8 = Node(7)
a7.next = a8
a9 = Node(7)
a8.next = a9
a9.next = k
print(check_if_cycle(k))
print(check_if_cycle_2(k))
