def cw12(a, b, c):
    for x in range(1, a + 1):
        if x <= a and x <= b and x <= c:
            if a % x == 0 and b % x == 0 and c % x == 0:
                result = x
        else:
            return result


print(cw12(85, 17, 1513))
def cw13(a, b, c):
    for x in range(1, a + 1):
        if x <= a and x <= b:
            if a % x == 0 and b % x == 0:
                result = x
    result = a*b/result
    print("NWD1 = ", result)
    for i in range(1, int(result) + 1):
        if i <= c and i <= result:
            if c % i == 0 and result % i == 0:
                result_2 = i
    print("NWD2 = ", result_2)
    nww = c*result/result_2
    print(nww)

cw12(23, 14, 54)

cw13(25, 34, 26)