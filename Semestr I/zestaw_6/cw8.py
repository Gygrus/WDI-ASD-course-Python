"""
Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach.
"""

def czy_mozliwe(T, masa, i):
    if masa == 0:
        return True
    if i == len(T):
        return False

    else:
        return czy_mozliwe(T, masa - T[i], i +1) or czy_mozliwe(T, masa + T[i], i+1) or czy_mozliwe(T, masa, i+1)

def rek(T, masa):
    i = 0
    return czy_mozliwe(T, masa, i)

print(rek([1, 3, 5, 10, 16, 24], 43))