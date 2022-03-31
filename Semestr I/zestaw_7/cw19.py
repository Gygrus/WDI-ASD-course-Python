"""
Elementy w liście są uporządkowane według wartości klucza. Proszę
napisać funkcję usuwającą z listy elementy o nieunikalnym kluczu. Do
funkcji przekazujemy wskazanie na pierwszy element listy,
funkcja powinna zwrócić liczbę usuniętych elementów.
"""

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


def del_unique(first):
    if first == None:
        return 0

    if first.next == None:
        first = None
        return 1

    prev = None
    p = first
    count = 0
    while p != None:
        if prev and p.next and (p.next.val == p.val or prev.val == p.val):
            prev = p
            p = p.next
        elif prev and p.next and not (p.next.val == p.val or prev.val == p.val):
            count += 1
            prev.next = p.next
            p = prev.next

        if not prev:
            if p.next.val != p.val:
                count += 1
                first = p.next
                p = first
            else:
                prev = p
                p = p.next

        if not p.next:
            if prev.val != p.val:
                count += 1
                prev.next = None

            p = p.next

    return count


k = Node(3)
k = wstaw(k, 7)
k = wstaw(k, 8)
k = wstaw(k, 9)
k = wstaw(k, 9)
k = wstaw(k, 10)
k = wstaw(k, 11)
wypisz(k)
print(del_unique(k))
wypisz(k)