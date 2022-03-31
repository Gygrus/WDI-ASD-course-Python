"""
Zastosowanie listy odsyłaczowej do implementacji
tablicy rzadkiej. Proszę napisać trzy funkcje:
– inicjalizującą tablicę,
– zwracającą wartość elementu o indeksie n,
– podstawiającą wartość value pod indeks n.
"""

class Node:
    def __init__(self, val=0, next=None, i = -1):
        self.val = val
        self.next = next
        self.i = i


class Tab:
    def __init__(self, length):
        self.first = None
        self.length = length

    def print_tab(self):
        mark = self.first
        k = 0
        sign = ''
        while mark is not None:
            for x in range(k, mark.i):
                sign += str(0) + ' ---> '
            sign += f'{mark.val}' + ' ---> '
            k = mark.i+1
            mark = mark.next
        for x in range(k, self.length):
            sign += str(0) + ' ---> '
        return sign[:-5]

    def print_n(self, n):
        if n < self.length:
            mark = self.first
            while mark is not None:
                if mark.i == n:
                    print(mark.val)
                    return
                mark = mark.next
            print(Node().val)


    def append_n(self, val, n):
        if n >= self.length:
            return
        mark = self.first
        if mark is None:
            self.first = Node(val, None, n)
            return

        if mark.i > n:
            p = Node(val, self.first, n)
            self.first = p
            return

        if mark.i == n:
            self.first = Node(val, self.first.next, n)
            return

        mark_next = mark.next
        if mark_next is None:
            mark.next = Node(val, None, n)
            return

        while mark_next is not None:
            #print(mark.val, val)
            if mark.i == n:
                #print('góowno')
                mark = Node(val, mark.next, mark.i)
                current.next = mark
                return
            if mark_next.i <= n:

                current = mark
                mark = mark.next
                mark_next = mark.next

            if mark_next is None and mark.i < n:
                p = Node(val, mark_next, n)
                mark.next = p
                return
        p = Node(val, mark_next, n)
        current.next = p
        return


z = Tab(53522)
z.append_n(5, 0)
z.append_n(53, 1)
z.append_n(533,1)
z.append_n(23, 1)
z.append_n(2321, 6)
z.append_n(5353, 7)
z.append_n(433, 6)
z.append_n(9, 13)
z.append_n(3, 0)
z.print_n(13)
print(z.print_tab())






