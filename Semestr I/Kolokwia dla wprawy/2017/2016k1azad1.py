"""
Dane są dwa ciągi określone następująco:
a1 = 1 an = an−1 + bn/3
b1 = 2 bn = bn−1 + an−1
Proszę napisać program, który wczytuje liczbę naturalną k i odnajduje wyraz należący do
jednego z ciągów o wartości najbliższej k. Program powinien wypisać numer znalezionego
wyrazu i ciąg z którego on pochodzi. Jeżeli więcej niż jeden wyraz jest jednakowo odległy
od k, należy wybrać ten o mniejszym numerze.
"""

k = int(input("> "))

maximum = 10**100
count = 1
a = 1
a_copy = a
b = 2
b_copy = b
check_a = abs(a - k) + 1
check_b = abs(b-k) + 1
while abs(a-k) < check_a or abs(b-k) < check_b:
    if abs(a - k) < maximum:
        maximum = abs(a-k)
        result = "ciąg a", str(count), str(a)
        check_a = abs(a-k)

    if abs(b-k) < maximum:
        maximum = abs(b-k)
        result = "ciąg b", str(count), str(b)
        check_b = abs(b-k)

    a += b_copy / 34
    b += a_copy
    count += 1
    a_copy = a
    b_copy = b
    print(a, b, count)

print(result)