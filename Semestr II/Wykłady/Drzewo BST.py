class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def find(root, key):
    while root != None:
        if root.key ==  key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right

    return None

# zakładam że root to nie None
def BST_insert(new, root):
    while True:
        if root.key > new.key:
            if root.left is None:
                root.left = new
                new.parent = root
                return
            root = root.left

        elif root.key < new.key:
            if root.right is None:
                root.right = new
                new.parent = root
                return
            root = root.right


def remove(key, root):
    if root is None:
        return root

    node = find(root, key)

    if node.left is None:
        rem = node.right
        if rem is None:
            node = rem
        else:
            node.key = rem.key
            remove(rem.key, rem)
        return

    elif node.right is None:
        rem = node.left
        if rem is None:
            node = rem
        else:
            node.key = rem.key
            remove(rem.key, rem)

        return

    temp = next(root, node.key)
    node.key = temp.key
    remove(temp.key, temp)





def max(root):
    while root.right != None:
        root = root.right
    # tu zwracaj samego roota!
    return root

def min(root):
    while root.left != None:
        root = root.left
    # tu zwracaj samego roota!
    return root

def find_max(root):
    while root.parent is not None:
        root = root.parent

    return max(root)

def find_min(root):
    while root.parent is not None:
        root = root.parent

    return min(root)

def prev(root, key):
    node = find(root, key)
    if node.left is not None:
        node = node.left
        return max(node)

    while node.parent is not None:
        if node.parent.right == node:
            # tu zwracaj samego node'a!
            return node.parent
        node = node.parent

    return None


def next(root, key):
    node = find(root, key)
    if node.right is not None:
        node = node.right
        return min(node)

    while node.parent is not None:
        if node.parent.left == node:
            # tu zwracaj samego node'a!
            return node.parent
        node = node.parent

    return None

A = BSTNode(21)
B = BSTNode(37)
C = BSTNode(15)
D = BSTNode(20)
E = BSTNode(5)
F = BSTNode(7)
G = BSTNode(40)
H = BSTNode(25)
I = BSTNode(13)
J = BSTNode(8)
tab = [B, C, D, E, F, G, H, I, J]
for x in range(9):
    BST_insert(tab[x], A)

print(find_max(A).key)
print(find_min(A).key)
print(D.parent.key)
print(prev(A, 20).key)
print(next(A, 13).key)
remove(15, A)
print(prev(A, 20).key)
