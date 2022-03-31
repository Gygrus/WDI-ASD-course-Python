"""
Problem wież w Hanoi (treść oczywista)
"""

def hanoi(n, tab1, tab2, tab3, count):
    if n > 0:
        print(tab1, tab2, tab3)
        hanoi(n-1, tab1, tab3, tab2, count+1)
        tab3.insert(0, tab1.pop(0))
        count += 1
        hanoi(n-1, tab2, tab1, tab3, count+1)

def gowno(n):
    tab1 = list(range(1, n+1))
    print(tab1)
    tab2 = [0]*n
    tab3 = [0]*n
    hanoi(n, tab1, tab2, tab3, 0)


print(gowno(3))