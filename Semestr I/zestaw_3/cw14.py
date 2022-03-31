""""
Napisać program wyznaczający na drodze eksperymentu prawdopodobieństwo tego, że w
grupie N przypadkowo spotkanych osób, co najmniej dwie urodziły się tego samego dnia roku. Wyznaczyć
wartości prawdopodobieństwa dla N z zakresu 20-40.
"""

from random import randint

n = int(input("> "))
z = randint(500, 10000)
count = 0
for x in range(z):
    check = []
    for i in range(n):
        k = randint(1, 365)
        if k in check:
            count += 1
            break
        check.append(k)
print(count)
print(z)
print(count / z)