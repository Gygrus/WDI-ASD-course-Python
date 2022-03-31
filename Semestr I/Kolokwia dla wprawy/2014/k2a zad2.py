"""
 Wyrazy budowane są z liter a..z. Dwa wyrazy „ważą” tyle samo jeżeli: mają tę samą liczbę
samogłosek oraz sumy kodów ascii liter z których są zbudowane są identyczne, na przykład „ula” ->
117 108 97 oraz „exe” 101 120 101. Proszę napisać funkcję bool wyraz( string s1, string s2), która
sprawdza czy jest możliwe zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co
wyraz s1. Dodatkowo funkcja powinna wypisać znaleziony wyraz.
"""


def same_weight(s1, s2):
    samogl = ['a', 'e', 'i', 'o', 'u', 'y']
    count_samogl = 0
    weight_s1 = 0
    for p in s1:
        if p in samogl:
            count_samogl += 1

        weight_s1 += ord(p)

    n = len(s2)
    p = 2**n
    for x in range(p):
        binar = ''
        while x != 0:
            binar += str(x % 2)
            x //= 2

        binar = str(binar)
        while len(binar) != len(s2):
            binar += '0'
        # print(binar)
        count_samogl_s2 = 0
        weight_s2 = 0
        new_word = ''
        licznik = 0
        for k in s2:
            if int(binar) % 10 == 1:
                if k in samogl:
                    count_samogl_s2 += 1
                new_word += k

                weight_s2 += ord(k)

            binar = str(int(binar) // 10)

        if count_samogl_s2 == count_samogl and weight_s2 == weight_s1:
            return True, new_word, count_samogl_s2, weight_s2, weight_s1, count_samogl


print(same_weight('ulareeyd', 'ebe'))