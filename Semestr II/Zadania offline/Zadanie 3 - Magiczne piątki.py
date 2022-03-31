from random import shuffle
"""Magiczne piątki"""


# def linearselect(A, k):
#   def insertionSort(arr):
#     for i in range(1, len(arr)):
#       key = arr[i]
#
#       j = i - 1
#       while j >= 0 and key < arr[j]:
#         arr[j + 1] = arr[j]
#         j -= 1
#       arr[j + 1] = key
#
#   def find_median(T, l, r):
#     new = [0] * r
#     i = 0
#     for x in range(l, l + r):
#       new[i] = T[x]
#       i += 1
#
#     insertionSort(new)
#     return new[r // 2]
#
#   def partition(Tab, p, r, med_of_med):
#     for x in range(p, r):
#       if Tab[x] == med_of_med:
#         Tab[x], Tab[r] = Tab[r], Tab[x]
#         break
#
#     x = Tab[r]
#     i = p - 1
#     for j in range(p, r):
#       if Tab[j] < x:
#         i += 1
#         Tab[i], Tab[j] = Tab[j], Tab[i]
#     Tab[i + 1], Tab[r] = Tab[r], Tab[i + 1]
#     return i + 1
#
#   def magic_fifths(T, l, r, k):
#     if k <= r and k >= l:
#       n = r - l + 1
#       i = 0
#       medians = [0] * ((n + 4) // 5)
#       while i < n // 5:
#         medians[i] = find_median(T, l + i * 5, 5)
#         i += 1
#       if i * 5 < n:
#         medians[i] = find_median(T, l + i * 5, n % 5)
#         i += 1
#
#       if i == 1:
#         med_of_med = medians[0]
#       else:
#         med_of_med = magic_fifths(medians, 0, i - 1, i // 2)
#
#       q = partition(T, l, r, med_of_med)
#       if q == k:
#         return T[q]
#       elif q > k:
#         return magic_fifths(T, l, q - 1, k)
#       else:
#         return magic_fifths(T, q + 1, r, k)
#
#   return magic_fifths(A, 0, len(A) - 1, k)

# def linearselect2(A, k):
#   def insertionSort(arr, l, r):
#     for i in range(l, r):
#       key = arr[i]
#
#       j = i - 1
#       while j >= 0 and key < arr[j]:
#         arr[j + 1] = arr[j]
#         j -= 1
#       arr[j + 1] = key
#
#   def partition(Tab, p, r, med_of_med):
#     for x in range(p, r):
#       if Tab[x] == med_of_med:
#         Tab[x], Tab[r] = Tab[r], Tab[x]
#         break
#
#     x = Tab[r]
#     i = p - 1
#     for j in range(p, r):
#       if Tab[j] < x:
#         i += 1
#         Tab[i], Tab[j] = Tab[j], Tab[i]
#     Tab[i + 1], Tab[r] = Tab[r], Tab[i + 1]
#     return i + 1
#
#   def magic_fifths(T, l, r, k):
#     if k <= r and k >= l:
#       n = r - l + 1
#       i = 0
#       while i < n // 5:
#         insertionSort(T, l + i*5, l + (i*5 + 5))
#         median = (2*l + i*5 + (i*5 + 5)) // 2
#         T[l + i], T[median] = T[median], T[l + i]
#         i += 1
#       if i * 5 < n:
#         insertionSort(T, l + i*5, l + i*5 + n%5)
#         median = (2 * l + i*5 + (i*5 + (n%5))) // 2
#         T[l + i], T[median] = T[median], T[l + i]
#         i += 1
#
#       if i == 1:
#         med_of_med = T[l]
#       else:
#         med_of_med = magic_fifths(T, l, l + (i - 1), i // 2)
#
#       q = partition(T, l, r, med_of_med)
#       if q == k:
#         return T[q]
#       elif q > k:
#         return magic_fifths(T, l, q - 1, k)
#       else:
#         return magic_fifths(T, q + 1, r, k)
#
#   return magic_fifths(A, 0, len(A) - 1, k)

# def linearselect3(T, k):
#   def quicksort1(Tab, p, r):
#     # print(Tab[p:r+1])
#     def quicksort(Tab, p, r):
#       while p < r:
#         q = partition(Tab, p, r)
#         quicksort(Tab, p, q - 1)
#         p = q + 1
#
#     def partition(Tab, p, r):
#       x = Tab[r]
#       i = p - 1
#       for j in range(p, r):
#         if Tab[j] < x:
#           i += 1
#           Tab[i], Tab[j] = Tab[j], Tab[i]
#       Tab[i + 1], Tab[r] = Tab[r], Tab[i + 1]
#       return i + 1
#
#     # print("przed, ",Tab[p:r + 1])
#     quicksort(Tab, p, r)
#     # print("po, ",Tab[p:r + 1])
#
#   def partition(Tab, p, r, med_of_med):
#     for x in range(p, r):
#       if Tab[x] == med_of_med:
#         Tab[x], Tab[r] = Tab[r], Tab[x]
#         break
#
#     x = Tab[r]
#     i = p - 1
#     for j in range(p, r):
#       if Tab[j] < x:
#         i += 1
#         Tab[i], Tab[j] = Tab[j], Tab[i]
#     Tab[i + 1], Tab[r] = Tab[r], Tab[i + 1]
#     return i + 1
#
#   def magic_fifths(T, n):
#     if n <= 1:
#       return
#     number = n // 5
#     i = 0
#     while i < number:
#       quicksort1(T, i * 5, i * 5 + 4)
#       median = (i * 5 + i * 5 + 5) // 2
#       T[i], T[median] = T[median], T[i]
#       i += 1
#     if n % 5 != 0:
#       quicksort1(T, i * 5, i * 5 + n % 5 - 1)
#       median = (i * 5 + i * 5 + n % 5) // 2
#       T[i], T[median] = T[median], T[i]
#       i += 1
#
#     magic_fifths(T, i)
#
#   def select(T, p, r, k):
#     if p == r:
#       return T[p]
#
#     q = partition(T, p, r, k)
#     if q == k:
#       return T[q]
#
#     elif k < q:
#       return select(T, p, q - 1, k)
#
#     else:
#       return select(T, q + 1, r, k)
#
#   n = len(T)
#   magic_fifths(T, n)
#   T[0], T[n - 1] = T[n - 1], T[0]
#
#   return select(T, 0, n - 1, k)

# def linearselect4(T, k):
#   def insertionSort(arr, l, r):
#     for i in range(l + 1, r + 1):
#
#       key = arr[i]
#
#       j = i - 1
#       while j >= l and key < arr[j]:
#         arr[j + 1] = arr[j]
#         j -= 1
#       arr[j + 1] = key
#
#   def partition(Tab, p, r, med_of_med = None):
#     # for x in range(p, r):
#     #   if Tab[x] == med_of_med:
#     #     Tab[x], Tab[r] = Tab[r], Tab[x]
#     #     break
#
#     x = Tab[r]
#     i = p - 1
#     for j in range(p, r):
#       if Tab[j] < x:
#         i += 1
#         Tab[i], Tab[j] = Tab[j], Tab[i]
#     Tab[i + 1], Tab[r] = Tab[r], Tab[i + 1]
#     return i + 1
#
#   def magic_fifths(T, n):
#     if n <= 1:
#       return
#     number = n // 5
#     i = 0
#     while i < number:
#       insertionSort(T, i * 5, i * 5 + 4)
#       median = (i * 5 + i * 5 + 5) // 2
#       T[i], T[median] = T[median], T[i]
#       i += 1
#     if n % 5 != 0:
#       insertionSort(T, i * 5, i * 5 + n % 5 - 1)
#       median = (i * 5 + i * 5 + n % 5) // 2
#       T[i], T[median] = T[median], T[i]
#       i += 1
#
#     magic_fifths(T, i)
#
#   def select(T, p, r, k):
#     if p == r:
#       return T[p]
#
#     q = partition(T, p, r, T[n-1])
#     if q == k:
#       return T[q]
#
#     elif k < q:
#       return select(T, p, q - 1, k)
#
#     else:
#       return select(T, q + 1, r, k)
#
#   n = len(T)
#   magic_fifths(T, n)
#   T[0], T[n - 1] = T[n - 1], T[0]
#
#   return select(T, 0, n - 1, k)


def linearselect(T, k):
    def insertionSort(arr, l, r):
        for i in range(l + 1, r+1):

            key = arr[i]

            j = i - 1
            while j >= l and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def partition(Tab, p, r):

        x = Tab[r]
        i = p-1
        for j in range(p, r):
            if Tab[j] < x:
                i += 1
                Tab[i], Tab[j] = Tab[j], Tab[i]
        Tab[i+1], Tab[r] = Tab[r], Tab[i+1]
        return i+1


    def magic_fifths(T, l ,r):
        if r - l <= 1:
            return
        number = (r-l+1)//5
        i = 0
        while i < number:
            insertionSort(T, l + i*5, l + i*5 + 4)
            median = (2*l + i*5 + i*5+5)//2
            T[l + i], T[median] = T[median], T[l + i]
            i += 1
        if ((r-l)+1)%5 != 0:
            insertionSort(T, l + i * 5,l + i*5 + (r-l+1)%5 - 1)
            median = (2*l + i * 5 + i * 5 + (r-l+1)%5) // 2
            T[l+i], T[median] = T[median], T[l+i]
            i += 1


        magic_fifths(T, l, i-1)

    def select(T, p, r, k):
        if p == r:
            return T[p]

        q = partition(T, p, r)
        if q == k:
            return T[q]

        elif k < q:
            magic_fifths(T, p, q-1)
            T[p], T[q-1] = T[q-1], T[p]
            return select(T, p, q-1, k)

        else:
            magic_fifths(T, q+1, r)
            T[q+1], T[r] = T[r], T[q+1]
            return select(T, q+1, r, k)


    n = len(T)
    magic_fifths(T, 0, n-1)
    T[0], T[n-1] = T[n-1], T[0]


    return select(T, 0, n-1, k)







T = list(range(27))
shuffle(T)
t2 = T[::]
k = 14
print(T)
#print(t2)

#a = linearselect(T, k)
#print(T)
print(linearselect(T, k))
# print(linearselect2(t2, k))
#print(T)

