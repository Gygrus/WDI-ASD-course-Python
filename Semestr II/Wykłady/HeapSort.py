def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return (i - 1)//2

def heapify(A, n, i):           #"Naprawia" dany element i całą podgałąź
    l = left(i)
    r = right(i)
    m = i
    if l < n and A[l] > A[m]:
        m = l

    if r < n and A[r] > A[m]:
        m = r

    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify(A, n, m)

def buildheap(A):               #Buduje kopiec (typu maxheap)
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A, n, i)

def heapsort(A):                #Sortuje powstały kopiec (najpierw go inicjalizując za pomocą buildheap)
    n = len(A)
    buildheap(A)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]  #Przemieszcza największy element na ostatnie miejsce
        heapify(A, i, 0)         #"Naprawia" kopiec, ale nie rusza już ostatniego (największego) elementu


def heap_insert(A, x):
    n = len(A)
    A.append(x)
    while n >= 1 and A[parent(n)] < x:
        A[n] = A[parent(n)]
        n = parent(n)
    A[n] = x

def extract_max(A):
    n = len(A)
    if n < 1:
        return "Kopiec jest pusty"

    max = A[0]
    A[0] = A[n-1]
    heapify(A, n-1, 0)
    return max

def extract_max_z_popem(A):
    n = len(A)
    if n < 1:
        return "Kopiec jest pusty"

    A[0], A[n-1] = A[n-1], A[0]
    max = A.pop()
    heapify(A, n-1, 0)
    return max

T = [5, 10, 12, 7, 8, 1, 9]
print(T)
buildheap(T)
print(T)
heap_insert(T, 6)
print(T)
extract_max_z_popem(T)
print(T)