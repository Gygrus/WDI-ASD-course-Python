



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


def usun(L):
    el = L
    prev = None
    while el != None:
        el2 = el.next
        prev2 = el2
        flaga = False
        while el2 is not None:
            if el2.val == el.val:
                prev2.next = el2.next
                el2 = el2.next
                flaga = True
            else:
                prev2 = prev2.next
                el2 = el2.next

        if flaga:
            if prev is None:
                L = L.next
            else:
                prev.next = el.next
                el = el.next
        else:
            prev = el
            el = el.next

    return L


a = Node(2)
b = Node(2)
c = Node(5)
d = Node(6)
a.next = b
b.next = c
c.next = d
