'''
Napisi funkciju koja ce za ucitani string prebrojati:
velika slova, mala slova, brojeve i ostale znakove te vratiti listu
s rezultatima koliko kojih znakova ima.
'''


def broji(s):
    u=0
    l=0
    n=0
    s2=0
    for i in s:
        if i.islower():
            l+=1
        elif i.istitle():
            u+=1
        elif i.isdigit():
            n+=1
        else:
            s2+=1
    return [u,l,n,s2]

#test
print (broji('sadaABAB345(/&'))
