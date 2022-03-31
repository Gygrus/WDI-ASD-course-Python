"""
Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A cyfr
1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca ilość
wszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym (najstarszy
bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
10010(2), 10100(2), 11000(2)
"""

def check_if_not_prime(n):
    length = 0
    copy = n
    while copy != 0:
        copy //= 10
        length += 1

    copy = n
    new_number = 0
    i = 0
    #print('wejscie', copy, length)
    for x in range(length):
        t = copy % 10
        new_number += t*(2**i)
        i += 1
        copy //= 10

    i = 2
    #print('nowa liczba', new_number)
    while i*i <= new_number:
        #print("i", i)
        if new_number % i == 0:
            return True
        i += 1

    return False


def rekur(A, B):
    if A <= 0:
        return False

    sum_of_all = A+B
    counter = 0
    def find_all_binary(A, B, number, i):
        #print(number)
        if i == 0:
            if check_if_not_prime(number):
                print(number)
                nonlocal counter
                counter += 1

        else:
            number *= 10
            if A > 0:
                find_all_binary(A-1, B, number+1, i-1)
            if B > 0:
                find_all_binary(A, B-1, number, i-1)



    find_all_binary(A-1, B, 1, sum_of_all-1)

    return counter

print(rekur(5, 5))
