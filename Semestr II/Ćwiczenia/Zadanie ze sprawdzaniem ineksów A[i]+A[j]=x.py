def quicksort(Tab, p, r):
    while p < r:
        q = partition(Tab, p, r)
        quicksort(Tab, p, q-1)
        p = q + 1

def partition(Tab, p, r):
    x = Tab[r]
    i = p-1
    for j in range(p, r):
        if Tab[j] < x:
            i += 1
            Tab[i], Tab[j] = Tab[j], Tab[i]
    Tab[i+1], Tab[r] = Tab[r], Tab[i+1]
    return i+1

def check_if_exists(T, x):
    i, j = 0, len(T)-1
    new = T[:]
    quicksort(new, 0, j)
    while i < j:
        if new[i] + new[j] > x:
            j -= 1
        elif new[i] + new[j] < x:
            i += 1
        else:
            return (True, new[i], new[j])
    return False


T = [3, 23, 7, 3, 2, 8, 1, 5, 4]
print(check_if_exists(T, 15))
print(T)