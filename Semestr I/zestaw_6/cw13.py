"""
Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej
na sumę składników. Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.
"""

def rekur(n):
    copy = n
    counter = 0
    def find_parts(number, i, set_of_el, global_set_of_el, result):
        if number == result:
            if set_of_el not in global_set_of_el:
                nonlocal counter
                #set_of_el = map(str, list(set_of_el))
                #print('+'.join(set_of_el))
                #set_of_el = tuple(set_of_el)
                counter += 1
                global_set_of_el.append((set_of_el))
        elif number < result and i < result:
            find_parts(number, i+1, set_of_el, global_set_of_el, result)
            set_of_el = set_of_el[:]
            set_of_el.append(i)
            find_parts(number+i, i, set_of_el, global_set_of_el, result)
        else:
            pass




    find_parts(0, 1, list(), list(), copy)
    return counter

print(rekur(50))