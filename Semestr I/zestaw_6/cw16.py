"""
Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą liczbę samogłosek oraz sumy kodów ascii liter z których są zbudowane są identyczne, na przykład 00ula00 → 117, 108, 97
oraz 00exe00 → 101, 120, 101. Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. Dodatkowo funkcja powinna wypisać
znaleziony wyraz.
"""


def get_weight(n):
    sam_count = 0
    weight = 0
    for x in n:
        if x in "aeiouy":
            sam_count += 1
        weight += ord(x)

    return (sam_count, weight)





def wyraz(s1, s2, i, s2_or):
    print(s2)
    if i == len(s2_or):
        if get_weight(s1) == get_weight(s2):
            return True, s2
        else:
            return False
    else:
        return wyraz(s1, s2, i + 1, s2_or) or wyraz(s1, s2 + s2_or[i], i+1, s2_or)


print(wyraz('ularfeu', '', 0, 'exetyeoruiytuifh'))
