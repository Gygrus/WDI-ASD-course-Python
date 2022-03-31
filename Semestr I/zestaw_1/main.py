
x_0 = 0
x_1 = 0
x_2 = 5
e = 0.00000001

while True:
    if (x_0**x_0 - 2020) * (x_2**x_2 - 2020) < 0:
        x_1 = (x_0 + x_2)/2
        if abs(0 - (x_1**x_1 - 2020)) < e:
            print(x_1, "to odpowiedź")
            break
        else:
            if (x_0**x_0 - 2020) * (x_1**x_1 - 2020) < 0:
                x_2 = x_1
            else:
                x_0 = x_1
