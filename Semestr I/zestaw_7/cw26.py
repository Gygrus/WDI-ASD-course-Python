"""
Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w
drugiej. Do funkcji należy przekazać wskazania na pierwsze elementy obu
list, funkcja powinna zwrócić wartość logiczną.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def wypisz(first):
    napis = ""
    while first is not None:
        #print(f"{first.val} ---> ", end='')
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

def get_length(first):
    length = 0
    while first != None:
        length += 1
        first = first.next
    return length

def if_in(first_one, second_one):

    p, q = first_one, second_one
    if get_length(first_one) > get_length(second_one):
        p, q = q, p

    tab = [None for _ in range(get_length(p))]
    counter = 0
    while p != None:
        compare = q
        check = False
        sub_counter = 1
        while compare != None:
            if compare.val == p.val:
                if compare.val in tab and sub_counter <= tab.count(compare.val):
                    sub_counter += 1
                else:
                    tab[counter] = compare.val
                    counter += 1
                    check = True
                    break
            compare = compare.next
        if not check:
            return False
        p = p.next

    return True


def if_in_v2(first_one, second_one):
    p, q = first_one, second_one
    if get_length(first_one) < get_length(second_one):
        p, q = q, p
    if first_one == None or second_one == None:
        return True

    while p != None:
        if q.val == p.val:
            q_1 = q
            p_1 = p
            result = True
            while q_1.next != None and p_1.next != None:
                q_1 = q_1.next
                p_1 = p_1.next
                if q_1.val != p_1.val:
                    result = False
                    break

            if result:
                return True
        p = p.next

    return False

a1 = Node(18)
a1 = wstaw(a1, 4)
a1 = wstaw(a1, 18)
a1 = wstaw(a1, 2)
a1 = wstaw(a1, 73)
a1 = wstaw(a1, 412)
a1 = wstaw(a1, 18)
a1 = wstaw(a1, 7)
a1 = wstaw(a1, 7)
a1 = wstaw(a1, 59)
a1 = wstaw(a1, 42)
a2 = Node(2)
a2 = wstaw(a2, 73)
a2 = wstaw(a2, 412)
a2 = wstaw(a2, 18)
a3 = None
a4 = Node(18)
wypisz(a1)
wypisz(a2)
#print(if_in(a2, a1))
print(if_in_v2(a2, a4))

