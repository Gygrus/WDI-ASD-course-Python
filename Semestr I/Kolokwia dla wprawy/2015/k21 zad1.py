"""
 Dane są trzy operacje na liczbach naturalnych oznaczone literami ĄB,C.
A. jeżeli liczba posiada co najmniej 2 cyfry zamienia miejscami dwie ostatnie cyfry w liczbie;
B. mnoży liczbę przez3;
c. jeżeli liczba posiada co najmniej 2 cyfry usuwa pierwszą cyfrę z liczby.
Proszę napisać funkcję, która szuka sekwencji operacji przekształcającej liczbę naturalną x na y (x!=y) o długości nie większej niż 7. Do funkcji
należy przekazać liczby x, y. Funkcja powinna zwrócić napis złożony z liter ABC realizujący przekształcenie albo łańcuch pustyjeżeli
przekształcenie nie istnieje. Na przykład dla liczb 6,3 funkcja powinna zwrócić napis "BACB".
"""

def czy_istnieje(x, y):

    def d_A(k):
        ost = k % 10
        pdost = (k % 100 - k % 10) // 10
        k = k // 100
        k = (k*10 + ost)*10 + pdost
        return k

    def d_B(k):
        return k * 3

    def d_C(k):
        p = len(str(k))
        return k % 10**(p-1)

    result = ''
    count_of_steps = 0
    while x != y and count_of_steps <= 7:
        if len(str(x)) > 1:
            count = 1
            tab = [(x % 100 - x % 10)//10, x % 10]
            for t in tab:
                if y % t == 0:
                    pom = y / t
                    k = True
                    while pom != 1:
                        pom /= 3
                        if pom < 1:
                            k = False
                            break

                    if k:
                        if count == 1:
                            x = d_A(x)
                            count_of_steps += 1
                            result += 'A'
                            print(x)
                            while len(str(x)) != 1:
                                x = d_C(x)
                                count_of_steps += 1
                                result += 'C'
                                print(x)

                            while x != y:
                                x = d_B(x)
                                count_of_steps += 1
                                result += 'B'
                                print(x)

                            return result, count_of_steps

                        else:
                            while len(str(x)) != 1:
                                x = d_C(x)
                                count_of_steps += 1
                                result += 'C'
                                print(x)

                            while x != y:
                                x = d_B(x)
                                count_of_steps += 1
                                result += 'B'
                                print(x)

                            return result, count_of_steps

                    count += 1

        x = d_B(x)
        result += "B"
        count_of_steps += 1





print(czy_istnieje(6, 78))