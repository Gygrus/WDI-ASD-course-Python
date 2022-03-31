"""
Kopiec z najmniejszą wartością na pierwszym miejscu
"""
def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return (i - 1)//2


def minHeapify(A, n, i):
    l = left(i)
    r = right(i)
    m = i

    if l < n and A[l] < A[m]:
        m = l

    if r < n and A[r] < A[m]:
        m = r

    if m != i:
        A[m], A[i] = A[i], A[m]
        minHeapify(A, n, m)


def buildminheap(A):
    n = len(A)
    for x in range(parent(n-1), -1, -1):
        minHeapify(A, n, x)


def insert_minheap(A, x):
    n = len(A)
    A.append(x)
    i = n
    while i > 0 and A[parent(i)] > x:
        A[i] = A[parent(i)]
        i = parent(i)
    A[i] = x

def extract_min(A):
    n = len(A)
    if n < 1:
        return "Kopiec jest pusty"

    A[n-1], A[0] = A[0], A[n-1]
    min = A[n-1]
    minHeapify(A, n-1, 0)
    return min

def extract_min_z_popem(A):
    n = len(A)
    if n < 1:
        return "Kopiec jest pusty"

    A[n-1], A[0] = A[0], A[n-1]
    min = A.pop()
    minHeapify(A, n-1, 0)
    return min


T = [9, 10, 7, 5, 11, 6, 13]
buildminheap(T)
print(T)
insert_minheap(T, 2)
print(T)
insert_minheap(T, 9)
print(T)
k = extract_min_z_popem(T)
print(T, k)