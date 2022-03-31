"""
Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do
10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy
należy połączyć w jedną listę odsyłaczową, która jest posortowana
niemalejąco według ostatniej cyfry pola val.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def f(ptr):
    firsts = [None for _ in range(10)]
    lasts = [None for _ in range(10)]
    while ptr is not None:
        last_dig = ptr.val % 10
        if firsts[last_dig] is None:
            firsts[last_dig] = lasts[last_dig] = ptr
        else:
            lasts[last_dig].next = ptr
            lasts[last_dig] = ptr

        ptr = ptr.next

    first = None
    for i in range(10):
        if firsts[i] is not None:
            if first is None:
                first = first[i]
                last = lasts[i]
            else:
                last.next = firsts[i]
                last = last[i]
    last.next = None
    return first

    first = None
    for i in range(9, -1, -1):
        if first[i] is not None:
            lasts[i].next = first
            first = firsts[i]
    return first
