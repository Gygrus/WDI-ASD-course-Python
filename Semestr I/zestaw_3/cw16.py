"""
Mamy zdefiniowaną n-elementową tablicę liczb całkowitych. Proszę napisać funkcję zwracającą wartość typu bool oznaczającą, czy w tablicy istnieje dokładnie jeden element najmniejszy i dokładnie
jeden element największy (liczba elementów najmniejszych oznacza liczbę takich elementów o tej samej
wartości).
"""

def check(t):
    return t.count(min(t)) == 1 and t.count(max(t)) == 1

print(check([3]))