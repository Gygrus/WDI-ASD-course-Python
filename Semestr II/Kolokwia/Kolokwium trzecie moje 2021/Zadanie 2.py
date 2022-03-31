# Piotr Socała
"""
Schodzę do poszczególnych węzłów, zapisując ich wartości, a następnie rekurencyjnie schodzę do coraz niższych, sprawdzając, czy
usunięcie ich da mniejszą sumę niż dotychczasowego usuniętego węzła
"""
class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def cutthetree(T):
    counter = 0
    tab = []
    def rekur(node):
        if node.right is not None and node.left is not None:
            current = node.value
            return min(current, rekur(node.left) + rekur(node.right))
        elif node.right is None and node.left is None:
            return float('inf')
        else:
            if node.right is None:
                return min(node.val, rekur(node.left))
            else:
                return min(node.val, rekur(node.right))

    counter += rekur(T.left)
    counter += rekur(T.right)
    return counter


