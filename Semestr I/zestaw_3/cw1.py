"""
1. Napisać program zamieniający liczbę naturalną z systemu 10 na
podstawę 2-16
"""


n = int(input("> "))
s = 16

new = ""
while n != 0:
    k = n % s
    if k < 10:
        new += str(k)
    elif k == 10:
        new += "A"
    elif k == 11:
        new += "B"
    elif k == 12:
        new += "C"
    elif k == 13:
        new += "D"
    elif k == 14:
        new += "E"
    elif k == 15:
        new += "F"
    n = n // s

new = new[::-1]
print(new)