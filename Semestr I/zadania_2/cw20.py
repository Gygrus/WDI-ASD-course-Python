
k = 123
l = 522

for x in range(2, 17):
    check = True
    check_01 = True
    z = k
    new = ''
    while z != 0:
        if str(z % x) in new:
            check = False

        new += str(z % x)
        z = z//x
    new = new[::-1]

    z = l
    new_01 = ''
    while z != 0:
        if str(z % x) in new:
            check_01 = False
        new_01 += str(z % x)
        z = z//x
    new_01 = new_01[::-1]
    if check and check_01:
        print(new, new_01, "system", x)
        break

