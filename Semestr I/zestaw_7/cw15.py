"""
Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
początek listy jednokierunkowej, usuwa z niej wszystkie elementy, w których
wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek.
"""
from random import randint

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
    r.prev = previous
    return first

def check_trirary(n):
    p = n
    new = ''
    count = 0
    while p != 0:
        new += str(p%3)
        p //= 3

    new = new[::-1]
    new = int(new)
    print("Oryginał:", n, ", nowa:", new)

    count_1 = 0
    count_2 = 0
    while new != 0:
        k = new % 10
        new //= 10

        if k == 1:
            count_1 += 1
        elif k == 2:
            count_2 += 1

    if count_1 > count_2:
        return True

    return False

def delete_func(first):
    p = first
    if p == None:
        return first

    prev = None
    while p != None:
        if check_trirary(p.val):
            if prev:
                prev.next = p.next
            else:
                first = p.next
        else:
            prev = p
        p = p.next

    return first


k = Node(4)
k = wstaw(k, randint(1, 20))
k = wstaw(k, randint(1, 20))
k = wstaw(k, randint(1, 20))
k = wstaw(k, randint(1, 20))
k = wstaw(k, randint(1, 20))

wypisz(k)
k = delete_func(k)
wypisz(k)