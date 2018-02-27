'''Napisi program koji ce za ucitani url ukloniti sve iza znaka # u url adresi

Npr. www.codewars.com#about ----> www.codewars.com

'''

url=input()
z=url.split('#')
print (z[0])
