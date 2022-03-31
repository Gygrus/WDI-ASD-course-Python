"""
Dana jest lista, który zakończona jest cyklem.
Napisać funkcję, która zwraca liczbę elementów w cyklu.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



def ile_elem(head):
    p = head
    q = head

    while True:
        p = p.next
        q = q.next.next

        if q == p:
            cnt = 1
            p = p.next

            while p != q:
                p = p.next
                cnt += 1
            return cnt

def ile_elem2(head):
    p = head
    q = head.next

    while p != q:
        p = p.next
        q = q.next.next

    cnt = 1
    p = p.next

    while p != q:
        p = p.next
        cnt += 1
        
    return cnt