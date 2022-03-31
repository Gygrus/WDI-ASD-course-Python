"""
Pewien eksperyment fizyczny daje w wyniku liczby rzeczywiste postaci a
x
, gdzie a to pewna stała większa od 1 (a > 1) zaś x to liczby rzeczywiste rozłożone równomiernie na przedziale [0, 1].
Napisz funkcję fast sort, która przyjmuje tablicę liczb z wynikami eksperymentu oraz stałą a i
zwraca tablicę z wynikami eksperymentu posortowanymi rosnąco. Funkcja powinna działać możliwie jak najszybciej. Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność
obliczeniową. Nagłówek funkcji fast sort powinien mieć postać:
"""

# a^(1/n) - 1 -> kubełek
# (a^x - 1)%(a^(1/n) - 1) -> przypasowanie do kubełka

class Node:
    def __init__(self):
        self.val = None
        self.next = None

def ln(x):
    n = 1000.0
    return n * ((x**(1/n))-1)

def log_temp(a, x):
    return ln(x) / ln(a)

def fast_sort(tab, a):
    n = len(tab)
    bucket = (1/n)
    print(bucket)
    new = [Node() for _ in range(n)]
    for x in range(n):
        node = Node()
        node.val = tab[x]
        get_val = log_temp(a, tab[x])
        print(int((get_val)//bucket))
        guard = new[int(get_val//bucket)]
        check = False
        while guard.next is not None:
            if guard.next.val > node.val:
                temp = guard.next
                guard.next = node
                node.next = temp
                check = True
                break
            guard = guard.next

        if not check:
            guard.next = node

    for x in range(n):
        guard = new[x]
        while guard.next is not None:
            print(guard.next.val, "---> ", end='')
            guard = guard.next
        print()

    first = Node()
    temp = first
    for x in range(n):
        if new[x].next is not None:
            temp.next = new[x].next
            while temp.next is not None:
                temp = temp.next

    temp = first.next
    for x in range(n):
        tab[x] = temp.val
        temp = temp.next

    print(tab)




tab = [1.631, 1.478, 1.039, 1.894, 1.670, 1.586, 3.737, 2.732, 1.698, 2.042]
print(fast_sort(tab, 4))