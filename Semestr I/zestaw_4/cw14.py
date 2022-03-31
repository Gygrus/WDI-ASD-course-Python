"""
Dwie liczby naturalne są zgodne jeżeli w zapisie dwójkowym zawierają tę samą liczbę jedynek,
np. 22 = 101102 i 14 = 11102. Dane są tablice T1[N1][N1] T2[N2][N2], gdzie N2¿N1. Proszę napisać funkcję,
która sprawdza czy istnieje takie położenie tablicy T1 wewnątrz tablicy T2, przy którym liczba zgodnych
elementów jest większa od 33%. Do funkcji należy przekazać tablicę T1 i T2. Obie oryginalne tablice powinny
pozostać nie zmieniane.
"""

def cw14(t1, t2):
    p_g = len(t1) - 1
    l_d = len(t1) - 1
    x_1 = 0
    y_1 = 0
    while p_g < len(t2):

        while l_d < len(t2):

            x_t2 = x_1
            y_t2 = y_1
            count = 0
            print("ZACZYNAMY NOWE SZUKANIE", y_t2, x_t2)

            for x in range(len(t1)):
                for i in range(len(t1)):
                    print(x, i)

                    new_t1 = ''
                    new_t2 = ''
                    copy_t1 = t1[x][i]
                    copy_t2 = t2[y_t2][x_t2]
                    while copy_t1 != 0 and copy_t2 != 0:
                        new_t1 += str(copy_t1 % 2)
                        copy_t1 = copy_t1 // 2
                        new_t2 += str(copy_t2 % 2)
                        copy_t2 = copy_t2 // 2

                    if new_t2.count("1") == new_t1.count("1"):
                        print(new_t2, new_t1)
                        count += 1
                    print("count", count)

                    x_t2 += 1
                y_t2 += 1
                x_t2 = x_1

            if count >= (len(t1) ** 2) * 0.33:
                return True, y_1, x_1
            l_d += 1
            x_1 += 1


        p_g += 1
        y_1 += 1

    return False





print(cw14([[1, 1, 1, 3, 3, 61],
           [7, 1, 6, 3, 3, 53452],
           [3, 3, 11, 3, 33, 1],
           [1, 3, 1, 12, 1, 1],
           [1, 3, 3, 3, 7, 1],
           [32, 1, 1, 41, 2341, 63467]],

           [[152, 33242, 45, 542, 66424, 675, 46],
            [124, 421, 3452, 523, 2342, 53453452, 52],
            [23324, 443, 45321, 13224, 333, 552, 5231],
            [142, 123, 234, 1345, 55313, 23451, 73],
            [234, 5325, 23425, 412, 5524, 1341, 123],
            [332, 512, 122, 421, 2341, 63467, 92],
            [22353, 45, 5521, 2324, 35351, 552412, 52, 51]]
           ))