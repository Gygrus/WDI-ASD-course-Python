""" Dana jest lista, który zakończona jest cyklem.
Napisać funkcję, która zwraca liczbę elementów w cyklu.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

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

def get_cycle_length(first):
    if first == None or first.next == None:
        return False

    p, q = first, first
    while q != None or q.next != None or q.next.next != None:
        p, q = p.next, q.next.next
        if p == q:
            count = 1
            p = p.next
            while p != q:
                count += 1
                p = p.next

            return count


a1 = Node(4)
a2 = Node(5)
a3 = Node(5)
a4 = Node(53)
a5 = Node(12)
a6 = Node(6)
a7 = Node(6)
a8 = Node(6)
a9 = Node(5)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a6
a6.next = a7
a7.next = a8
a8.next = a9
a9.next = a1
print(get_cycle_length(a1))