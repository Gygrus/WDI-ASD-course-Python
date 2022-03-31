"""
 Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
kolejność jej elementów.
"""

class Node:
     def __init__(self, val):
         self.val = val
         self.next = None

def reverse(first):
    p = None
    q = first
    while q != None:
        r = q.next
        q.next = p
        p = q
        q = r

    return p 
