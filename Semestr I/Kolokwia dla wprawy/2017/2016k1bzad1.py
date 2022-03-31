"""
Dane są ciągi an, bn i cn określone następująco:
an = 1 dla n = 1, 2 bn = 1 dla n = 1, 2, 3
an = an−1 + an−2 dla n > 2 bn = bn−1 + bn−2 + bn−3 dla n > 3
Wyrazy ciągu cn są kolejnymi liczbami naturalnymi należącymi do ciągu an lub bn.
Ciągi te przyjmują wartości:
an : 1 1 2 3 5 8 13 21 ...
bn : 1 1 1 3 5 9 17 31 ...
cn : 1 2 3 5 8 9 13 17 ...
Proszę napisać program który wczytuje wprowadzoną z klawiatury liczbę naturalną k
i wypisuje k-ty wyraz ciągu cn.
"""


k = int(input("> "))

a_1 = 1
a_2 = 1
b_1 = 1
b_2 = 1
b_3 = 1
count = 1
cn = 1
while count != k:

    while a_1 <= cn:
        a_pom = a_1 + a_2
        a_2 = a_1
        a_1 = a_pom

    while b_1 <= cn:
        b_pom_1 = b_1 + b_2 + b_3
        b_pom_2 = b_2
        b_2 = b_1
        b_3 = b_pom_2
        b_1 = b_pom_1

    if a_1 < b_1:
        cn = a_1
        count += 1
    else:
        cn = b_1
        count += 1
