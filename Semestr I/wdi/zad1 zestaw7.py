class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def contains(first, val):
    while first != None and first.val < val:
        first = first.next

    return first != None and first.val == val


def contains_rec(first, value):
    if first == None:
        return False

    return first.val == value or contains_rec(first.next, value)

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
    napis = ""
    while first is not None:
        #print(f"{first.val} ---> ", end='')
        napis += str(f"{first.val} ---> ")
        first = first.next

    print(napis[:-5])

k = Node(5)
k = wstaw(k, 7)
k = wstaw(k, 2)
wypisz(k)
