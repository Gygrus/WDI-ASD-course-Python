"""
Proszę napisać funkcję scalającą dwie posortowane listy w jedną
posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
- funkcja iteracyjna,
- funkcja rekurencyjna.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


def iter_merge_lists(node_1, node_2):
    """if node_1 == None:
        return node_2
    if node_2 == None:
        return node_1"""

    # if node_1.data < node_2.data:
    #     res_head = node_1
    #     node_1 = node_1.next
    # else:
    #     res_head = node_2
    #     node_2 = node_2.next
    res_head = Node()
    curr_node = res_head
    while node_1 != None and node_2 != None:
        if node_1.data < node_2.data:
            curr_node.next = node_1
            curr_node = curr_node.next
            node_1 = node_1.next
        else:
            curr_node.next = node_2
            curr_node = curr_node.next
            node_2 = node_2.next

    if node_1 == None:
        curr_node.next = node_2
    else:
        curr_node.next = node_1

    return res_head.next

def scal_reku(z1, z2):
    if z1 == None:
        return z2
    if z2 == None:
        return z1
    if z1.dane < z2.dane:
        result = z1
        result.next = scal_reku(z1.next, z2)
    else:
        result = z2
        result.next = scal_reku(z1, z2.next)
    return result