"""
Napisać program obliczający i wypisujący wartość N! dla N z
zakresu od 1 do 1000.

"""

n = int(input("> "))
result = 1
for x in range(1, n + 1):
    result *= x
    print(x)
print(result)