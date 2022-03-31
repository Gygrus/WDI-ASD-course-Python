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
