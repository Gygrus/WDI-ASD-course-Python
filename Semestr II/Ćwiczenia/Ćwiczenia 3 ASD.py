"""1. Proszę zaimplementować algorytm QuickSort do sortowania n elementowej tablicy tak, żeby
zawsze używał najwyżej O(log n) dodatkowej pamięci na stosie, niezależnie od jakości podziałów w funkcji
partition."""

from random import randint

def partition(T, p, r):
    pivot = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def rec_quick_sort(T, p, r):
    if p < r:
        q = partition(T, p, r)
        rec_quick_sort(T, p, q-1)
        rec_quick_sort(T, q+1, r)

counter = 0
max_counter = 0

def rec_quick_sort2(T, p, r):
    global counter, max_counter
    counter += 1
    max_counter = max(max_counter, counter)
    while p < r:
        q = partition(T, p, r)
        rec_quick_sort2(T, p, q-1)
        p = q+1
    counter -= 1


def rec_quick_sort3(T, p, r):
    global counter, max_counter
    counter += 1
    max_counter = max(max_counter, counter)
    while p < r:
        q = partition(T, p, r)
        if q-p+1<r-q:
            rec_quick_sort3(T, p, q-1)
            p = q+1
        else:
            rec_quick_sort3(T, q+1, r)
            r = q-1

    counter -= 1
#
# counter = 0
# max_counter = 0
#
# n = 20
# t = [randint(10, 99) for _ in range(n)]
# t.sort()
# t2 = t[:]
# #t.sort()
# print(t)
#
# counter = 0
# max_counter = 0
# rec_quick_sort2(t, 0, n-1)
# print(t)
# print(max_counter)
#
# counter = 0
# max_counter = 0
# rec_quick_sort3(t2, 0, n-1)
# print(t)
# print(max_counter)


"""2. Proszę zaimplementować funkcję wstawiającą dowolny element do kopca binarnego"""


def insert(T, ele):
    T.append(ele)
    current_index = len(T) - 1
    while current_index != 0:
        parent = (current_index -1) // 2
        if T[parent] < T[current_index]:
            T[parent], T[current_index] = T[current_index], T[parent]
            current_index = parent
        else:
            break


"""3. Proszę zaimplementować algorytm QuickSort bez użycia rekurencji (ale można wykorzystać
własny stos)."""

def quicksort(T):
    n = len(T)
    stack = []
    stack.append((0, n))
    while len(stack) > 0:
        p, r = stack.pop()
        if p < r:
            q = partition(T, p, r)
            stack.append((p, q-1))
            stack.append((q+1, r))
