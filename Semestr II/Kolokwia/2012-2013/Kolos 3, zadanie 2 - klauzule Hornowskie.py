"""
Na wejściu dana jest formuła logiczna F postaci CNF (conjunctive normal form), czyli
F = C1 ∧ C2 ∧ ... ∧ Cm, gdzie każde Ci to tak zwana klauzula, czyli alternatywa zmiennych
logicznych lub ich negacji. Formuła w postaci CNF jest Hornowska jeśli każda klauzula zawiera
najwyżej jedną niezanegowaną zmienną. Przykłady Hornowskich formuł CNF to:
(x) ∧ (x ∨ y) ∧ (x ∨ y ∨ z), (x ∨ y) ∧ (x ∨ y), czy (x) ∧ (x). Proszę opisać wielomianowy algorytm,
który sprawdza czy Hornowska formuła w postaci CNF jest spełnialna (to znaczy, czy da się
przypisać wartości logiczne zmiennym tak, żeby formuła miała wartość prawda).
"""

"""
Zamieniamy wszystkie klauzule na implikacje (poprzednik to koniunkcja zmiennych, następnik to pojedyncza zmienna)
(klauzule zawierające jedną zmienną, która w dodatku nie jest zanegowana, traktujemy jako 1=>x po zmianie), 
następnie przechodząc przez wszystkie klauzule, zakładając na początku, że wszystkie zmienne są ustawione na fałsz,
następniki implikacji, które nie zachodzą dodajemy do zbioru zmiennych, które będą miały wartościowanie 1, następnie 
powtarzamy operację dodając do zbioru kolejne zmienne. Jeśli liczność zbioru jest równa n (liczba zmiennych), a formuła
nie jest spełniona, to oznacza, że formuła nie jest spełnialna.
"""