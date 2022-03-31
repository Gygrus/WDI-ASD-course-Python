"""
Napisać program, który wczytuje liczbę naturalną N. Interesujące są
dla nas reprezentacje liczby w systemach o podstawach od 2 do 8
włącznie. Program powinien odpowiadać na pytanie: czy w
którejkolwiek z tych reprezentacji długość maksymalnego podciągu
niemalejącego utworzonego z kolejnych cyfr liczby jest
równa dokładnie 4.
"""

def funkcja():
    N = int(input("Wpisz liczbę naturalną: "))

    for x in range(2, 9):
        n_copy = N
        new_n = 0
        while n_copy != 0:
            new_n *= 10
            new_n += n_copy%x
            n_copy //= x

        count = 1
        biggest = 0
        l = len(str(new_n))
        for i in range(l - 1):
            if (new_n // 10**i) % 10 <= (new_n // 10**(i+1)) % 10:
                count += 1
                if count > biggest:
                    biggest = count

            else:
                count = 1

        if biggest == 4:
            return "Tak", x, new_n

    return "Nie"


print(funkcja())