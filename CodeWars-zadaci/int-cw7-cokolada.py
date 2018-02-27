'''
Tvoj zadatak je napisati program koji ce plocicu cokolade dimenzija n*m
razdijeliti na male kvadratice. Svaki kvadratic je velicine 1x1 i ne moze se
razlomiti na manji dio. Napisi program koji ce vratiti broj poteza koji je
potreban da se plocica razlomi na najmanji moguci broj kvadratica.

Npr. plocica velicine 2x1 se moze razdijeliti na 1x1 kvadratice u samo jednom
potezu, ali za velicinu 3x1 potrebno je dva poteza.
'''

#rjesenje 1:
n=int(input())
m=int(input())
print (max(n*m-1,0))


#rjesenje 2:
n=int(input())
m=int(input())
if n > 0 and m > 0:
    print (m*n - 1)
    else:
    print (0)
