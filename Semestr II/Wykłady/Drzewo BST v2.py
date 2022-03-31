class BSTNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def print_tree(root):
    if root is None:
        print("Empty!")
        return
    def inorder(root):
        if root is not None:
            inorder(root.left)
            print(root.key, end=" ")
            inorder(root.right)
    inorder(root)
    print()

def insert(root, key):
    if root is None:
        return BSTNode(key)

    node = root
    while True:
        if node.key > key:
            if node.left is None:
                node.left = BSTNode(key)
                node.left.parent = node
                return root
            node = node.left

        elif node.key < key:
            if node.right is None:
                node.right = BSTNode(key)
                node.right.parent = node
                return root
            node = node.right

        else:
            print("ten element już istnieje")
            return root

def find(root, key):
    if root is None:
        return None
    if root.key == key:
        return root

    if root.key > key:
        return find(root.left, key)
    elif root.key < key:
        return find(root.right, key)

def find_min(root):
    node = root
    while node.left is not None:
        node = node.left

    return node

def find_max(root):
    node = root
    while node.right is not None:
        node = node.right

    return node

def prev(root, key):
    node = find(root, key)
    if node is not None:
        if node.left is not None:
            node = node.left
            return find_max(node)
        else:
            rem = node
            node = node.parent
            while node is not None:
                if node.right == rem:
                    return node
                rem = node
                node = node.parent
            return None

    return None

def next(root, key):
    node = find(root, key)
    if node is not None:
        if node.right is not None:
            node = node.right
            return find_min(node)
        else:
            rem = node
            node = node.parent
            while node is not None:
                if node.left == rem:
                    return node
                rem = node
                node = node.parent
            return None

    return None

def remove(root, key):
    if root is None:
        return None

    node = find(root, key)
    if node is not None:
        if node.left is None and node.right is None:
            if node.parent is not None:
                print('gówienko', node.key)
                if node.parent.right == node:
                    node.parent.right = None
                elif node.parent.left == node:
                    node.parent.left = None
            else:
                return None

        elif node.left is None:
            if node.parent is not None:
                save = node.right
                if node.parent.right == node:
                    node.parent.right = save
                    save.parent = node.parent
                elif node.parent.left == node:
                    node.parent.left = save
                    save.parent = node.parent

                node.parent = None
            else:
                node.right.parent = None
                return node.right

        elif node.right is None:
            if node.parent is not None:
                save = node.left
                if node.parent.right == node:
                    node.parent.right = save
                    save.parent = node.parent
                elif node.parent.left == node:
                    node.parent.left = save
                    save.parent = node.parent

                node.parent = None
            else:
                node.left.parent = None
                return node.left

        else:
            new = next(node, node.key)
            node.key = new.key
            remove(new, new.key)

    return root

root = None
root = insert(root, 21)
root = insert(root, 37)
root = insert(root, 15)
root = insert(root, 63)
root = insert(root, 25)
print_tree(root)
# print(prev(root, 63).key)
# root = remove(root, 37)
# print_tree(root)
# print(prev(root, 63).key)
# print(prev(root, 25).key)
# print(next(root, 25).key)
# print(next(root, 21).key)
# print(next(root, 15).key)
root = insert(root, 5)
root = insert(root, 7)
root = insert(root, 13)
root = insert(root, 8)
# print_tree(root)
# root = insert(root, 20)
print_tree(root)
root = remove(root, 21)
root = remove(root, 25)
root = remove(root, 37)
# root = remove(root, 37)
# print(find(root, 63).left, find(root, 63).right)
print_tree(root)
# print(find(root, 15).left.key, find(root, 15).right.key)
root = remove(root, 15)
root = remove(root, 63)
root = remove(root, 5)
root = remove(root, 8)
root = remove(root, 13)
root = remove(root, 7)
print_tree(root)
# # print(find(root, 15))
# print(find_min(root).key)
gowno = None
gowno = insert(gowno, 3)
gowno = insert(gowno, 6)
gowno = remove(gowno, 3)
print(find(gowno, 6).right, find(gowno, 6).left, find(gowno, 6).parent)
gowno = remove(gowno, 6)
print_tree(gowno)
