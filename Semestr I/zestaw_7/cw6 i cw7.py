"""
Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do
funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą
wartość.

Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji
należy przekazać wskazanie na pierwszy element listy.

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def wstaw(first, value):
    p = first
    r = Node(value)
    if p == None:
        return r

    while p != None:
        prev = p
        p = p.next

    prev.next = r
    return first

def usun(first):
    p = first
    if p.next == None or p == None:
        return None
    while p.next != None:
        prev = p
        p = p.next
    prev.next = None
    return first


def wypisz(first):
    while first is not None:
        #print(first)
        print(first.val, '--->', end='')
        first = first.next
    print()


lista = Node(46)
lista = wstaw(lista, 23)
lista = wstaw(lista, 3561)
lista = wstaw(lista,2)
wypisz(lista)
