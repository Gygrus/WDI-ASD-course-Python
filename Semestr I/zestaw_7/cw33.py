"""
 Napis s1 poprzedza napis s2 jeżeli ostatnia litera s1 jest „mniejsza”
od pierwszej litery s2. Według tej zasady rozmieszczono napisy w liście
cyklicznej, na przykład:
┌─bartek──leszek──marek──ola──zosia─┐
└───────────────────────────────────┘
Proszę napisać stosowne definicje typów oraz funkcję wstawiającą do listy
napis z zachowaniem zasady poprzedzania. Do funkcji należy przekazać
wskaźnik do listy oraz wstawiany napis, funkcja powinna zwrócić wartość
logiczną wskazującą, czy udało się wstawić napis do listy. Po wstawieniu
elementu wskaźnik do listy powinien wskazywać na nowo wstawiony element.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Lista:
    def __init__(self, first):
        self.first = first

    def wypisz(self):
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

def append_new(origin_list, name):
    k, p = origin_list.first, origin_list.first.next
    while p != k:
        if ord(p.val[-1]) < ord(name[0]):
            if ord(name[-1]) < ord(p.next.val[0]):
                r = Node(name)
                r.next = p.next
                p.next = r
                origin_list.first = r
                return True

        p = p.next

    if ord(p.val[-1]) < ord(name[0]):
        if ord(name[-1]) < ord(p.next.val[0]):
            r = Node(name)
            r.next = p.next
            p.next = r
            origin_list.first = r
            return True

    return False

a = Node("bartek")
a1 = Node("leszek")
a2 = Node("marek")
a3 = Node("ola")
a4 = Node("gosia")
a.next = a1
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a
t = Lista(a)
t.wypisz()
print(append_new(t, "lioth"))
t.wypisz()

