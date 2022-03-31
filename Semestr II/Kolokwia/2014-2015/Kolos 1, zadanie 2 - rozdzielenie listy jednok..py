"""
Dane są następujące struktury:

struct Node { Node* next; int val; };
struct TwoLists { Node* even; Node* odd; };

Napisać funkcję: TwoLists split(Node* list);
Funkcja rozdziela listę na dwie: jedną zawierającą liczby parzyste i drugą zawierającą liczby
nieparzyste. Listy nie zawierają wartowników.
"""

"""
Za pomocą wskaźników przechodzę po liście i wypinam spójne fragmenty elementów parzystych/nieparzystych, 
a następnie przepinam je do dwóch list wyjściowych.
Złożoność: O(n)"""
from random import randint
from time import time


class Node:
    def __init__(self):
        self.next = None
        self.value = None


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")

def check_if_even(x):
    if x.value % 2 == 0:
        return True

    return False



def TwoListsSplit(first):
    guard_original = Node()
    guard_original.next = first
    guard_ev = Node()
    even_last = guard_ev
    guard_un = Node()
    uneven_last = guard_un

    while guard_original.next is not None:
        if check_if_even(guard_original.next):
            pointer = guard_original.next
            while pointer.next is not None and check_if_even(pointer.next):
                pointer = pointer.next

            start = guard_original.next
            guard_original.next = pointer.next
            pointer.next = None
            even_last.next = start
            even_last = pointer

        else:
            pointer = guard_original.next
            while pointer.next is not None and not check_if_even(pointer.next):
                pointer = pointer.next

            start = guard_original.next
            guard_original.next = pointer.next
            pointer.next = None
            uneven_last.next = start
            uneven_last = pointer

    return guard_un.next, guard_ev.next

n = 100000
m = 10000000
T = [randint(1, m) for _ in range(n)]
T = tab2list(T)
#printlist(T)
start = time()
A, B = TwoListsSplit(T)
end = time()
#printlist(A)
#printlist(B)
print(end-start)


