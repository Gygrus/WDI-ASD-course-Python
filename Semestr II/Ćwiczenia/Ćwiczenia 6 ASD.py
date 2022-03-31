"""Zadanie 7. (sklejanie odcinków) Dany jest ciąg przedziałów postaci [ai
, bi]. Dwa przedziały można
skleić jeśli mają dokładnie jeden punkt wspólny. Proszę wskazać algorytmy dla następujących problemów:
1. Problem stwierdzenia, czy da się uzyskąć przedział [a, b] przez sklejanie odcinków.
2. Zadanie jak wyżej, ale każdy odcinek ma koszt i pytamy o minimalny koszt uzyskania odcinka [a, b].
3. Problem stwierdzenia jaki najdłuższy odcinek można uzyskać sklejając najwyżej k odcinków.
"""
a = 0
b = 9
F = [ [None]*(b+1) for _ in range(b+1) ]
S = [ (0, 3), (1, 5), (3, 7), (5, 7), (7, 9) ]

def intervals( i, j, F, S):
  if F[i][j] is not None: return F[i][j]

  if (i, j) in S:
    F[i][j] = True
    return F[i][j]

  q = False
  for k in range(i+1, j):
    q = ( intervals(i, k, F, S) and intervals(k, j, F, S) )
    if q: break

  F[i][j] = q
  return F[i][j]



print( intervals(1,5,F,S) )
print( intervals(0,3,F,S) )
print( intervals(0,5,F,S) )