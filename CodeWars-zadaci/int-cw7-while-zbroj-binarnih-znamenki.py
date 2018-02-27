#napisi program koji ucitani broj n pretvara u binarni te zbraja njegove znamenke
#ukoliko zbroj binarnih znamenki ima vise od 1 znamenke, proces se ponavlja...
#...broj se opet pretvara u binarni te se zbrajaju znamenke

n=int(input())
while n > 9:
    n = bin(n).count("1")
print (n)
