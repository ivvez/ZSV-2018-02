#napisi program koji za ucitani broj ispisuje zbroj njegovih znamenki

a=int(input())
s=0
a=abs(a)
for i in str(a):
    s+=int(i)

print (s)
        
