"""
Proszę napisać funkcję, która rozdziela listę na dwie listy. Pierwsza
powinna zawierać klucze parzyste dodatnie, drugi klucze nieparzyste ujemne,
pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać
wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe. Funkcja
powinna zwrócić liczbę usuniętych elementów.
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

def wypisz(first):
    napis = ""
    while first is not None:
        #print(f"{first.val} ---> ", end='')
        napis += str(f"{first.val} ---> ")
        first = first.next

    print(napis[:-5])

def split_to_two(original, plus_even, minus_uneven):
    if original.first == None:
        return 0
    counter = 0
    p = original.first
    pl_ev = None
    min_un = None
    while p != None:
        if p.val > 0 and p.val % 2 == 0:
            if not plus_even.first:
                plus_even.first = p
                pl_ev = plus_even.first
            else:
                pl_ev.next = p
                pl_ev = pl_ev.next
        elif p.val < 0 and p.val*(-1) % 2 == 1:
            if not minus_uneven.first:
                minus_uneven.first = p
                min_un = minus_uneven.first
            else:
                min_un.next = p
                min_un = min_un.next
        else:
            counter += 1
        original.first = original.first.next
        p = original.first

    if pl_ev:
        pl_ev.next = None
    if min_un:
        min_un.next = None



    return counter


a = Node(-43)
a = wstaw(a, 60)
a = wstaw(a, 8)
a = wstaw(a, 2)
a = wstaw(a, -7)
a = wstaw(a, 24)
a = wstaw(a, -11)
a = wstaw(a, -32)
a = wstaw(a, 45)
origin = Lista(a)
origin.wypisz()
parzyste = Lista(None)
nieparzyste = Lista(None)
print(split_to_two(origin, parzyste, nieparzyste))
print("parzyste")
parzyste.wypisz()
print("nieparzyste")
nieparzyste.wypisz()
origin.wypisz()



