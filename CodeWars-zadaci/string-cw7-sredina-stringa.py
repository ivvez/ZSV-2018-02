#napisi program koji ce za ucitani string ispisati:
#srednji znak stringa ako string ima neparan broj znakova
#srednja dva znaka stringa ako string ima paran broj znakova
#ako string ima samo jedan znak, ispisat ce se taj znak

s=input()
if len(s)<=2:
    print (s)
if len(s)%2==0:
    print (s[len(s)//2 - 1:len(s)//2 + 1])
else:
    print (s[len(s)//2])
    
