"""
Liczby zespolone są reprezentowane przez krotkę (re, im). Gdzie: re - część rzeczywista liczby,
im - część urojona liczby. Proszę napisać podstawowe operacje na liczbach zespolonych, m.in. dodawanie,
odejmowanie, mnożenie, dzielenie, potęgowanie, wypisywanie i wczytywanie.
"""
from math import sqrt

def sprzezenie(a):
    return (a[0], -a[1])

def dodawanie(a, b):
    return (a[0] + b[0], a[1] + b[1])

def odejmowanie(a, b):
    return (a[0] - b[0], a[1] - b[1])

def mnozenie(a, b):
    return ((a[0] * b[0]) - (a[1] * b[1]), a[0] * b[1] + a[1] * b[0])

def dzielenie(a, b):
    return ((a[0]*b[0] - a[1] * sprzezenie(b)[1]) / (b[0]**2 + b[1]**2), (a[0] * (-b[1]) + a[1] * b[0]) / (b[0]**2 + b[1]**2))

def potegowanie(a, b):
    modul = sqrt(a[0]**2 + a[1]**2)
    cos = a[0]/modul
    sin = a[1]/modul


def wypisywanie(a):
    return f'{a[0]}, {a[1]}i'

def wczytywanie():
    re = int(input("Wpisz część rzeczywistą: "))
    im = int(input("Wpisz część urojoną: "))
    return (re, im)


a = wczytywanie()

b = (3, 5)
print((a[0]*b[0] - a[1] * sprzezenie(b)[1]))
print(b[0]**2 + b[1]**2)
print(dodawanie(a, b))
print(odejmowanie(a, b))
print(mnozenie(a, b))
print(dzielenie(a, b))


