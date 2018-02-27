'''
Napisi program koji za ucitani string (recenicu) prvo slovo svake rijeci pomice
na kraj rijeci i nakon toga dodaje nastavak -ay. Pravilo ne vrijedi za pravopisne
znakove npr. !, ? itd.

Npr.
text="Pig Latin je super" ----> igPay atinLay eJay uperSay
text="Hello World !" ----> elloHay orldWay !


'''

text=input()

tn=''
br=0
for i in text.split():
    br+=1
    if i=='!' or i=='?':
        tn+=i[1:]+i[0]
    elif br==len(text.split()):
        tn+=i[1:]+i[0]+'ay'
    
    else:
        tn+=i[1:]+i[0]+'ay'+' '
print (tn)
