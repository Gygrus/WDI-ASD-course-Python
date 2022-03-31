"""
Proszę napisać funkcję, która usuwa z listy cyklicznej elementy,
których klucz występuje dokładnie k razy. Do funkcji należy przekazać
wskazanie na jeden z elementów listy, oraz liczbę k, funkcja powinna
zwrócić informację czy usunięto jakieś elementy z listy.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Lista:
    def __init__(self, first):
        self.first = first

    def wypisz(self):
        if self.first == None:
            print("Lista jest pusta!")
            return
        k, t = self.first, self.first.next
        napis = f"{k.val} ---> "
        while t != k:
            napis += str(f"{t.val} ---> ")
            t = t.next
        print(napis)
        back = "<"
        for x in napis[:-2]:
            back += "-"
        print(back)

def get_values(cycled_list):
    p, q = cycled_list.first, cycled_list.first.next
    counter = 0
    while q != p:
        counter += 1
        q = q.next

    counter += 1
    tab = [0 for x in range(counter)]
    i = 1
    tab[0] = q.val
    q = q.next
    while q != p:
        tab[i] = q.val
        q = q.next
        i += 1

    return tab


def delete_k_elements(cycled_list, k):
    if cycled_list.first == None:
        return False
    p, prev, q = cycled_list.first, cycled_list.first, cycled_list.first.next
    tab = get_values(cycled_list)
    check = False
    while q != p:
        if tab.count(q.val) == k:
            check = True
            prev.next = q.next
        else:
            prev = q
        q = q.next

    if tab.count(q.val) == k:
        check = True
        if prev == q and q.next == q:
            cycled_list.first = None
        else:
            prev.next = q.next
            cycled_list.first = q.next

    return check


a = Node(3)
a1 = Node(5)
a2 = Node(7)
a3 = Node(4)
a4 = Node(93)
a5 = Node(32)
a6 = Node(8)
a7 = Node(94)
a8 = Node(3)
a.next = a1
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a6
a6.next = a7
a7.next = a8
a8.next = a
p = Node(6)
p.next = p
t1 = Lista(p)
t = Lista(a)
t.wypisz()
print(delete_k_elements(t, 3))
t.wypisz()