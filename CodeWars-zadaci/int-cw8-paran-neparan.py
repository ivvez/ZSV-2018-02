#Napisi program koji za ucitani cijeli broj ispisuje je li broj paran ili neparan

n=int(input())
if n%2==0:
    print ('Paran')
else:
    print ('Neparan')


#rjesenje u jednom retku
print ('Broj je paran') if n % 2 else ('Broj je neparan')
