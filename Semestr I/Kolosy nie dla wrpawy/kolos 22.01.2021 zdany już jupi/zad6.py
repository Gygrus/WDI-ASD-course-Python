#Piotr Socała
# przechodzę po kolejnych elementach listy odsyłaczowej,
# porównując kolejne elementy z pierwszej do kolejnych,
# jeśli wartości się zgadzają, dążę do operacji tworzenia zbioru
# mnogościowego
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def iloczyn(z1, z2, z3):
    if z1 == None or z2 == None or z3 == None:
        return None
    p = z1
    q = z2
    t = z3
    new = None
    result = None
    while p != None:
        while q != None and q.val < p.val:
            q = q.next

        if q != None and q.val == p.val:
            while t != None and t.val < p.val:
                t = t.next
            if t != None and t.val == q.val:
                t_1 = t.next
                if new == None:
                    new = t
                    result = new
                    new.next = None
                else:
                    new.next = t
                    new = new.next
                    new.next = None
                t = t_1

        p = p.next

    return result

#end def


