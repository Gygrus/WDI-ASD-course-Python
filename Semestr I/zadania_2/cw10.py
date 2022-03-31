def f(x):
    return 1/x


k = 5
a = 0.0001
pr = 5674
odst = (k-a) / pr
sr = a + (k-a)/(2*pr)
n = 0
wynik = 0

while n < k:
    print(odst*f(sr + n*odst))
    wynik += odst*f(sr + n*odst)
    n += 1

print(wynik)

