'''
Marko i Ana izmislili su novu igru. Zove se Pronadji iglu u sijenu.
Marko na stol stavi jako puno predmeta i jednu malu iglu. Ana mora pronaci iglu.

Napisi program koji ce za ucitanu listu predmeta (mozes ih ucitati kao
string pa spremiti u listu) pronaci iglu te ispisati mjesto na listi na kojem
se igla nalazi i poruku: 'Pronasao sam iglu' 

'''

n=int(input('Broj predmeta:'))
l=[]
b=False
for i in range(n):
    p=input()
    l.append(p)

for i in l:
    if 'igla' in i:
        print ('Pronasao sam iglu na mjestu '+str(l.index(i)))
        b=True

if b==False:
    print ('Nema igle')
