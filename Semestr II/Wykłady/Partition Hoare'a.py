def partition(T, p, r):
    pivot = T[p]
    i = p - 1
    j = r + 1

    while True:
        i += 1
        while T[i] < pivot:
            i += 1

        j -= 1
        while T[j] > pivot:
            j -= 1

        if i >= j:
            return j

        T[i], T[j] = T[j], T[i]