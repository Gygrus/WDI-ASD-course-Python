def cw3(searched_number):
    a1 : int = 1
    a2 : int = 1
    suma : int = 0
    b1 = 1
    b2 = 1
    while True:
        suma += a1
        print("Suma na początku równa się = ", suma)
        if searched_number - suma == 0:
            return True
        if searched_number < suma:
            while True:
                print("Suma w wewnętrznej pętli równa się = ", suma)
                if suma - b1 == searched_number:
                    return True
                if suma - b1 < searched_number:
                    return False
                suma -= b1
                new_number_b = b1 + b2
                b1 = b2
                b2 = new_number_b
        new_number = a1 + a2
        a1 = a2
        a2 = new_number

cw3(13)