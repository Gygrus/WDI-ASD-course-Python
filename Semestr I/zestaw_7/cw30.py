"""
Dane są dwie niepuste listy, z których każda zawiera niepowtarzające
się elementy. Elementy w pierwszej liście są uporządkowane rosnąco, w
drugiej elementy występują w przypadkowej kolejności. Proszę napisać
funkcję, która z dwóch takich list stworzy jedną, w której uporządkowane
elementy będą stanowić sumę mnogościową elementów z list wejściowych.
Do funkcji należy przekazać wskazania na obie listy, funkcja powinna
zwrócić wskazanie na listę wynikową. Na przykład dla list:
2 -> 3 -> 5 ->7-> 11
8 -> 2 -> 7 -> 4
powinna pozostać lista:
2 -> 3 -> 4 -> 5 ->7-> 8 -> 11
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Lista:
    def __init__(self, first):
        self.first = first

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

def join_to_set(first_one, second_one):
    # if first_one == None:
    #     return second_one
    # if second_one == None:
    #     return first_one
    p = second_one
    while p != None:
        t = p.next
        q = first_one
        q_prev = None
        while q != None and q.val < p.val:
            q_prev = q
            q = q.next
        if q and q.val != p.val or not q:
            if q_prev:
                q_prev.next = p
                p.next = q
            else:
                p.next = q
                first_one = p

        p = t

    return first_one

a = Node(2)
a = wstaw(a, 3)
a = wstaw(a, 5)
a = wstaw(a, 7)
a = wstaw(a, 11)
b = Node(8)
b = wstaw(b, 2)
b = wstaw(b, 7)
b = wstaw(b, 4)

wypisz(a)
wypisz(b)
k = join_to_set(a, b)
wypisz(k)