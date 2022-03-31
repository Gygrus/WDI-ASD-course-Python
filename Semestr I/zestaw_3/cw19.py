"""
Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów jest
równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość
znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje
"""

def cw19(t):
    k = len(t)
    i = 0
    biggest = 0
    result = []
    while k > 0:
        i = 0
        while i != k:
            new = t[i:k]
            temp_length = len(new)
            index_sum = sum(list(range(i, k)))
            if sum(new) == index_sum:
                tab = [0]
                z = True
                for x in new:
                    if x < tab[-1]:
                        z = False
                        break
                    tab.append(x)
                if z and temp_length > biggest:
                    biggest = temp_length
                    result.append(new)


            i += 1
        k -= 1
    return biggest, result

print(cw19([7, 6, 5, 2, 3, 2, 1, 4]))

