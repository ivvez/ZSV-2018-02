
#Napisi program koji ce ucitani broj ispisati obrnuto

#Npr. 456 ---> 654

broj=int(input())
obrnuti=0
while(broj > 0):
    ostatak = broj %10
    obrnuti = (obrnuti *10) + ostatak
    broj = broj //10

print (obrnuti)
