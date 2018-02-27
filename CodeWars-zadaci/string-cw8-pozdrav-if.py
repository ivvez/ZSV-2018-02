'''
Ana je napisala program koji pozdravlja korisnika. No, kako joj se svidja Ivo,
odlucila je za njega napisati poseban pozdrav.
Pomozi joj da zavrsi svoj program. Napisi program koji za ucitani
string x, pozdravlja korisnika imenom u obliku: "Bok, x!", a u slucaju da je
ime Ivo, ispisat ce se poruka: "Bok Ivo, kako si danas?"

'''
x=input()
if x=='Ivo':
    print ('Bok Ivo, kako si danas?')
else:
    print ('Bok '+x+'!')
