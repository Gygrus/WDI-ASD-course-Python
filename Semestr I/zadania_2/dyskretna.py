def generuj_pozdziory(n, p):
    if p == n:
        for i in range(n):
            if ciag[i] == 1:
                print(i, end = '')
        print()
    else:
        ciag[p] = 0
        generuj_pozdziory(n, p + 1)
        ciag[p] = 1
        generuj_pozdziory(n, p + 1)


ciag = [0, 1, 2, 7]
generuj_pozdziory(4, 0)