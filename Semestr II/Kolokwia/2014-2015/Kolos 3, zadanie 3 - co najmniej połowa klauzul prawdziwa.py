"""
Forma to koniunkcja klauzul. Klauzula to alternatywa zmiennych lub ich negacji. Przykład:
(¬a or b) and (¬b or c or d) and (a or d) and (¬a or ¬c or d). Forma składa się z m klauzul
(C1, ..., Cm). Jest n zmiennych (x1, ..., xn). Jak ustawić zmienne, aby co najmniej połowa klauzul
była spełniona? Oszacować złożoność i udowodnić poprawność algorytmu.
(Nie trzeba implementować).
"""

"""
Na początku ustawiamy wszystkie zmienne na "prawdę" i przeszukujemy klauzule, zliczając te spełnione.
Jeśli jest ich nie mniej niż połowa, to oznacza że znaleźliśmy takie przyporządkowanie, jeśli nie, to negujemy te formuły
i mamy pewność że tym razem co najmniej połowa jest spełniona. Dzieje się tak dlatego, że jeśli za pierwszym przyporzą-
dkowaniem nie mamy spełnionych co najmniej połowy klauzul, to oznacza że istnieje więcej niż połowa klauzul o postaci 
(¬a) and (¬b or ¬c) and (¬a or ¬c) (wszystkie zmienne zanegowane). Po zamienieniu wartościowań na przeciwne, te klauzule zmienią
się na spełnione, a więc będziemy mieli większość klauzul spełnionych.
Złożoność: O(n)
"""