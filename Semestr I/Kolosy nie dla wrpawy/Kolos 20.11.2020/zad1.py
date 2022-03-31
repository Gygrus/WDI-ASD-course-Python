# Piotr Socała
# Począwszy od 2, sprawdzam czy podciągi długości k są napisami
# wielokrotnymi i zapisuje ich długość do count, porównuje z biggest
#
#
#


def multi(T):
    biggest = 0
    k = 1
    while k <= len(T):
        i = 0
        count = 0
        while i < len(T) - 2:
            for x in range(i, len(T) // 2):
                if T[x:k+x] == T[k+x:x+2*k]:
                    count += 1

                if count > biggest:
                    biggest = count
            i += 1
        k += 1

    return biggest


#end def

