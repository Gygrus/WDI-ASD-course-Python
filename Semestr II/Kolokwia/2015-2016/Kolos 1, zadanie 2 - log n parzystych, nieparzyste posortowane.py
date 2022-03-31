"""
Dana jest n elementowa tablica A zawierająca liczby naturalne (potencjalnie bardzo duże).
Wiadomo, że tablica A powstała w dwóch krokach. Najpierw wygenerowano losowo (z nieznanym
rozkładem) n różnych liczn nieparzystych i posortowano je rosnąco. Następnie wybrano losowo
dlog ne elementów powstałej tablicy i zamieniono je na losowo wybrane liczby parzyste. Proszę
zaproponować (bez implementacji!) algorytm sortowania tak powstałych danych. Algorytm
powinien być możliwie jak najszybszy. Proszę oszacować i podać jego złożoność czasową.
"""



"""
Tworzę pomocniczą tablicę o rozmiarze ceil(logn), w których zapiszę wartości liczb parzystych z tablicy A po przeiterowaniu
po jej elementach. Następnie posortuję pomocniczą tablicę za pomocą algorytmu countsort(złożoność liniowa O(logn)).
Następnie tworzę 2 pomocnicze "wskaźniki", które będę inkrementował w miarę iteracji przez indeksy od 0 do n-1. Wartość
każdego iterowanego elementu tablicy porównuję z kolejnymi, coraz większymi elementami z tablicy pomocniczej, dopóki są one
mniejsze od parzystej liczby porównywanej, wtedy podstawiam pod te indeksy wartości nieparzyste (które już są posortowane). Jeśli
natrafię na wartość parzystą, to jeden ze wskaźników nie jest inkrementowany, a kolejne wartości mniejsze od porównywanej liczby parzystej
są przypisywane pod miejsca w tablicy o indeksie wskazywanym przez wskaźnik o wartości mniejszej. Gdy dojdziemy do wartości większej od 
porównywanej parzystej, pod "mniejszy" wskaźnik podstawiamy naszą porównywaną parzystą, "mniejszy" wskaźnik zwiększamy o jeden i 
powtarzamy operację, porównując z kolejną parzystą liczbą z naszej tablicy pomocniczej
Złożoność: O(n + logn + n) = O(n)"""