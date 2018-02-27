'''
Napisi funkciju koja ce za ucitani string vratiti njegovu brojcanu vrijednost
prema pravilima: a=1, b=2, c=3.....z=26.

Npr.
s=love ---> l+o+v+e = 54
s=friendship ---> f+r+i+e+n+d+s+h+i+p=108


'''


def koliko(s):
    z=0
    abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for i in s:
        if i in abc:
            z+=int(abc.index(i))+1
  
    return z


#drugi nacin rjesenja pomocu naredbe ord


def koliko(s):
    z=0
    for i in s:
       z=z+(ord(i)-96)

    return z
