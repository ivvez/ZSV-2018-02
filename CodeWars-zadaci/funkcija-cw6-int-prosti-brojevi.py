'''
Prosti brojevi su svi prirodni brojevi djeljivi bez ostatka
samo s brojem 1 i sami sa sobom, a strogo veci od broja 1.
Napisi funkciju koja ce za ucitani broj n provjeriti je li prosti broj ili ne.
'''

def is_prime(n):
    if n <= 1:
        return False
    elif n <=3:
        return True
    elif n%2 == 0 or n%3 == 0:
        return False
    i=5
    while i * i <= n:
        if n %i == 0 or n %(i + 2) == 0:
            return False
        i+=1
    return True
