"""
Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
zadanych liczb.
"""

def czy_pierwsza(n):
    if n < 2:
        return False
    else:
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

def get_length(n):
    if n == 0:
        return 0
    return 1 + get_length(n//10)




def rec(s1, s2):
    count = 0
    def create_word(s1, s2, i_1, i_2, new):
        if i_1 + i_2 == get_length(s1) + get_length(s2) + 2:
            if czy_pierwsza(new):
                print(new)
                nonlocal count
                count += 1

        else:
            if i_1 <= get_length(s1) and i_2 <= get_length(s2):
                return create_word(s1, s2, i_1 + 1, i_2, new*10 + (s1//(10**((get_length(s1)) - i_1)) % 10)) or create_word(s1, s2, i_1, i_2+1, new*10 + (s2//(10**((get_length(s2)) - i_2)) % 10))
            elif i_1 <= get_length(s1):
                return create_word(s1, s2, i_1 + 1, i_2, new * 10 + (s1//(10**((get_length(s1)) - i_1)) % 10))
            else:
                return create_word(s1, s2, i_1, i_2+1, new*10 + (s2//(10**((get_length(s2)) - i_2)) % 10))

    create_word(s1, s2, 1, 1, 0)
    return count

#


print(rec(123, 758))


