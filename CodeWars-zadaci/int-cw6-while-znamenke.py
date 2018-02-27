'''
napisi program koji za ucitani broj n mnozi njegove znamenke sve dok ne dodje
do jednoznamenkastog broja. Program treba ispisati koliko puta se mnozenje
moze ponoviti.
Npr.
n=39 --->  3 (3*9=27, 2*7=14, 1*4=4)
n=999 ---> 4
n=4 ---->  0

'''


n=int(input())
m = 1
z=0
if n < 10:
    print (0)
else:
    while n > 0:
        m = n%10 * m
        n = n//10
        z+=1
    print (z+1)

