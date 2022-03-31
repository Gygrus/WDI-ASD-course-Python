def cw8(x):
    k = 0
    for i in range(2, x):
        if x % i == 0:
            k = 1
    if k == 1:
        print("To nie jest liczba pierwsza")
    else:
        print("To jest liczba pierwsza")



cw8(11)
