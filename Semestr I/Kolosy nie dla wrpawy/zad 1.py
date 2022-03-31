
n = int(input("> "))

silnia = 1
for x in range(2, n + 1):
    silnia *= x

    while silnia % 10 == 0:
        silnia //= 10

print(silnia%10)

#end