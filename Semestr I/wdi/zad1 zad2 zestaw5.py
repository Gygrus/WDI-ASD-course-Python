"""
Dany jest zbiór punktów leżących na płaszczyźnie opisany przy pomocy struktury dane =
[(x1, y1),(x2, y2),(x3, y3), ...(xN , yN )] Proszę napisać funkcję, która zwraca wartość True jeżeli zbiorze istnieją 4 punkty wyznaczające kwadrat o bokach równoległych do osi układu współrzędnych, a wewnątrz
tego kwadratu nie ma żadnych innych punktów. Do funkcji należy przekazać strukturę opisującą położenie
punktów.
"""

def suma(u1, u2): return skroc((u1[0]*u2[1] + u2[0]*u1[1], u1[1]*u2[1]))

def odej(u1, u2): return skroc((u1[0]*u2[1] - u2[0]*u1[1], u1[1]*u2[1]))

def mnoz(u1, u2): return skroc((u1[0]*u2[0], u1[1]*u2[1]))

def dziel(u1, u2): return skroc((u1[0]*u2[1], u1[1]*u2[0]))

def pot(u, p):
    if p >= 0:
        return(u[0]**p, u[1]**p)
    if p < 0:
        return(u[1]**abs(p), u[0]**abs(p))


    return u1
#end

def skroc(u):
    def nwd(a, b):
        a = abs(a)
        while a * b != 0:
            print(a, b)
            if a >= b: a %= b
            if a == 0: break
            if b >= a: b %= a
            if b == 0: break
        return a + b
    # end def

    r = nwd(u[0], u[1])
    return (u[0]//r, u[1]//r)
# end def

"""
ax + by = c
dx + ey = f
"""

def wczytaj(s):
    a = skroc(tuple(map(int, input(s).split("/"))))
    return a
# end

a = wczytaj("a = ")
print(pot(a, -2))

b = wczytaj("b = ")
c = wczytaj("c = ")
d = wczytaj("d = ")
e = wczytaj("e = ")
f = wczytaj("f = ")

W = odej(mnoz(a, e), mnoz(b, d))
Wx = odej(mnoz(c, e), mnoz(b, f))
Wy = odej(mnoz(a, f), mnoz(c, d))

x = dziel(Wx, W)
y = dziel(Wy, W)
print(x, y)
