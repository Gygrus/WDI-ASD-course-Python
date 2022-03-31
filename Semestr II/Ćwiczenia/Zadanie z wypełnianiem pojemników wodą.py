Tab = [((1, 3), (4, 6)), ((2, 8), (5, 9)), ((0, 5), (3, 7))]

def check_if_filled(tank, height):
    if tank[0][1] <= height:
        if tank[1][1] <= height:
            return ((tank[1][0] - tank[0][0])*(tank[1][1] - tank[0][1]), 1)
        else:
            return ((tank[1][0] - tank[0][0])*(height-tank[0][1]), 0)

    return (0, 0)

def get_L_by_height(T, height):
    liters = counter = 0
    for x in T:
        result = check_if_filled(x, height)
        liters, counter = liters + result[0], counter + result[1]

    return (liters, counter)

def get_h_from_l(T, l, max):
    max_n = check = max
    current = 10^10
    mark = 2**(-20)
    while abs(current - l) >= mark and max_n <= check:
        partial = get_L_by_height(T, max_n)
        current = partial[0]
        max /= 2
        print(max_n)
        if current > l:
            max_n -= max
        if current < l:
            max_n += max

    return partial, max_n


print(get_h_from_l(Tab, 16, 9))
