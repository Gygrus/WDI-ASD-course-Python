"""
Zbiór mnogościowy zawierający napisy jest reprezentowany w postaci
jednokierunkowej listy. Napisy w łańcuchu są uporządkowane
leksykograficznie. Proszę napisać stosowne definicje typów oraz funkcję
dodającą napis do zbioru. Do funkcji należy przekazać wskaźnik do listy
oraz wstawiany napis, funkcja powinna zwrócić wartość logiczną wskazującą,
czy w wyniku operacji moc zbioru uległa zmianie.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def czy_wieksza(string1, string2):
    for x in range(max(len(string1), len(string2))):
        if x >= len(string1):
            return False

        if x >= len(string2):
            return True

        if ord(string1[x]) == ord(string2[x]):
            continue

        elif ord(string1[x]) > ord(string2[x]):
            return True

        elif ord(string1[x]) < ord(string2[x]):
            return False

    return False

def append(first, string):
    if first == None:
        first = Node(string)
        print("True")
        return first

    new = Node(string)
    prev = None
    p = first
    while p != None and czy_wieksza(string, p.val):
        prev = p
        p = p.next

    if not p:
        prev.next = new
        print("True")
        return first

    if string == p.val:
        print('False')
        return first

    if not prev:
        new.next = p
        print("True")
        return new


    prev.next = new
    new.next = p
    print("True")
    return first

def wypisz(first):
    while first is not None:
        #print(first)
        print(first.val, '--->', end='')
        first = first.next
    print()

a = Node('aeww')
a = append(a, 'abc')
a = append(a, 'gsdg')
a = append(a, 'qwfs')
a = append(a, 'babajaga')
a = append(a, 'zabajaga')
a = append(a, 'zabajaga')
a = append(a, 'aewww')
wypisz(a)


#print(czy_wieksza('aeww', 'abfse'))