"""zadanie 1"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def create(T):
    first = None
    T.reverse()
    for el in T:
        p = Node(el)
        p.next = first
        first = p

    return first

def write(first):
    while first is not None:
        print(first.value, end=' ')
        first = first.next
    print()

# first1 = create([1, 5, 4, 6, 3])
# write(first1)

"""Sortowanie przez wybieranie"""

#def wybieranie(first):
def get_max(wart):
    max_prev = wart
    max = wart.next
    q = wart
    p = wart.next

    while p is not None:
        if p.value > max.value:
            max_prev = q
            max = p

        q = p
        p = p.next

    if max is not None:
        max_prev.next = max.next

    return max

def insertion_sort(first):
    usortedList = Node()
    usortedList.next = first

    sortedList = None
    while usortedList.next is not None:
        max = get_max(usortedList)
        max.next = sortedList
        sortedList = max

    return sortedList


# list1 = create([40, 5, 4, 6, 3, 4, 7, 900])
# write(list1)
#
# list2 = insertion_sort(list1)
# write(list2)
#
# m = get_max(list1)



"""Zadanie 7"""

def find_sum(T, x):
    l, p = 0, len(T)-1
    sum = T[l] + T[p]
    while l < p:
        if sum > x:
            p -= 1
        elif sum < x:
            l += 1
        else:
            return l, p
        sum = T[l] + T[p]

    return None


T = [2, 3, 6, 20, 28, 36, 58, 100, 1924, 2021]
print(find_sum(T, 120))

"""Zadanie 4 (jednocześnie min i max w 1.5n porównań)"""

def naj(T):
    min = T[0]
    max = T[0]
    i = len(T)%2
    while i < len(T):
        if T[i] < T[i+1]:
            if T[i] < min:
                min = T[i]
            if T[i+1] > max:
                max = T[i+1]
        else:
            if T[i] > max:
                max = T[i]
            if T[i+1] < min:
                min = T[i+1]
        i += 2

    return min, max

print(naj([1, 3, 3, 2, 6, 7, 3, 9, 12, 13]))