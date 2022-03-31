"""
 Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
struktury listy odsyłaczowej.
- czy element należy do zbioru
- wstawienie elementu do zbioru
- usunięcie elementu ze zbioru
"""

class Node:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class LList:
    def __init__(self):
        self.first = None


    def wypisz(self):
        if self.first is None:
            return None
        mark = self.first
        while mark is not None:
            print(mark.val, '--> ', end='')
            mark = mark.next

    def czy_w(self, x):
        if self.first is None:
            return False

        mark = self.first
        while mark.next is not None:
            if mark.val == x:
                return True
            mark = mark.next
        if mark.val == x:
            return True
        return False

    def dodaj(self, x):
        if self.first == None:
            self.first = Node(x)
        else:
            mark = self.first
            z = True
            while mark.next is not None:
                if mark.val == x:
                    z = False
                    break
                mark = mark.next
            if mark.val != x and z:
                mark.next = Node(x)

    def usun(self, x):
        mark = self.first
        if mark.val == x:
            if mark.next is not None:
                self.first = self.first.next
        else:
            z = None
            while mark is not None:
                if mark.val == x:
                    z.next = mark.next
                    break
                z = mark
                mark = mark.next






zbior = LList()
zbior.dodaj(6)
zbior.dodaj(7)
zbior.usun(6)
zbior.dodaj(13)
zbior.dodaj(52)
zbior.dodaj(35)
zbior.dodaj(72)
zbior.usun(24)
zbior.usun(7)
zbior.usun(72)

zbior.wypisz()
print(zbior.czy_w(52))