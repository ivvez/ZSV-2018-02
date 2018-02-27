'''
Napisi funkciju koja prima zadanu listu brojeva. Unutar te list jedan od brojeva
ce se uvijek pojaviti neparan broj puta. Program treba pronaci i ispisati taj
broj koji se ponavlja neparan broj puta.
'''

def pronadji(lista):
    for i in lista:
        if lista.count(i)%2!=0:
            return i
