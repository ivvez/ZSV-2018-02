'''

napisi funkciju koja za ucitane stranice a,b,c provjerava moze li se
od njih nacrtati trokut. U slucaju da moze vratit ce se True, inace False.

'''

def trokut(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)



