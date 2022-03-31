def weight(n):
    counter = 0
    podzielnik = 2
    while n > 1 and podzielnik < n**0.5:
        is_primary = False
        while n % podzielnik == 0:
            is_primary = True
            n //= podzielnik
        if is_primary:
            counter += 1
        podzielnik += 1
    if n > 1:
        counter += 1
    return counter

def zbiory(t):

    def zbiory2(t, set1, set2, set3):
        if licznik == len(t):
            return set1 == set2 == set3
        return zbiory2(t, set1 + t[licznik], set2, set3, licznik + 1) or zbiory2(t, set1 + t[licznik], set2, set3, licznik + 1) or zbiory2(t, set1 + t[licznik], set2, set3, licznik + 1):

    weight_sum = 0
    weight_array = [0]*len(t)
    for i in range(len(t)):
        weight_array[1] = weight(t[i])
        weight_sum += weight_array[i]

    if weight_sum % 3 != 0:
        return False
    return
