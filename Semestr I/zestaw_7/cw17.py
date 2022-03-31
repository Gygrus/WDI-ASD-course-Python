"""
Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
początek listy dwukierunkowej, usuwa z niej wszystkie elementy, w których
wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.
"""
from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


def wypisz(first):
    napis = ""
    while first is not None:
        #print(first)
        napis += str(f"{first.val} ---> ")
        first = first.next

    print(napis[:-5])

def wypisz_reverse(first):
    napis = ""
    while first.next is not None:
        first = first.next

    while first is not None:
        napis += str(f"{first.val} ---> ")
        first = first.prev
        
    print(napis[:-5])

def wstaw_2_directions(first, value):
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

def check_binary(n):
    p = n
    count_ones = 0
    while p != 0:
        if p % 2 == 1:
            count_ones += 1

        p //= 2

    print("liczba:", n, "jedynki:", count_ones)

    if count_ones % 2 == 1:
        return True

    return False

def delete_func(first):
    if first == None:
        return first

    p = first
    previous = None
    while p != None:
        if check_binary(p.val):
            if previous:
                previous.next = p.next
                if p.next != None:
                    p.next.prev = previous
                p = previous.next

            else:
                first = p.next
                p = p.next

        else:
            previous = p
            p = p.next

    return first

t = Node(7)
t = wstaw_2_directions(t, randint(1, 30))
t = wstaw_2_directions(t, randint(1, 30))
t = wstaw_2_directions(t, randint(1, 30))
t = wstaw_2_directions(t, randint(1, 30))
t = wstaw_2_directions(t, randint(1, 30))
wypisz(t)
wypisz_reverse(t)
t = delete_func(t)
wypisz(t)