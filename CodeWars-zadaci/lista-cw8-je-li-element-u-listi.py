'''
Pero trazi zlato u rijeci tako da kanticom zahvati zemlju na dnu rijeke i zatim
provjerava ima li u kantici zlata ili samo kamenja
Za zadanu listu koja predstavlja sadrzaj kantice ispisi True ili False
ovisno o tome nalazi li se u kantici zlato ili ne.
'''

l=[]
n=int(input('koliko zelis unosa?'))
for i in range(n):
    s=input('Upisi: zlato ili kamen')
    l.append(s)

if 'zlato' in l:
    print (True)
else:
    print (False)
