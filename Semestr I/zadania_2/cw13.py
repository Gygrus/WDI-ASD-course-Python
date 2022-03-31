x = int(input("> "))

pierwsze = True
z = True
while x > 0:
    if pierwsze:
        j = x % 10
        pierwsze = False
    else:
        k = x % 10
        if k == j:
            print("gówno")
            z = False
            break
    x = x // 10
if z:
    print("jest unikalna")


# k = 0
# for i in str(x)[:-1]:
#     if i == str(x)[-1]:
#         print(False)
#         break
# print(k)
# print(not (k-1))

