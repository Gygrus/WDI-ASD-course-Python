from random import randint, seed
from time import time

def mergesort(T):
    # Subfunctions
    def rec_mergesort(A, B, beg, end):  # recursive function that performs mergesort
        if end - beg == 1:
            return

        mid = (end + beg) // 2

        rec_mergesort(B, A, beg, mid)
        rec_mergesort(B, A, mid, end)

        merge(B, A, beg, mid, end)  # treat B as a soure for sorting A

    def merge(A, B, beg, mid, end):  # merge from arg A to arg B, beg is inclusive, end is exclusive
        j = beg
        k = mid

        for i in range(beg, end):

            if (k == end or A[j] <= A[k]) and j < mid:
                B[i] = A[j]
                j += 1
            else:
                B[i] = A[k]
                k += 1

    def copy_arr(A, B):  # from A to B
        for i in range(len(A)):
            B[i] = A[i]

    A = T  # for convenience in naming
    n = len(A)
    B = [0] * n
    copy_arr(A, B)
    rec_mergesort(A, B, 0, n)
    return A


seed(42)

n = 10
T = [randint(-100000, 100000) for i in range(1000000)]

print("przed sortowaniem: T =", T)
start = time()
T = mergesort(T)
end = time()
print("po sortowaniu    : T =", T)
print(end-start)
for i in range(len(T) - 1):
    if T[i] > T[i + 1]:
        print("Błąd sortowania!")
        exit()

print("OK")