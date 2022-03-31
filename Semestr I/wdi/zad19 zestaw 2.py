"""
Napisać program wczytujący dwie liczby naturalne a,b i wypisujący rozwinięcie dziesiętne
ułamka a/b w postaci ułamka okresowego. Na przykład 1/3 = 0.(3), 1/6 = 0.1(6), 1/7 = 0.(142857)
"""

def f(a, b):
    def ile2_5(n):
        counter2 = 0
        while n % 2 == 0:
            counter2 += 1
            n //= 2

        counter5 = 0
        while n % 5 == 0:
            counter5 += 1
            n //= 5

        return max(counter2, counter5)
    #end

    result = ''

    #print(a//b, end='')
    result += str(a//b)

    r = a % b
    if r > 0:
        #print('.', end='')
        result += '.'
        for i in range(ile2_5(b)):
            r *= 10
            #print(r//b, end='')
            result += str(r//b)
            r %= b

        if r > 0:
            #print('(', end='')
            result += '('
            temp = r
            while True:
                r *= 10
                #print(r//b, end='')
                result += str(r // b)
                r %= b
                if r == temp:
                    break

            #print(')', end='')
            result += ')'

    #print()
    return result
#end


print(len(f(356633799846, 89654863368354)))