'''
Svi znamo kako funkcionira sustav "lajkanja" na Fejsbuku. Kada netko nesto
"lajka" ispod toga se pojavi tekst - Peter likes this...ili Peter and Ana like this...
itd.
Za ucitanu listu imena napisi funkciju koja ce ispisati odgovarajuci tekst.

[] - no one likes this
[Peter] - Peter likes this
[Peter, Ana] - Peter and Ana like this
[Peter, Ana, Jacob] - Peter, Ana and Jacob like this
[Alex, Jacob, Mark, Max] - Alex, Jacob and 2 others like this

'''

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return names[0] + " likes this"
    elif len(names) == 2:
        return names[0] + " and " + names[1] + " like this"
    elif len(names) == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        return names[0] + ", " + names[1] + " and " + str(len(names)-2) + " others like this"
