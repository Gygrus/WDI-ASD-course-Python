"""
Dana jest tablica int t[MAX][MAX] wypełniona liczbami naturalnymi. Proszę napisać
funkcję który odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda
z liczb zawiera przynajmniej jedna cyfrę parzystą.
"""

def cw3(t):
    for x in t:
        count = 0
        for i in x:
            for l in str(i):
                if not(int(l) % 2):
                    count += 1
                    break
            if count == len(x):
                return "Istnieje taki wiersz, a dokładnie wiersz", x
    return "Nie istnieje taki wiersz"


print(cw3([[3, 65, 68, 47],
           [66, 49, 97, 90],
           [2, 54, 187, 60],
           [47, 89, 32, 3]]))