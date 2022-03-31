"""
Liczby wymierne są reprezentowane przez krotkę (l,m). Gdzie: l - liczba całkowita oznaczająca
licznik, m - liczba naturalna oznaczająca mianownik. Proszę napisać podstawowe operacje na ułamkach,
m.in. dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, skracanie, wypisywanie i wczytywanie.
"""
def skracanie(a):
    x = a[0]
    y = a[1]
    i = 2
    while i <= abs(max(x, y)):
        if x % i == 0 and y % i == 0:
            x //= i
            y //= i

        else:
            i += 1
    if y < 0 and x > 0:
        x = -x
        y = -y

    if y < 0 and x < 0:
        x = -x
        y = -y

    return (x, y)

def dodawanie(a, b):
    if a[1] == b[1]:
        return skracanie((a[0]+b[0], a[1]))

    else:
        return skracanie((a[0]*b[1] + b[0]*a[1], a[1]*b[1]))

def odejmowanie(a, b):
    if a[1] == b[1]:
        return skracanie((a[0] - b[0], a[1]))

    else:
        return skracanie((a[0] * b[1] - b[0] * a[1], a[1] * b[1]))

def mnozenie(a, b):
    return skracanie((a[0]*b[0], a[1]*b[1]))

def dzielenie(a, b):
    return skracanie((a[0]*b[1], a[1]*b[0]))

def potegowanie(a, b):
    return skracanie((a[0]**(b[0]/b[1]), a[1]**(b[0]/b[1])))

def wypisywanie(a):
    return a[0], '/', a[1]

def wczytywanie():
    x = int(input("> "))
    y = int(input("> "))
    return (x, y)


# a = wczytywanie()
# b = wczytywanie()
#
# print(dodawanie(a, b))
# print(odejmowanie(a, b))
# print(mnozenie(a, b))
# print(dzielenie(a, b))
# print(potegowanie(a, b))
# print(skracanie(a))
# print(skracanie(b))

"""
Używając funkcji z poprzedniego zadania proszę napisać funkcję rozwiązującą układ 2 równań
o 2 niewiadomych.
"""
a = ((-1, 1), (43, 5), (5, 1))
b = ((1, 34), (1, 1), (3, 1))
print(a[1])
print(b[2])

def rozwiaz_rownanie(a, b):
    x_1 = a[0]
    x_2 = b[0]
    y_1 = a[1]
    y_2 = b[1]
    res_1 = a[2]
    res_2 = b[2]

    W = odejmowanie(mnozenie(x_1, y_2), mnozenie(y_1, x_2))
    W_x = odejmowanie(mnozenie(res_1, y_2), mnozenie(y_1, res_2))
    W_y = odejmowanie(mnozenie(x_1, res_2), mnozenie(y_1, res_1))
    if W == 0:
        return "Sprzeczność"

    else:
        return "x =", dzielenie(W_x, W), "y =", dzielenie(W_y, W)

print(rozwiaz_rownanie(a, b))