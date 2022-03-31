x = int(input("> "))

k = x
j = 0
while x > 0:
    j = j*10 + x % 10
    x = (x - x%10) // 10
    print(j)
if j == k:
    print("True")
else:
    print("False")

new = '1'
l = k
n = 0
suma = 1
while suma <= l:
    z = n
    suma = 2**n
    n += 1
suma = suma // 2
while suma != l:
    if suma + 2**(z-2) <= l:
        suma += 2**(z-2)
        new += "1"
    else:
        new += "0"
    z -= 1

if new == new[::-1]:
    print("True for bin", new)
else:
    print("Not True for bin")
print(new)

