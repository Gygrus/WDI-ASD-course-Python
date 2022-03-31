x = int(input("> "))

a = 1
b = 1
sum = 0

while sum < x:
    sum += b
    c = a + b
    b = a
    a = c

a = 1
b = 1

while True:
    if sum - b < x:
        print(sum)
        break
    sum -= b
    c = a + b
    b = a
    a = c


