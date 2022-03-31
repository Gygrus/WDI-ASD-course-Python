"""
Sprawdzić czy hetmany się szachują na szachownicy 100x100
"""


def check_if_killing_eachother(tab_of_cords):
    tab_of_first_cross = [-1]*len(tab_of_cords)
    tab_of_second_cross = [-1]*len(tab_of_cords)
    tab_of_line = [-1]*len(tab_of_cords)
    tab_of_col  = [-1]*len(tab_of_cords)
    i = 0
    for x in tab_of_cords:
        print(x)
        if x[0] in tab_of_line or x[1] in tab_of_col:
            return True

        first_check = x[0] + x[1]
        second_check = abs(x[0] - x[1])
        if first_check in tab_of_first_cross or second_check in tab_of_second_cross:
            return True

        tab_of_first_cross[i] = first_check
        tab_of_second_cross[i] = second_check
        tab_of_line[i] = x[0]
        tab_of_col[i] = x[1]
        i += 1

    return False

print(check_if_killing_eachother([[3, 3], [6, 11], [5, 7]]))