from random import randint
def merge_invert(T):
    n = len(T)
    sub_array = [0]*n
    return get_inversions(T, 0, n-1, sub_array)


def get_inversions(T, left, right, sub_array):
    inv_count = 0


    if left < right:
        mid = (right+left)//2

        inv_count += get_inversions(T, left, mid, sub_array)

        inv_count += get_inversions(T, mid+1, right, sub_array)

        inv_count += merge(T, left, mid, right, sub_array)

    return inv_count

def merge(T, left, mid, right, sub_array):
    i = left
    j = mid+1
    k = left
    inv_count = 0
    while i <= mid and j <= right:
        if T[i] <= T[j]:
            sub_array[k] = T[i]
            i += 1
            k += 1
        else:
            sub_array[k] = T[j]
            inv_count += (mid-i)+1
            j += 1
            k += 1

    while i <= mid:
        sub_array[k] = T[i]
        i += 1
        k += 1

    while j <= right:
        sub_array[k] = T[j]
        j += 1
        k += 1

    for x in range(left, right+1):
        T[x] = sub_array[x]

    return inv_count


def brute_check(T):
    counter = 0
    for x in range(len(T)):
        for y in range(x+1, len(T)):
            if T[y] < T[x]:
                counter += 1
    return counter

T = [randint(-100, 100) for _ in range(25)]
print(T)
# print(brute_check(T))
print(merge_invert(T))
print(T)
