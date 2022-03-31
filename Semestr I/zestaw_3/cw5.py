"""
Obliczanie stałej e z rozwinięcia w szereg
e=1/0!+1/1!+1/2!+1/3!+... z dokładnością do np. 1000 cyfr dziesiętnych.

"""

ep = 1e-10
result = 0
k = 0
licz = 634
def fact(x):
    result = 1
    if x == 0:
        return 1
    else:
        for i in range(1, x + 1):
            result *= i
        return result

def div(x, count):
    p = count
    z = 1
    result = ''
    if x == 1:
        return x
    else:
        # result = str(1 // x) + '.'
        while count > 0:
            z = (z % x) * 10
            result += str(z//x)
            z = z - x * (z//x)
            count -= 1



        return result

previous = 10
while abs(result - previous) > ep:
    previous = result
    result += int(div(fact(k), 1000))
    k += 1

print(("2." + str(result))[:licz + 2])