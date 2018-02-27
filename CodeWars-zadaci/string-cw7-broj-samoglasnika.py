#za ucitani string ispisi koliko ima samoglasnika

n=input()
bs=0
for i in n:
    if i in 'aeiou':
        bs+=1

print (bs)
