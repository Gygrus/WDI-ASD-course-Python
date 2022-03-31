def longest_palindrome(tab, tab_length):
    # nieparzyste
    max_length = 0
    for i in range(tab_length):
        j = 0
        while 0 < i-j and i + j < tab_length and tab[i+j] == tab [i-j] and tab[i+j] % 2 == 1:
            j += 1

        if 2*j - 1 > max_length:
            max_length = 2*j - 1

    # parzyste
    for i in range(tab_length - 1):
        j = 0
        while 0 < i-j and i+j+1 < tab_length and tab[i+j+1] == tab[i-j] and tab[i+j+1] % 2 == 1:
            j += 1

        if 2*j > max_length:
            max_length = 2 * j

    return max_length



t1 = [26, 56, 86, 6, 86, 6, 26]

print(longest_palindrome(t1, len(t1)))