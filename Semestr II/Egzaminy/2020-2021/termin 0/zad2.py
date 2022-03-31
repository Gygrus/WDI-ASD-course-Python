"""
Dane jest drzewo binarne T, gdzie każda krawędź ma pewną wartość. Proszę zaimplementować
funkcję:
def valuableTree(T, k):
...
która zwraca maksymalną sumę wartości k krawędzi tworzących spójne poddrzewo drzewa T.
Funkcja powinna być jak najszybsza. Proszę oszacować złożoność czasową oraz pamięciową zastosowanego algorytmu.
Drzewo T reprezentowane jest przez obiekty klasy Node:
class Node:
def __init__(self):
self.left = None # lewe poddrzewo
self.leftval = 0 # wartość krawędzi do lewego poddrzewa jeśli istnieje
self.right = None # prawe poddrzewo
self.rightval = 0 # wartość krawędzi do prawego poddrzewa jeśli istnieje
self.X = None # miejsce na dodatkowe dane
Pole X można wykorzystać do przechowywania dodatkowych informacji w trakcie obliczeń.
"""
from queue import Queue

class Node:
    def __init__(self, val):
        self.left = None # lewe poddrzewo
        self.leftval = 0 # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = None # prawe poddrzewo
        self.rightval = 0 # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X = None # miejsce na dodatkowe dane
        self.val = val

# def valuableTree(T, k):
#     def rekur(node, k, i, res):
#         if i == 0:
#             return res
#         if node.left is None and node.right is None and i > 0:
#             return None
#         temp = res
#         if node.left is not None and node.right is not None:
#             for x in range(1, i):
#                 # print(x)
#                 if rekur(node.left, k, x-1, res+node.leftval) is not None and rekur(node.right, k, i-x-1, res + node.rightval) is not None:
#                     temp = max(temp, res + rekur(node.left, k, x-1, node.leftval) + rekur(node.right, k, i-x-1, node.rightval))
#                 # print("a", temp)
#             a = rekur(node.left, k, i-1, res+node.leftval)
#             b = rekur(node.right, k, i-1, res+node.rightval)
#             if a is not None:
#                 temp = max(temp, rekur(node.left, k, i-1, res+node.leftval))
#             # print("b", temp)
#             if b is not None:
#                 temp = max(temp, rekur(node.right, k, i-1, res+node.rightval))
#             # print("c", temp)
#         elif node.left is None and node.right is not None:
#             if rekur(node.right, k, i-1, res+node.rightval) is not None:
#                 temp = max(temp, rekur(node.right, k, i-1, res+node.rightval))
#
#         elif node.right is None and node.left is not None:
#             if rekur(node.left, k, i-1, res+node.leftval) is not None:
#                 temp = max(temp, rekur(node.left, k, i-1, res+node.leftval))
#
#         # print(temp, node.leftval, node.rightval)
#
#         return temp
#
#     best = 0
#     curr = T
#     q = Queue()
#     q.put(curr)
#     while not q.empty():
#         curr = q.get()
#         if rekur(curr, k, k, 0) is not None:
#             best = max(best, rekur(curr, k, k, 0))
#             # print("best = ", best, "curr = ", curr.val)
#         if curr.left is not None:
#             q.put(curr.left)
#         if curr.right is not None:
#             q.put(curr.right)
#
#     return best

def valuabletree(T, k):
    counter = 0
    def rekur(node):
        if node is None:
            return
        nonlocal counter
        counter += 1
        rekur(node.left)
        rekur(node.right)

    for x in range()

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
A.leftval = 1
A.rightval = 5
A.left = B
A.right = E
B.leftval = 6
B.rightval = 2
B.left = D
B.right = C
C.leftval = 8
C.rightval = 10
C.left = F
C.right = G

print(valuableTree(A, 3))