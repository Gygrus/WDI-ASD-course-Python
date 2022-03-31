"""
Dane s¡ dwie tablice int t1[N] oraz int t2[N] wypeªnione liczbami naturalnymi. Elementy z tablic t1 i t2
ª¡czymy w pary (po jednym elemencie z ka»dej tablicy) tak, aby suma wybranych elementów z tablicy t1 byªa
równa sumie wybranych elementów z tablicy t2. Prosz¦ napisa¢ funkcj¦, która zwróci maksymaln¡ liczb¦
par, jak¡ mo»na uzyska¢. Do funkcji nale»y przekaza¢ wyª¡cznie tablice t1 i t2, funkcja powinna zwróci¢
maksymaln¡ liczb¦ par.
"""


def licz_sume(tab):
    result = 0
    for x in tab:
        result += x
    return result

def licz_pary(t1, t2):
    if licz_sume(t1) == licz_sume(t2):
        return len(t1)

    #result = 0
    # def rekur(t1, t2, counter, i, suma, check = False, compare = tuple()):
    #     nonlocal result
    #     if not check:
    #         if i == len(t1):
    #             if counter > 0 and not check:
    #                 rekur(t2, t1, 0, 0, 0, True, (counter, suma))
    #             return
    #     if check:
    #         if suma > compare[1]:
    #             return
    #         if i == len(t1) and check:
    #             #print((i, counter, suma), t1[i-1], check, compare, 'gówno')
    #             if (counter, suma) == compare:
    #                 if counter > result:
    #                     print((i, counter, suma), t1[i-1], check, compare, 'gówno')
    #                     result = counter
    #             return
    #
    #     #print((i, counter, suma), t1[i], check, compare)
    #     rekur(t1, t2, counter, i+1, suma, check, compare)
    #     rekur(t1, t2, counter+1, i+1, suma+t1[i], check, compare)
    #
    # rekur(t1, t2, 0, 0, 0)

    def rekur(t1, counter, i, suma):
        print(t1, i, (counter, suma))
        if i == len(t1):
            if (counter, suma) in result:
                return
            if counter > 0:
                result.append((counter, suma))
            return

        rekur(t1, counter, i+1, suma)
        rekur(t1, counter+1, i+1, suma+t1[i])

    result = []
    rekur(t1, 0, 0, 0)
    result1 = result[:]
    result = []
    rekur(t2, 0, 0, 0)
    result2 = result[:]

    last_result = 0
    for x in result1:
        for y in result2:
            if x == y and x[0] > last_result:
                last_result = x[0]





    return last_result


t1 = [4, 2, 6, 3]
t2 = [2, 4, 7, 9, 6, 34, 6, 3, 6, 68, 3, 3, 42, 5, 7,6 ,8]

print(licz_pary(t1, t2))