"""
Rekurencyjne obliczanie wyznacznika z macierzy (treść oczywista)
"""


def rekur(T):
    count = 0
    det = 0
    def get_det(T, k, i):
        nonlocal count
        nonlocal det
        if i == 3:
            count += 1
            print(T, k)
            #nonlocal det
            det += k * (T[0][0]*T[1][1]*T[2][2] + T[0][1]*T[1][2]*T[2][0] + T[1][0]*T[2][1]*T[0][2] - T[0][2]*T[1][1]*T[2][0] - T[0][1]*T[1][0]*T[2][2] - T[0][0]*T[1][2]*T[2][1])
        elif i == 2:
            #nonlocal det
            det += T[0][0]*T[1][1] - T[0][1]*T[1][0]
        else:
            new_matrix = [[0 for _ in range(i-1)] for _ in range(i-1)]
            T = list(T)
            # print(new_matrix)
            # print(type(new_matrix))
            # print(type(T))
            for k in range(len(T)):
                for x in range(len(T)-1):
                    p = 0
                    for y in range(len(T)):
                        if y != k:
                            new_matrix[x][p] = T[x+1][y]
                            p += 1
                #print(new_matrix)
                new_matrix = tuple(new_matrix)
                get_det(new_matrix, ((-1)**k)*T[0][k], i-1)

    get_det(T, 1, len(T))
    return det, count


T = ((6, 2, 3, 9, 5, 4,), (1, 8, 5, 2, 1, 8,), (1, 0, 9, 5, 9, 3,), (9, 5, 0, 7, 3, 1), (4, 5, 7, 2, 5, 5,), (1, 5, 5, 3, 0, 1))

print(rekur(T))

