class Node:
    def __init__(self, val, n=None):
        self.value = val
        self.next = n


class Set:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_in(self, x: int):
        if self.head is None:
            return False
        else:
            nod = self.head
            while nod.value < x and not(nod.next is None):
                nod = nod.next
            if nod.value == x:
                return True
            else:
                return False

    # pewnie da się to zrobić krócej
    def add(self, x: int):
        if self.length == 0:
            self.head = Node(x)
            self.length += 1
        elif self.length == 1:
            if x < self.head.value:
                nod = Node(x, self.head)
                self.head = nod
                self.length += 1
            elif x > self.head.value:
                self.head.next = Node(x)
                self.length += 1
        else:
            if x < self.head.value:
                nod = Node(x, self.head)
                self.head = nod
                self.length += 1
            elif x > self.head.value:
                prev = self.head
                nod = prev.next
                while not(nod is None) and x > nod.value:
                    prev = nod
                    nod = nod.next
                if nod is None:
                    prev.next = Node(x)
                    self.length += 1
                    self.length += 1
                elif nod.value > x:
                    x_nod = Node(x, nod)
                    prev.next = x_nod
                    self.length += 1

    def __repr__(self):
        if self.length == 0:
            return "Set is empty"
        else:
            nod = self.head
            ans = ''
            while not(nod is None):
                ans += str(nod.value) + ", "
                nod = nod.next
            return ans[:len(ans)-2]

    def remove(self, x: int):
        if self.length == 1:
            if self.head.value == x:
                self.head = None
                self.length -= 1
        elif self.length > 1:
            if self.head.value == x:
                self.head = self.head.next
                self.length -= 1
            else:
                prev = self.head
                nod = prev.next
                while not(nod is None) and x > nod.value:
                    prev = nod
                    nod = nod.next
                if nod.value == x:
                    prev.next = nod.next
                    self.length -= 1
