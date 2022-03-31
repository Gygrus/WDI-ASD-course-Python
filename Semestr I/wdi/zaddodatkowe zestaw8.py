from random import choice

class Node:
    def __init__(self):
        self.right = None
        self.down = None

W = 4
K = 5

T = [[choice([True, False]) for _ in range(K)] for _ in range(W)]
for x in T:
    print(x)
TW = [None for _ in range(W)]
TK = [None for _ in range(K)]


m = len(T)
n = len(T[0])
for w in range(W-1, -1, -1):
    for k in range(K-1, -1, -1):
        if T[w][k]:
            head = Node()
            head.right = TW[w]
            head.down = TK[k]
            TW[w] = TK[k] = head
