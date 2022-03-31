"""Proszę opisać (bez implementacji!) jak najszybszy algorytm, który otrzymuje na wejściu pewien
ciąg n liter oraz liczbę k i wypisuje najczęściej powtarzający się podciąg długości k (jeśli ciągów
mogących stanowić rozwiązanie jest kilka, algorytm zwraca dowolny z nich). Można założyć, że
ciąg składa się wyłącznie z liter a i b.
Na przykład dla ciągu ababaaaabb oraz k = 3 rozwiązaniem jest zarówno ciąg aba, który
powtarza się dwa razy (to, że te wystąpienia na siebie nachodzą nie jest istotne). Zaproponowany
algorytm opisać, uzasadnić jego poprawność oraz oszacować jego złożoność.
"""


"""
Tworzę tablicę o długości 2^(k). W pętli for przechodzę po kolejnych elementach tablicy, sprawdzając kolejne
podciągi długości k. Ciągi znaków będę traktował jako liczby zapisane w systemie dwójkowym, to znaczy a odpowiada wartości 0,
a b odpowiada jedynce, np. dla k = 4, ciąg abab będzie miał przypisaną wartość 0*2^3 + 1*2^2 + 0*2^1 + 1*2^0 = 5. W stworzonej
tablicy pomocniczej będę inkrementował wartości pod odpowiednimi indeksami, które to indeksy będą wartościami odpowiadającymi
ciągom jako liczby w systemie dwójkowym. Na końcu iteruję znów przez ciąg liter, odczytując największą wartość z odpowiedniego indeksu 
(będzie to najczęściej występujący podciąg) i znając indeks, mogę numer tego indeksu przekonwertować na liczbę w systemie binarnym, 
która to będzie moim ciągiem, wystarczy zastąpić 0 jako 'a' i 1 jako 'b'. Złożoność obliczeniowa będzie wynosiła O(2(n-k))"""