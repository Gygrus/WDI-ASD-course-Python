#Piotr Socała

#Obliczę sumy dla wszystkich kolumn i wierszy i sprawdze takie ułożenie dwóch
# punktów, dla których sumy te są najmniejsze



def chess(T):
    sum_of_col = [0]*len(T)
    sum_of_row = [0] * len(T)

    for x in range(len(T)):
        for y in range(len(T)):
            sum_of_col[y] += T[x][y]
            sum_of_row[x] += T[x][y]
    biggest = -9*(10**10)
    result = []
    for x in range(len(T)):
        for y in range(len(T)):
            for x1 in range(len(T)):
                for y1 in range(len(T)):
                    if x == x1 and y == y1:
                        sum = biggest
                        pass
                    elif x == x1:
                        sum = sum_of_row[x] + sum_of_col[y] + sum_of_col[y1] - 2*T[x][y] - 2*T[x1][y1]

                    elif y == y1:
                        sum = sum_of_row[x] + sum_of_row[x1] + sum_of_col[y] - 2 * T[x][y] - 2 * T[x1][y1]

                    else:
                        sum = sum_of_row[x] + sum_of_row[x1] + sum_of_col[y] + sum_of_col[y1] - 2*T[x][y] - 2*T[x1][y1] - T[x1][y] - T[x][y1]

                    if sum > biggest:
                        result = [x, y, x1, y1]
                        biggest = sum

    return tuple(result)



