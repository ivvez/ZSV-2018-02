'''
Ako ispisemo sve prirodne brojeve do 10 koji su djeljivi s 3 ili 5, dobit cemo
brojeve: 3,5,6 i 9. Njihov zbroj je 23.
Napisi program koji ce za ucitani broj n ispisati zbroj brojeva djeljivih s
3 ili 5 do tog zadanog broja n.
'''

n=int(input())
z=0
for i in range(n):
    if i%3==0 or i%5==0:
        z+=i

print (z)
