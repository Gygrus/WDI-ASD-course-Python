"""
 Kolejne elementy listy o zwiększającej się wartości pola val nazywamy
podlistą rosnącą. Proszę napisać funkcję, która usuwa z listy wejściowej
najdłuższą podlistę rosnącą. Warunkiem usunięcia jest istnienie w liście
dokładnie jednej najdłuższej podlisty rosnącej.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def wypisz(first):
    napis = ""
    while first is not None:
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
    return first

def is_bigger(v1, v2):
    return v1 < v2

def get_longest(first):
    if first == None or first.next == None:
        return first
    count = 0
    length_of_list = 0
    biggest = 0
    p = first
    prev = None
    prev_save = None
    next_save = None
    result_prev = None
    while p.next != None:
        if is_bigger(p.val, p.next.val):
            if not length_of_list:
                length_of_list = 1
                if prev:
                    prev_save = prev


            length_of_list += 1
            if p.next.next == None:
                if length_of_list == biggest and biggest != 0:
                    count += 1
                if length_of_list > biggest:
                    count = 1
                    biggest = length_of_list
                    next_save = p.next.next
                    result_prev = prev_save

        else:
            if length_of_list > biggest:
                count = 1
                biggest = length_of_list
                next_save = p.next
                result_prev = prev_save


            elif length_of_list == biggest and biggest != 0:
                count += 1

            length_of_list = 0

        prev = p
        p = p.next

    if count == 1:
        if result_prev == None:
            return next_save

        result_prev.next = next_save

    return first


k = Node(4)
k = wstaw(k, 7)
k = wstaw(k, 8)
k = wstaw(k, 9)
k = wstaw(k, 10)
k = wstaw(k, 4)
k = wstaw(k, 6)
k = wstaw(k, 7)
k = wstaw(k, 8)
k = wstaw(k, 9)
k = wstaw(k, 10)


wypisz(k)
k = get_longest(k)
wypisz(k)




