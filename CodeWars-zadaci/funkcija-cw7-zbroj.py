'''Napisi funkciju koja za ucitana dva broja vraca zbroj svih brojeva
izmedju ta dva broja'''


def get_sum(a,b):
    z=0
    if a>b:
        for i in range(b,a+1):
            z+=i
    elif b>a:
        for i in range(a,b+1):
            z+=i
            
    return z
