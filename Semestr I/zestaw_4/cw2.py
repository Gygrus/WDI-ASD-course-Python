"""
Dana jest tablica int t[MAX][MAX] wypełniona liczbami naturalnymi. Proszę napisać
funkcję który odpowiada na pytanie, czy w każdym wierszu tablicy występuje co
najmniej jedna liczba złożona wyłącznie z nieparzystych cyfr.
"""

def cw2(t):
    count = 0
    for x in t:
        for i in x:
            k = True
            for l in str(i):
                if int(l) % 2 == 0:
                    k = False
                    break
            if k:
                count += 1
                break
    if count == len(t):
        return True, count
    else:
        return False, count

print(cw2([[37, 65, 65, 97],
          [66, 39, 87, 90],
          [2, 54, 51, 60],
          [47, 89, 32, 2]]))
