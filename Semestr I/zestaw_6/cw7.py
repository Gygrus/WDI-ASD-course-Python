"""
Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy.
Odważniki można umieszczać tylko na jednej szalce.
"""

def czy_mozliwe(T, masa, i):
    if i == len(T):
        print(masa)
        if masa == 0:
            return True
        return False

    else:
        return czy_mozliwe(T, masa - T[i], i +1) or czy_mozliwe(T, masa, i+1)

def rek(T, masa):
    i = 0
    return czy_mozliwe(T, masa, i)

print(rek([1, 3, 5, 10, 16, 24], 43))