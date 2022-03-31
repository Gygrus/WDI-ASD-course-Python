# Piotr Socała
# Wyznaczam najpierw wartości liczb dla
# poszczególnych wierszy, zapisuję je w tablicy
# a potem iteruję po znalezionych liczbach i
# znajduję największą różnicę między dwoma


def distance(T):

    def change_to_normal(x):
        l = len(x)
        new_number = 0
        for k in x:
            if k == 1:
                new_number += 2**l
                l -= 1
            else:
                l -= 1
        return new_number
    #end def

    tab = [0]*len(T)
    i = 0
    for x in T:
        tab[i] = change_to_normal(x)
        i += 1

    biggest = 0
    for x in range(len(tab)):
        for y in range(x + 1, len(tab)):
            if abs(tab[x] - tab[y]) > biggest:
                biggest = abs(tab[x] - tab[y])
                result = y - x

    return result

#end def



