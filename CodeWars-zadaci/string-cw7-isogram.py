'''
Isogram je rijec u kojoj se ne ponavljaju slova tj.znakovi.
Napisi program koji ce za ucitanu rijec provjeriti je li isogram ili ne.
'''
rijec=input().lower()
b=0

for i in rijec:
    if rijec.count(i) > 1:
        b+=1

if b>0:
    print ('Nije isogram')
else:
    print ('Isogram')
    
    
