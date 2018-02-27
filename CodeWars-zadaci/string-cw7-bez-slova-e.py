#napisi program koji provjerava koliko puta se u unesenom stringu nalazi slovo e
#ukoliko slovo e ne postoji, treba se ispisati poruka 'Nema slova e'
s=input()
br=0
for i in s:
    if i in 'e':
        br+=1

if br==0:
    print ('Nema slova e')
else:
    print (br)
