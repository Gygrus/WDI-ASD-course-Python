"""
Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. Proszę napisać
funkcję, która zwraca długość najdłuższego spójnego podciągu będącego palindromem złożonym wyłącznie
z liczb nieparzystych. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość znalezionego
podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.
"""

def cw18(t):
    temp = []
    tab = []
    max = []
    max_amount = 0
    k = len(t)
    while k > 1:
        i = 0
        while i != k:
            print("i", i)
            print("k", k)
            temp = t[i:k]
            z = True
            for x in temp:
                if x % 2 == 0:
                    z = False
                    break
            if temp[::-1] == temp and len(temp) > max_amount and z:
                max_amount = len(temp)
                max = temp
            i += 1
        k -= 1
    if len(max) > 1:
        return max_amount, max

    else:
        return None

print(cw18([6, 9, 9, 3, 9, 9, 6, 8, 9, 9, 4, 15, 9, 7, 5, 4, 5, 5, 7, 9, 15]))