from random import randint
n = int(input("> "))

t = [randint(1, 1000) for x in range(n)]

"""
Napisać program wypełniający N-elementową tablicę t
liczbami naturalnymi 1-1000 i sprawdzający czy każdy
element tablicy zawiera co najmniej jedną cyfrę nieparzystą.
"""

for x in t:
    k = False
    for i in str(x):
        if int(i) % 2 != 0:
            k = True
    if not k:
        print("Nie ma nieparzystej!", x)
        break

"""
Napisać program wypełniający N-elementową tablicę t liczbami naturalnymi 1-1000 i 
sprawdzający czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste
"""

for x in t:
    p = True
    for i in str(x):
        if int(i) % 2 == 0:
            p = False
            break
    if p:
        print("Jest wyłącznie z nieparzystymi cyframi!", x)
        break