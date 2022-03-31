"""
Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów.
Krańce przedziałów określa uporządkowana para liczb całkowitych. Proszę
napisać stosowne deklaracje oraz funkcję redukującą liczbę elementów listy.
Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17]
powinien zostać zredukowany do listy: [13,19] [2,6] [7,12]
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
    #r.prev = previous
    return first


def check_if_combine(s1, s2):
    if s1[0] <= s2[0] and s1[1] >= s2[1]:
        return s1
    if s1[0] >= s2[0] and s1[1] <= s2[1]:
        return s2
    if s1[0] >= s2[0] and s1[0] <= s2[1]:
        return [s2[0], s1[1]]
    if s1[1] >= s2[0] and s1[1] <= s2[1]:
        return [s1[0], s2[1]]

    return False


def seek_for_combine(first):
    control = True
    while control == True:
        control = False
        p = first.next
        prev = first

        while p != None:
            if check_if_combine(first.val, p.val):
                first.val = check_if_combine(first.val, p.val)
                prev.next = p.next
                p = prev.next
                control = True

            else:
                prev = p
                p = p.next
    #return control

def combine_func(first):
    if first == None:
        return

    if first.next == None:
        return

    p = first
    while p != None:
        seek_for_combine(p)
        p = p.next

    p = first
    while p != None:
        seek_for_combine(p)
        p = p.next



#[15,19] [2,5] [7,11] [8,12] [5,6] [13,17]
k = Node([15,19])
k = wstaw(k, [45, 56])
k = wstaw(k, [1, 6])
k = wstaw(k, [6, 11])
k = wstaw(k, [3, 4])
k = wstaw(k, [13, 15])

wypisz(k)
combine_func(k)
wypisz(k)
